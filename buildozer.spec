[app]

# App 基本信息
title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Python / Kivy / Cython
requirements = python3,kivy==2.3.1,cython==0.29.36

# Orientation
orientation = portrait
fullscreen = 0

# Android 配置
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a
android.permissions = INTERNET
android.enable_androidx = True
android.allow_backup = True
android.accept_sdk_license = True

# Python-for-Android 配置
p4a.branch = develop

[buildozer]

log_level = 2
warn_on_root = 1
android.add_sqlite3 = False
