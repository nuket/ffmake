# ffmake

It's another script-driven build system. But, hopefully a hell of a 
lot easier to maintain than [Gyp](https://code.google.com/p/gyp/), [Scons](http://www.scons.org/), or [CMake](http://www.cmake.org/).

It's currently way less full-featured than those build systems, but then, 
I could care less about OpenVMS Makefiles or OpenWatcom.

The stated goal of this project is to generate project and solution
files for the following major development environments and build
system command lines (at least, these are the things I am personally
going to invest time in supporting):

- Microsoft Visual Studio 2013 for Desktop (msbuild)
- Apple Xcode 6.1 for OS X and iOS (xcodebuild)
- Android.mk files (ndk-build)

In all of these cases, I'm currently focusing on native C++ development,
but ffmake should easily be able to generate other project files.

To do this, ffmake uses [Jinja templates](http://jinja.pocoo.org/) based on the stock project
templates from those development environments, customizing as little as possible when compared to those 
templates. 

ffmake does not try to have some kind of (ultimately 
incomplete) custom internal model of what a build looks like that it then 
maps through some kind of generator. All you do is specify a few lists of
files, includes, include dirs, and preprocessor defines, and it just 
plugs those values into the templates, which you can easily create 
yourself.

In other words, you should be able to roundtrip pretty easily, because
our inputs and outputs are diff'able plaintext files. So changes made
while you're in the native IDE can be easily backported to the project 
templates.

# Contributing

If you'd like to work on ffmake:

    git clone git@github.com:nuket/ffmake.git
    git checkout develop

Work on it, commit, push, and send me a pull request!

# License

Copyright (c) 2013-2015 Max Vilimpoc

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom 
the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.
