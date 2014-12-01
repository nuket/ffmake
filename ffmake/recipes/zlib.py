"""
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
"""

#
# Note the use of raw strings for paths, ffmake will convert
# paths to use the proper path separator when generating output.
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


# ------------------------------------------------------------------------
# Targets
# ------------------------------------------------------------------------

# Don't specify a 'name' here. The ProjectFactory takes a single
# 'name' param, which it uses convention over configuration to
# create the project names.
#
# 'static_library' generates 'name_static'.project
# 'shared_library' generates 'name_shared'.project
# 'executable'     generates 'name_executable'.project

ZLIB_STATIC_TARGET      = { 'build_type':                'static_library',
                            'source_dir':                ZLIB_SOURCE_DIR,
                            'source_files':              ZLIB_SOURCE_FILES,
                            'include_dirs':              ZLIB_INCLUDE_DIRS,
                            'include_dirs_shared':       [],
                            'include_dirs_static':       [],
                            'include_dirs_debug':        [],
                            'include_dirs_release':      [],
                            'include_dirs_32bit':        ZLIB_INCLUDE_DIRS_32BIT,
                            'include_dirs_64bit':        ZLIB_INCLUDE_DIRS_64BIT,
                            'preprocessor_defs':         ZLIB_PP_DEFS,
                            'preprocessor_defs_shared':  [],
                            'preprocessor_defs_static':  [],
                            'preprocessor_defs_debug':   [],
                            'preprocessor_defs_release': [],
                            'preprocessor_defs_32bit':   [],
                            'preprocessor_defs_64bit':   ZLIB_PP_DEFS_64BIT }

ZLIB_SHARED_TARGET      = { 'build_type':                'shared_library',
                            'source_dir':                ZLIB_SOURCE_DIR,
                            'source_files':              ZLIB_SOURCE_FILES,
                            'include_dirs':              ZLIB_INCLUDE_DIRS,
                            'include_dirs_shared':       [],
                            'include_dirs_static':       [],
                            'include_dirs_debug':        [],
                            'include_dirs_release':      [],
                            'include_dirs_32bit':        ZLIB_INCLUDE_DIRS_32BIT,
                            'include_dirs_64bit':        ZLIB_INCLUDE_DIRS_64BIT,
                            'preprocessor_defs':         ZLIB_PP_DEFS,
                            'preprocessor_defs_shared':  [],
                            'preprocessor_defs_static':  [],
                            'preprocessor_defs_debug':   [],
                            'preprocessor_defs_release': [],
                            'preprocessor_defs_32bit':   [],
                            'preprocessor_defs_64bit':   ZLIB_PP_DEFS_64BIT }

# zlib = ffmake.ProjectFactory(name="zlib",
#                              project_types=["VS2012", "Android.mk"],
#                              
#                              )

zlib_static = ffmake.WindowsProject(name="zlib", 
                                    build_type="static_library",
                                    source_dir=ZLIB_SOURCE_DIR,
                                    source_files=ZLIB_SOURCE_FILES,
                                    include_dirs=ZLIB_INCLUDE_DIRS,
                                    include_dirs_shared=[],
                                    include_dirs_static=[],
                                    include_dirs_debug=[],
                                    include_dirs_release=[],
                                    include_dirs_32bit=ZLIB_INCLUDE_DIRS_32BIT,
                                    include_dirs_64bit=ZLIB_INCLUDE_DIRS_64BIT,
                                    preprocessor_defs=ZLIB_PP_DEFS,
                                    preprocessor_defs_shared=[],
                                    preprocessor_defs_static=[],
                                    preprocessor_defs_debug=[],
                                    preprocessor_defs_release=[],
                                    preprocessor_defs_32bit=[],
                                    preprocessor_defs_64bit=ZLIB_PP_DEFS_64BIT)
