[app]

# (str) Title of your application
title = 宠物语言翻译器

# (str) Package name
package.name = pettranslator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.pettranslator

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (version) Your application version
type = string
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1,cython==0.29.36

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (int) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path = 

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = @android:style/Theme.Holo.Light

# (list) Pattern to whitelist for the whole project
#android.whitelist = 

# (str) Path to a custom whitelist file
#android.whitelist_src = 

# (str) Path to a custom blacklist file
#android.blacklist_src = 

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process.
#android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src = 

# (list) Android AAR archives to add
#android.add_aars = 

# (list) Gradle dependencies to add
#android.gradle_dependencies = 

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies' 
# contains an AndroidX library or when 'android.enable_androidx' is True
android.enable_androidx = True

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "-Xlint:deprecation","-Xlint:unchecked"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes
# android.gradle_repositories = "https://kotlin.bintray.com/kotlinx/"

# (list) packaging options to add
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle dependencies
# android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'"
# android.add_packaging_options = "exclude 'META-INF/*.kotlin_module'"

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon = 

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters = 

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data = 

# (list) Android library project to add (will be added in the 
# project.properties automatically.)
#android.library_references = 

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_library = 

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules = 

# (str) If you need to insert variables into your AndroidManifest.xml file, 
# you can do so with the manifestPlaceholders property. 
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = [myCustomUrl:"org.kivy.customurl"]
# android.manifest_placeholders = 

# (str) Simon template android.permission 
#android.simon.permissions = 

# (str) Simon template android.meta_data 
#android.simon.meta_data = 

# (list) Android AAPT options
#android.aapt_options = 

# (list) options to pass to build.py
# build.py options
#android.buildtools = 29.0.3

# (str) python-for-android branch to use, defaults to master
p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes = 

# (str) Filename to the hook for p4a
#p4a.hook = 

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2
p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port = 

# (bool) Whether or not to package the entire Python distribution
# (runs python-for-android with --pack-python flag)
#p4a.pack_python = False

# (str) The directory where buildozer should look for p4a recipes when using a source directory
#p4a.recipes_dir = 

# (str) The directory where buildozer should look for android recipes
#p4a.local_recipes = 

# (str) The directory where buildozer should look for a custom bootstrap
#p4a.bootstrap_dir = 

# (str) The SDK directory to use
#p4a.sdk_dir = 

# (str) The NDK directory to use
#p4a.ndk_dir = 

# (str) The Android API to use
#p4a.api = 27

# (str) The Android SDK tools version to use
#p4a.sdk_tools = 24.4.1

# (str) The build tools version to use
#p4a.buildtools = 28.0.3

# (str) The extra args to pass to the android tool
#p4a.extra_args = 

# (bool) Enable verbose mode. Do not set this to True if you are not debugging something
#p4a.verbose = False


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

# (list) List of application packages to install in the build environment
#    (e.g. pip, cython, pygments etc.)
# requirements = 

# (str) Filename of the package to use for the repo (if empty, package.name will be used)
# package = 

# (str) Device spec to use (see `buildozer device list`)
# device = 

# (str) Bootstrap to use for iOS builds
# ios.bootstrap = sdl2

# (str) List of iOS SDK versions to use
# ios.sdk = ["9.3", "10.0", "10.1", "10.2"]

# (str) List of architectures to build for iOS
# ios.arch = arm64,armv7

# (bool) Always use the latest SDK instead of the one specified above
# ios.use_latest_sdk = False

# (str) iOS Xcode project setting, you can use this property to override the
# default value of IPHONEOS_DEPLOYMENT_TARGET. Minimum version is 8.0
# ios.deployment_target = 8.0

# (str) Name of the certificate to use for signing the debug version
# Get a list of available certificates: buildozer ios list_certificates
# ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
# ios.codesign.release = %(ios.codesign.debug)s


[app:debug]

# (bool) Skip debug builds
# skip = False

# (int) How much debug information to log (0 = none, 1 = errors, 2 = warnings, 3 = info)
# log_level = 1

[app:release]

# (bool) Skip release builds
# skip = False

# (int) How much debug information to log (0 = none, 1 = errors, 2 = warnings, 3 = info)
# log_level = 1
