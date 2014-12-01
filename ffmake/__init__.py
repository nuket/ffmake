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

from .ffmake import Project, Solution, VisualStudioProject, VS2012Solution

__version__ = '0.2' # Also change in setup.py.
# __all__     = ['Project', 'Solution', 'VisualStudioProject', 'VS2012Solution']

# Constants

STATIC_LIBRARY = 'static_library'
SHARED_LIBRARY = 'shared_library'
EXECUTABLE     = 'executable'

VS_2012 = 'VS2012'
VS_2013 = 'VS2013'
VS_2015 = 'VS2015'

XCODE_6_1 = 'XCODE61'