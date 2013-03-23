ffmake
======

It's another script-driven build system. But, hopefully a hell of a 
lot easier to maintain than Gyp, SCons, or CMake.

It's less full-featured, but then, I could care less about OpenVMS
Makefiles or OpenWatcom.

The stated goal of this project is to ge nerate project and solution
files for the following major development environments and build
system command lines (at least, these are the things I am personally
going to invest time in supporting):

- Microsoft Visual Studio 2012 for Desktop (msbuild)
- Apple Xcode 4.5 for OS X and iOS (xcodebuild)
- Android.mk files (ndk-build)

To do this, ffmake uses Mustache templates, customizing as little
as possible when compared to the stock project templates.