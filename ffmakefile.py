"""
Copyright (c) 2013 Max Vilimpoc

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
"""

import ffmake

# ffmake.GenerateProjects(types=["VS2012", "Xcode45", "Android.mk"])

#
# Note the use of raw strings for paths on Windows.
#
ZLIB_SOURCE_DIR         = r'..\ffmakeexternal\zlib-1.2.7'
ZLIB_INCLUDE_DIRS       = [ZLIB_SOURCE_DIR]
ZLIB_INCLUDE_DIRS_32BIT = [ZLIB_SOURCE_DIR + r'\contrib\masmx86']
ZLIB_INCLUDE_DIRS_64BIT = [ZLIB_SOURCE_DIR + r'\contrib\masmx64']
ZLIB_SOURCE_FILES       = ['adler32.c',
                           'compress.c',
                           'crc32.c',
                           'deflate.c',
                           'gzclose.c',
                           'gzlib.c',
                           'gzread.c',
                           'gzwrite.c',
                           'infback.c',
                           'inffast.c',
                           'inflate.c',
                           'inftrees.c',
                           'trees.c',
                           'uncompr.c',
                           'zutil.c',]
ZLIB_PP_DEFS            = ['ZLIB_WINAPI',
                           '_CRT_NONSTDC_NO_DEPRECATE',
                           '_CRT_SECURE_NO_DEPRECATE',
                           '_CRT_NONSTDC_NO_WARNINGS']
ZLIB_PP_DEFS_64BIT      = ['WIN64']

# zlib = ffmake.ProjectFactory(project_types=["VS2012", "Android.mk"],
#                              build_types=['static_library', 'shared_library'],
# 
#                              name="zlib")

zlib_static = ffmake.WindowsProject(name="zlib", 
                                    build_type="static_library",
                                    source_dir=ZLIB_SOURCE_DIR,
                                    source_files=ZLIB_SOURCE_FILES,
                                    include_dirs=ZLIB_INCLUDE_DIRS,
                                    include_dirs_shared=['..\shared'],
                                    include_dirs_static=['..\static'],
                                    include_dirs_debug=['../debug'],
                                    include_dirs_release=['../release'],
                                    include_dirs_32bit=ZLIB_INCLUDE_DIRS_32BIT,
                                    include_dirs_64bit=ZLIB_INCLUDE_DIRS_64BIT,
                                    preprocessor_defs=ZLIB_PP_DEFS,
                                    preprocessor_defs_shared=[],
                                    preprocessor_defs_static=[],
                                    preprocessor_defs_debug=[],
                                    preprocessor_defs_release=[],
                                    preprocessor_defs_32bit=[],
                                    preprocessor_defs_64bit=ZLIB_PP_DEFS_64BIT)

print zlib_static.render()

zlib_shared = ffmake.WindowsProject(name="zlib",
                                    build_type="shared_library",
                                    source_dir=r"..\ffmakeexternal\zlib-1.2.7")

"""
L = Project(name='MyLib',
            result='StaticLibrary',
            source_root='')
L.render(where="outputdir")
"""

"""
E = Project(name='MyExe',
            dependencies = [ L ])

S = Solution(name='MySolution',
             projects = [ L, E ])
"""

"""
# Generate the solution, project files in the current working directory
# with all paths relative to that directory.

if __name__ == "__main__":
    wp = WindowsProject(name="ConsoleExe", build_type="windows_executable", source_dir="", source_files=[])
    print wp.render()
    
    ws = WindowsSolution(name="MySolution", projects=[wp])
    print ws.render()
"""
