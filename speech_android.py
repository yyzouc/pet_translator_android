from __future__ import annotations

from kivy.utils import platform
from kivy.clock import Clock

IS_ANDROID = platform == "android"

def request_mic_permission(on_granted, on_denied=None):
    """
    请求麦克风权限
    """
    if not IS_ANDROID:
        if on_granted:
            on_granted()
        return
    
    try:
        from android.permissions import Permission, request_permissions
        
        def _granted(permissions, granted):
            if granted and on_granted:
                on_granted()
        
        def _denied(permissions, denied):
            if on_denied:
                on_denied()
        
        request_permissions(
            [Permission.RECORD_AUDIO],
            _granted,
            _denied
        )
    except Exception as e:
        print(f"请求麦克风权限失败: {e}")
        if on_denied:
            on_denied()

def start_speech_recognition(callback, error_callback=None, language="zh-CN"):
    """
    启动语音识别
    """
    if not IS_ANDROID:
        if error_callback:
            error_callback("非Android设备不支持语音识别")
        return
    
    try:
        from android import activity
        from android.runnable import run_on_ui_thread
        from jnius import autoclass, PythonJavaClass, java_method
        
        SpeechRecognizer = autoclass("android.speech.SpeechRecognizer")
        RecognizerIntent = autoclass("android.speech.RecognizerIntent")
        Intent = autoclass("android.content.Intent")
        
        class SpeechListener(PythonJavaClass):
            __javainterfaces__ = ["android/speech/RecognitionListener"]
            __javacontext__ = "app"
            
            def __init__(self, cb, eb):
                super().__init__()
                self.callback = cb
                self.error_callback = eb
            
            @java_method("(Landroid/os/Bundle;)V")
            def onResults(self, results):
                try:
                    results_key = SpeechRecognizer.RESULTS_RECOGNITION
                    matches = results.getStringArrayList(results_key)
                    if matches and len(matches) > 0:
                        best_match = matches.get(0)
                        if self.callback:
                            Clock.schedule_once(lambda dt: self.callback(best_match), 0)
                    else:
                        if self.callback:
                            Clock.schedule_once(lambda dt: self.callback(""), 0)
                except Exception as e:
                    print(f"处理识别结果失败: {e}")
                    if self.error_callback:
                        Clock.schedule_once(lambda dt: self.error_callback("识别结果处理失败"), 0)
            
            @java_method("(I)V")
            def onError(self, error):
                error_msgs = {
                    1: "网络错误",
                    2: "语音识别服务忙",
                    3: "无匹配结果",
                    4: "识别超时",
                    5: "语音识别服务不可用",
                    6: "语音识别服务被拒绝",
                    7: "语音识别权限被拒绝"
                }
                msg = error_msgs.get(error, f"识别错误: {error}")
                if self.error_callback:
                    Clock.schedule_once(lambda dt: self.error_callback(msg), 0)
            
            # 其他必要的回调方法
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
        def start_recognition():
            try:
                if not SpeechRecognizer.isRecognitionAvailable(activity):
                    if error_callback:
                        Clock.schedule_once(lambda dt: error_callback("语音识别服务不可用"), 0)
                    return
                
                recognizer = SpeechRecognizer.createSpeechRecognizer(activity)
                if not recognizer:
                    if error_callback:
                        Clock.schedule_once(lambda dt: error_callback("创建语音识别器失败"), 0)
                    return
                
                intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, language)
                intent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 1)
                
                listener = SpeechListener(callback, error_callback)
                recognizer.setRecognitionListener(listener)
                recognizer.startListening(intent)
            except Exception as e:
                print(f"启动语音识别失败: {e}")
                if error_callback:
                    Clock.schedule_once(lambda dt: error_callback(f"启动语音识别失败: {e}"), 0)
        
        start_recognition()
    except Exception as e:
        print(f"语音识别初始化失败: {e}")
        if error_callback:
            error_callback(f"语音识别初始化失败: {e}")
