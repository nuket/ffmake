ffmake
======

It's another script-driven build system. But, hopefully a hell of a 
lot easier to maintain than [Gyp](https://code.google.com/p/gyp/), [Scons](http://www.scons.org/), or [CMake](http://www.cmake.org/).

It's less full-featured, but then, I could care less about OpenVMS
Makefiles or OpenWatcom.

The stated goal of this project is to generate project and solution
files for the following major development environments and build
system command lines (at least, these are the things I am personally
going to invest time in supporting):

- Microsoft Visual Studio 2012 for Desktop (msbuild)
- Apple Xcode 4.5 for OS X and iOS (xcodebuild)
- Android.mk files (ndk-build)

In all of these cases, I'm currently focusing on native C++ development,
but ffmake should easily be able to generate other project files.

To do this, ffmake uses Mustache templates based on the stock project
template outputs, customizing as little as possible when compared to those 
stock project templates.

In other words, you should be able to roundtrip pretty easily, because
our inputs and outputs are diff'able plaintext files. So changes made
while you're in the native IDE can be easily backported to the project 
templates.