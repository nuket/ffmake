#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import ffmake
# import ffmake.recipes.zlib

# Generate the solution, project files in the current working directory
# with all paths relative to that directory.

if __name__ == "__main__":
    # zlib = ffmake.recipes.zlib.Project(source_dir='')

    # test_project_A = ffmake.VS2012Project(name="ProjectA", build_type="static_library")
    # test_project_B = ffmake.VS2012Project(name="ProjectB", build_type="static_library", dependencies=[test_project_A])
    # test_project_C = ffmake.VS2012Project(name="ProjectC", build_type="static_library")
    #
    #
    # test_solution = ffmake.VS2012Solution(name="TestSolution", projects=[test_project_A,
    #                                                                      test_project_B,
    #                                                                      test_project_C])
    # print test_solution.render()

    # User can provide UUID, which should enable easier roundtripping when generating
    # the Project files. UUID can be lower case, it will automatically be uppercased
    # if necessary by Jinja!
    project_A = ffmake.VisualStudioProject(name='Project_A',
                                           build_type=ffmake.STATIC_LIBRARY,
                                           uuid='0c3c77a5-66ab-43aa-8aa0-3eb99042b2e2')

    # TODO: Rendering environments like Jinja uses, to control where file output goes.
    print project_A.render()

    # project_B = ffmake.Project(name='Project_B', build_type=ffmake.STATIC_LIBRARY, dependencies=[ project_A ])

    # solution_A = ffmake.Solution(name="Solution_A", projects = [ project_A,
    #                                                              project_B ])

    # ffmake.render(targets=[ ffmake.VS_2013,
    #                         ffmake.XCODE_6_1 ])

    # wp = WindowsProject(name="ConsoleExe", build_type="windows_executable", source_dir="", source_files=[])
    # print wp.render()
    #
    # ws = WindowsSolution(name="MySolution", projects=[wp])
    # print ws.render()
