from __future__ import annotations

from kivy.utils import platform
from kivy.clock import Clock


IS_ANDROID = platform == "android"


def request_mic_permission(on_granted, on_denied=None) -> None:
    """
    Android 上请求麦克风权限后再开始识别。
    桌面/非 Android：直接回调 on_granted。
    """
    if not IS_ANDROID:
        on_granted()
        return

    from android.permissions import Permission, request_permissions

    def _granted():
        on_granted()

    def _denied():
        if on_denied:
            on_denied()

    request_permissions(
        [Permission.RECORD_AUDIO],
        on_granted=_granted,
        on_deny=_denied,
    )


def start_speech_recognition(callback, error_callback=None, language: str = "zh-CN") -> None:
    """
    Android: 调用系统语音识别，结束后把识别出的文字回调给 callback(text)。
    桌面: 直接提示错误（因为无法读麦）。
    """
    if not IS_ANDROID:
        if error_callback:
            error_callback("桌面模式：这里无法进行语音识别，请在界面输入文字。")
        else:
            raise RuntimeError("Desktop mode cannot do speech recognition.")
        return

    # 延迟导入，避免桌面环境 import 失败
    from android import activity
    from android.runnable import run_on_ui_thread
    from jnius import autoclass, PythonJavaClass, java_method

    SpeechRecognizer = autoclass("android.speech.SpeechRecognizer")
    RecognizerIntent = autoclass("android.speech.RecognizerIntent")
    Intent = autoclass("android.content.Intent")
    Bundle = autoclass("android.os.Bundle")

    # SpeechRecognizer.RESULTS_RECOGNITION 常量键
    results_key = SpeechRecognizer.RESULTS_RECOGNITION

    class Listener(PythonJavaClass):
        __javainterfaces__ = ["android/speech/RecognitionListener"]
        __javacontext__ = "app"

        def __init__(self, cb, eb):
            super().__init__()
            self._cb = cb
            self._eb = eb

        @java_method("(Landroid/os/Bundle;)V")
        def onResults(self, results):
            try:
                arr = results.getStringArrayList(results_key)
                best = ""
                if arr is not None and arr.size() > 0:
                    best = arr.get(0)
            except Exception:
                best = ""

            def _notify(dt):
                self._cb(best or "")

            Clock.schedule_once(_notify, 0)

        @java_method("(I)V")
        def onError(self, error):
            def _notify(dt):
                if self._eb:
                    self._eb(f"语音识别失败（error={error}）。请重试。")

            Clock.schedule_once(_notify, 0)

        # 其余回调保持空实现，满足接口要求
        @java_method("(Landroid/os/Bundle;)V")
        def onReadyForSpeech(self, params):
            pass

        @java_method("()V")
        def onBeginningOfSpeech(self):
            pass

        @java_method("(F)V")
        def onRmsChanged(self, rmsdB):
            pass

        @java_method("([B)V")
        def onBufferReceived(self, buffer):
            pass

        @java_method("()V")
        def onEndOfSpeech(self):
            pass

        @java_method("(Landroid/os/Bundle;)V")
        def onPartialResults(self, partialResults):
            pass

        @java_method("(ILandroid/os/Bundle;)V")
        def onEvent(self, eventType, params):
            pass

    @run_on_ui_thread
    def _start():
        rec = SpeechRecognizer.createSpeechRecognizer(activity)

        # 让识别结果更偏向“中文”，并尽量一次性返回结果
        intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, language)
        intent.putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, False)
        # 结果最多返回多条（我们只取第一条）
        intent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 3)

        listener = Listener(callback, error_callback)
        rec.setRecognitionListener(listener)
        rec.startListening(intent)

    request_mic_permission(
        on_granted=_start,
        on_denied=(lambda: (error_callback and error_callback("麦克风权限被拒绝。"))),
    )

