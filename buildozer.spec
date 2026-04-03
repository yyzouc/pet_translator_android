[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain
package.domain = org.test

# (str) Source code
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Version
version = 0.1

# ✅ 修复：移除 cython（关键）
requirements = python3,kivy==2.3.1

# (list) Supported orientations
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# ✅ 必加权限（避免闪退）
android.permissions = INTERNET

# ✅ 统一 API / SDK（避免兼容问题）
android.api = 33
android.minapi = 21
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (list) 架构
android.archs = arm64-v8a

# (bool) Allow backup
android.allow_backup = True

# ✅ Debug 输出格式
android.debug_artifact = apk

# ✅ 关键：稳定分支（不要用 develop）
p4a.branch = master

# (bool) 自动接受 license（CI 必须）
android.accept_sdk_license = True


#
# iOS（保留原样，不影响 Android 构建）
#
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

ios.codesign.allowed = false


[buildozer]

# (int) Log level
log_level = 2

# (int) Warn on root
warn_on_root = 1

# （可选）你原来的设置
android.add_sqlite3 = False
android.accept_sdk_license = True
