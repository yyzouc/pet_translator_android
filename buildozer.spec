[app]

title = My Application
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# ✅ 核心：稳定组合
requirements = python3,kivy==2.3.1,cython==0.29.36

orientation = portrait
fullscreen = 0

# Android
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 25b

android.archs = arm64-v8a
android.permissions = INTERNET

android.allow_backup = True
android.accept_sdk_license = True

# ❗不要用 develop（不稳定）
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
