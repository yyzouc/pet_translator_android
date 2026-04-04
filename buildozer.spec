[app]

title = My Application
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# ✅ 稳定组合（关键）
requirements = python3,kivy==2.3.1,cython==0.29.36

orientation = portrait
fullscreen = 0

# Android 配置
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 25b

android.archs = arm64-v8a
android.permissions = INTERNET

# ⭐ 关键（解决 Gradle 崩溃）
android.enable_androidx = True

android.allow_backup = True
android.accept_sdk_license = True

# ⭐ 关键（锁版本避免 SDL2 patch 崩）
p4a.branch = master
p4a.bootstrap = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
