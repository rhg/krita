set(CMAKE_SYSTEM_NAME Android)
set(CMAKE_SYSTEM_VERSION 21) # API level
set(CMAKE_ANDROID_ARCH_ABI armeabi-v7a)
set(CMAKE_ANDROID_STANDALONE_TOOLCHAIN /home/dashed/arm-linux-androideabi)
set(CMAKE_FIND_ROOT_PATH /home/dashed/android-root;/home/dashed/Qt/5.11.1/android_armv7)

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)
SET(CMAKE_INCLUDE_PATH ${CMAKE_INCLUDE_PATH} "/home/dashed/crystax-ndk-10.3.2/sources/boost/1.59.0/include")
SET(CMAKE_LIBRARY_PATH ${CMAKE_LIBRARY_PATH} "/home/dashed/crystax-ndk-10.3.2/sources/boost/1.59.0/libs/armeabi-v7a/gnu-4.9")
