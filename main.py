from __future__ import annotations

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.utils import platform

from pet_translator_logic import random_sentence, translate_by_text
from speech_android import request_mic_permission, start_speech_recognition


KV = r"""
<RootWidget>:
    orientation: "vertical"
    padding: dp(14)
    spacing: dp(10)

    BoxLayout:
        size_hint_y: None
        height: dp(40)
        spacing: dp(10)

        Label:
            text: "宠物语言翻译器"
            font_size: "18sp"

    BoxLayout:
        size_hint_y: None
        height: dp(40)
        spacing: dp(10)

        Label:
            text: "宠物类型"
            size_hint_x: None
            width: dp(80)
        Spinner:
            id: pet_spinner
            text: root.pet_type
            values: ["猫", "狗", "自动"]
            on_text: root.pet_type = self.text

    Label:
        text: "你可以输入文字（桌面模式）或点击“开始听”。"
        color: 0.3, 0.3, 0.3, 1
        size_hint_y: None
        height: dp(30)

    TextInput:
        id: input_text
        hint_text: "例如：喵喵 / 呼噜 / 汪汪 / 我要吃 / 有情况"
        multiline: True
        height: dp(120)

    BoxLayout:
        size_hint_y: None
        height: dp(44)
        spacing: dp(10)

        Button:
            text: "开始听"
            on_release: root.on_start_listen()

        Button:
            text: "翻译"
            on_release: root.on_translate_text()

        Button:
            text: "随机一句"
            on_release: root.on_random()

    Label:
        text: "识别到的文字："
        size_hint_y: None
        height: dp(24)
        color: 0.2, 0.2, 0.2, 1

    Label:
        id: recognized_label
        text: "-"
        text_size: self.width, None
        size_hint_y: None
        height: dp(70)
        valign: "top"
        halign: "left"

    Label:
        text: "翻译结果："
        size_hint_y: None
        height: dp(24)
        color: 0.2, 0.2, 0.2, 1

    Label:
        id: output_label
        text: "-"
        text_size: self.width, None
        size_hint_y: None
        height: dp(140)
        valign: "top"
        halign: "left"
        color: 0, 0, 0, 1

    BoxLayout:
        size_hint_y: None
        height: dp(40)

        Label:
            text: root.status_text
            color: 0.35, 0.35, 0.35, 1

"""


class RootWidget(BoxLayout):
    pet_type: str = StringProperty("猫")
    status_text: str = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._listening = False

    def _get_input_text(self) -> str:
        ti = self.ids["input_text"]
        return (ti.text or "").strip()

    def _set_output(self, recognized: str, translated: str) -> None:
        self.ids["recognized_label"].text = recognized if recognized else "-"
        self.ids["output_label"].text = translated if translated else "-"

    def on_translate_text(self) -> None:
        text = self._get_input_text()
        if not text:
            self.status_text = "请输入内容后再翻译。"
            return
        out = translate_by_text(self.pet_type, text)
        self._set_output(text, out)
        self.status_text = "已翻译（文字输入）。"

    def on_random(self) -> None:
        out = random_sentence(self.pet_type if self.pet_type != "自动" else "猫")
        self._set_output("", out)
        self.status_text = "已生成随机一句。"

    def on_start_listen(self) -> None:
        if self._listening:
            self.status_text = "正在识别中，请稍等。"
            return
        self._listening = True
        self.status_text = "正在听……"

        def _ok():
            # 真正开始识别
            def _cb(rec_text: str):
                self._listening = False
                self.status_text = "识别完成。"
                if not rec_text.strip():
                    self._set_output("", "我没听清，可以再说一次吗？")
                    return
                out = translate_by_text(self.pet_type, rec_text)
                self._set_output(rec_text, out)

            def _err(msg: str):
                self._listening = False
                self.status_text = "识别失败。"
                self._set_output("", msg)

            start_speech_recognition(callback=_cb, error_callback=_err, language="zh-CN")

        def _denied():
            self._listening = False
            self.status_text = "麦克风权限被拒绝。"
            self._set_output("", "需要麦克风权限才能进行语音识别。")

        request_mic_permission(on_granted=_ok, on_denied=_denied)


class PetTranslatorApp(App):
    def build(self):
        Builder.load_string(KV)
        return RootWidget()


if __name__ == "__main__":
    PetTranslatorApp().run()

