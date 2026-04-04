from __future__ import annotations

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

from pet_translator_logic import translate_by_text, random_sentence
from speech_android import request_mic_permission, start_speech_recognition

KV = '''
<RootWidget>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    
    Label:
        text: '宠物语言翻译器'
        font_size: '20sp'
        size_hint_y: None
        height: 50
    
    BoxLayout:
        size_hint_y: None
        height: 50
        spacing: 10
        
        Label:
            text: '宠物类型:'
            size_hint_x: None
            width: 80
        Spinner:
            id: pet_spinner
            text: root.pet_type
            values: ['猫', '狗', '自动']
            on_text: root.pet_type = self.text
    
    Label:
        text: '输入文字或点击"开始听"进行语音识别'
        size_hint_y: None
        height: 30
        color: 0.5, 0.5, 0.5, 1
    
    TextInput:
        id: input_text
        hint_text: '例如：喵喵 / 汪汪 / 我饿了'
        multiline: True
        size_hint_y: None
        height: 100
    
    BoxLayout:
        size_hint_y: None
        height: 50
        spacing: 10
        
        Button:
            text: '开始听'
            on_release: root.on_start_listen()
        Button:
            text: '翻译'
            on_release: root.on_translate()
        Button:
            text: '随机一句'
            on_release: root.on_random()
    
    Label:
        text: '识别结果:'
        size_hint_y: None
        height: 30
    
    Label:
        id: recognized_label
        text: '-'
        text_size: self.width, None
        size_hint_y: None
        height: 60
        valign: 'top'
    
    Label:
        text: '翻译结果:'
        size_hint_y: None
        height: 30
    
    Label:
        id: translation_label
        text: '-'
        text_size: self.width, None
        size_hint_y: None
        height: 100
        valign: 'top'
    
    Label:
        text: root.status
        size_hint_y: None
        height: 30
        color: 0.5, 0.5, 0.5, 1
'''

class RootWidget(BoxLayout):
    pet_type = StringProperty('猫')
    status = StringProperty('就绪')
    
    def on_start_listen(self):
        self.status = '正在请求麦克风权限...'
        
        def on_granted():
            self.status = '正在听...'
            
            def on_result(text):
                self.status = '识别完成'
                self.ids.recognized_label.text = text
                if text:
                    translation = translate_by_text(self.pet_type, text)
                    self.ids.translation_label.text = translation
            
            def on_error(msg):
                self.status = '识别失败'
                self.ids.translation_label.text = msg
            
            start_speech_recognition(on_result, on_error)
        
        def on_denied():
            self.status = '麦克风权限被拒绝'
            self.ids.translation_label.text = '需要麦克风权限才能进行语音识别'
        
        request_mic_permission(on_granted, on_denied)
    
    def on_translate(self):
        text = self.ids.input_text.text.strip()
        if not text:
            self.status = '请输入文字'
            return
        
        self.status = '正在翻译...'
        translation = translate_by_text(self.pet_type, text)
        self.ids.recognized_label.text = text
        self.ids.translation_label.text = translation
        self.status = '翻译完成'
    
    def on_random(self):
        self.status = '生成随机语句...'
        sentence = random_sentence(self.pet_type)
        self.ids.recognized_label.text = ''
        self.ids.translation_label.text = sentence
        self.status = '生成完成'

class PetTranslatorApp(App):
    def build(self):
        Builder.load_string(KV)
        return RootWidget()

if __name__ == '__main__':
    PetTranslatorApp().run()
