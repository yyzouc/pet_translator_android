宠物语言翻译器（Android APK）

功能：
- 支持猫/狗（以及“自动”判断）
- 通过手机语音识别，把识别文字翻译成中文“宠物想表达的话”
- 同时支持文字输入（桌面/调试时可用）

项目结构：
- `main.py`：Kivy 界面与交互
- `pet_translator_logic.py`：猫/狗翻译规则（关键词匹配 + 随机话术）
- `speech_android.py`：Android 语音识别（系统 SpeechRecognizer）
- `buildozer.spec`：打包配置

WSL 打包（生成 APK）：
1. 安装依赖（在 WSL 的 Ubuntu 里）：
   - `sudo apt update`
   - `sudo apt install -y git curl zip unzip openjdk-17-jdk`
   - `python3 -m pip install --upgrade pip`
   - `python3 -m pip install buildozer`

2. 进入项目目录：
   - 假设你的 Windows 路径是 `d:\Python\recruit`，在 WSL 里一般是 `/mnt/d/Python/recruit`
   - `cd /mnt/d/Python/recruit/pet_translator_android`

3. 生成 APK（debug）：
   - `buildozer android debug`

APK 输出目录通常在：
- `bin/`

提示：
- 语音识别用的是 Android 系统的 SpeechRecognizer，可能会需要联网；所以保留了 `INTERNET` 权限。
- 如果你在某些手机上识别结果不稳定，可以在界面里把输入改成手动文字测试翻译规则。

