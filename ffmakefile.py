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
# import ffmake.recipes.zlib

# zlib = 

test_project_A = ffmake.VS2012Project(name="ProjectA", build_type="static_library")
test_project_B = ffmake.VS2012Project(name="ProjectB", build_type="static_library", dependencies=[test_project_A])
test_project_C = ffmake.VS2012Project(name="ProjectC", build_type="static_library")


test_solution = ffmake.VS2012Solution(name="TestSolution", projects=[test_project_A,
                                                                     test_project_B,
                                                                     test_project_C])
print test_solution.render()


#test_project  = ffmake.project_factory(name='',
#                                       ide_type='',
#                                       dependencies=[])

# test_solution = WindowsSolution(name='TestSolution',
#                                projects=[test_project])

# 
# test_solution.render(to_dir='')

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
