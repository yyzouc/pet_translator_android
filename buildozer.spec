[app]

title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 关键：固定兼容版本
requirements = python3.10,kivy==2.3.1,cython==3.0.2

orientation = portrait
fullscreen = 0

# Android配置
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True

# Python for Android
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
