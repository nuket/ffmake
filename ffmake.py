"""
Copyright (c) 2012 Max Vilimpoc

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

import argparse
import pystache
import uuid

# Helper Functions

def create_uuid():
    return str(uuid.uuid4()).upper()

# Classes
    
class Project(object):
    """
    Pulls and holds onto some of the most basic/common tags.
    
    Tags this class automatically gobbles up:
    
    name: (Required)  
           Every Project, every Solution file has a name of some kind.
           It probably needs to be unique, but we're not going to check.
           No name == ValueError.

    guid: (Optional)
           Unique identifier for the Project / Solution.
           
    Items in args and kwargs and .popped, meaning the caller loses
    them.
    """
    def __init__(self, *args, **kwargs):
        # Contains information to be rendered to the project template.
        self.tags = {}
        
        # Superclass plugs the kwargs it recognizes into the tags
        # dict. Required parameters are pulled here.
        try:
            self.tags['name'] = kwargs.pop('name')
        except KeyError as e:
            print "Required parameter was not provided: " + str(e)
            raise e

        # Optional parameters are here.
        self.tags['guid'] = kwargs.pop('guid', create_uuid())
        
        """
        self.output         = output

        

        self.dependencies   = dependencies
        """
        
    def render(self):
        self.renderer = pystache.Renderer(search_dirs=self.template_dirs)
        return self.renderer.render_name(self.template, self.tags)

class WindowsProject(Project):
    # 'executable' == 'console_executable' by default (it's an alias)
    BUILD_TYPES = ['static_library', 'shared_library', 'executable', 'windows_executable', 'console_executable']
    
    BUILD_TYPE_MAPPING = {
        'static_library': {
            'windows_configuration_type': 'StaticLibrary',
            'windows_link_subsystem':     'Windows',
            'windows_incremental_link':   False,
            'preprocessor_defs':          ['_LIB']
        },
        'shared_library': {
            'windows_configuration_type': 'DynamicLibrary',
            'windows_link_subsystem':     'Windows',
            'windows_incremental_link':   True,
            'preprocessor_defs':          ["_WINDOWS", "_USRDLL"]
        },
        'executable': {
            'windows_configuration_type': 'Application',
            'windows_link_subsystem':     'Console',
            'windows_incremental_link':   True,
            'preprocessor_defs':          ["_CONSOLE"]
        },
        'windows_executable': {
            'windows_configuration_type': 'Application',
            'windows_link_subsystem':     'Windows',
            'windows_incremental_link':   True,
            'preprocessor_defs':          ["_WINDOWS"]
        },
        'console_executable': {
            'windows_configuration_type': 'Application',
            'windows_link_subsystem':     'Console',
            'windows_incremental_link':   True,
            'preprocessor_defs':          ["_CONSOLE"]
        }
    }

    def __init__(self, *args, **kwargs):
        # Call superclass (note: side effect, args and kwargs are modified)
        super(WindowsProject, self).__init__(*args, **kwargs)
        
        # Convert some of the basic params to the Windows-specific
        # Mustache tags.
        self.tags['windows_project_guid']   = self.tags['guid']
        self.tags['windows_root_namespace'] = self.tags['name']

        # Figure out what kind of project this is.
        try:
            build_type = kwargs.pop('build_type')
        except KeyError as e:
            print "Required parameter was not provided: " + str(e)
            raise e

        if build_type not in WindowsProject.BUILD_TYPES:
            raise ValueError("build_type must be one of: " + ', '.join(WindowsProject.BUILD_TYPES))
        
        # Pull in the default config values and apply them to the tags.
        self.tags.update(WindowsProject.BUILD_TYPE_MAPPING[build_type])
        
        # Start attaching parameters to the tags variable.
        # for k, v in kwargs.iteritems():
        #    print k
        #    print v

        # Set up template info.
        self.template_dirs  = kwargs.pop('template_dirs', ['templates/windows', 'templates/windows/partials'])
        self.template       = kwargs.pop('template',       'VS2012eProject')
        
        # Template dirs need to be specified in relation to where ffmake.py is located,
        # NOT where ffmakefile.py is being called (current working dir).
        
        # TODO: Get User's TMPDIR and use that for all intermediate compilation.
        self.working_dir    = kwargs.pop('working_dir',  '')
        
        # Need to set a sensible Program Database (.pdb) filename.
        
        # Need to set intermediate compilation dirnames based on VS macros $(Configuration) and $(Platform)
        
        # Start layering on additional settings.
        
        self.include_dirs  = kwargs.pop('include_dirs', [])
        self.include_files = kwargs.pop('include_files', [])
        
        self.lib_dirs      = kwargs.pop('lib_dirs', [])
        self.lib_files     = kwargs.pop('lib_names', [])
        
        self.source_files  = kwargs.pop('source_files', [])
        """
        self.include_dirs   = include_dirs
        self.include_files  = include_files   # full filenames (with .h)
        self.lib_dirs       = lib_dirs
        self.lib_files      = lib_names       # basename only, we stick .a or .lib on them.
        self.source_files   = source_files    # full filenames (with .cc or .cpp) with relative path?
        self.working_dir    = working_dir
        """
        # Check that the variables are the correct types.
        # if list != type(self.template_dirs):
        
        # Convert those variables we need as lists, to be lists of filename dicts { 'filename': 'X' }

class WindowsSolution:
    def __init__(self):
        pass

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

# Generate the solution, project files in the current working directory
# with all paths relative to that directory.

if __name__ == "__main__":
    wp = WindowsProject(name="ConsoleExe", build_type="windows_executable")
    print wp.render()
