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

import os
import uuid

from jinja2 import Environment, PackageLoader

# ----------------------------------------------------------
# Constants
# ----------------------------------------------------------

# You know, for development purposes. Set to 0 when 
# releasing.

DEBUG = 1

# Need to know where the ffmake module is located, and where the 
# templates are in relation to that.

MODULE_DIR = os.path.dirname(__file__) + os.sep

# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------

def create_windows_guid():
    return '{' + str(uuid.uuid4()).upper() + '}'

def fix_separators(paths):
    """
    Make sure that the input string or list of strings is using 
    the correct directory separator character.

    So, always replace the \ or / symbols with the correct symbol.
    """
    if   str  == type(paths):
        paths = paths.replace('\\', os.sep)
        paths = paths.replace('/',  os.sep)
    elif list == type(paths):
        paths = [P.replace('\\', os.sep) for P in paths]
        paths = [P.replace('/',  os.sep) for P in paths]

    return paths

def prefix_string_list_entries(prefix, string_list):
    return ['{0}{1}'.format(prefix, S) for S in string_list]

def prepare_list_entries(tag="", prefix="", string_list=[], suffix=""):
    """
    Used to create lists of objects ready for rendering with
    Mustache sections.

    Examples:
    [ {'filename': '../source_dir/A.cpp'}, ... ]
    [ {'dirname':  '..\..\includes'},   ... ]
    """
    return [{'{0}'.format(tag): '{0}{1}{2}'.format(prefix, S, suffix)} for S in string_list]

def prefix_files(prefix="", filename_list=[]):
    # Only use the prefix if one is provided. 
    # Check the prefix. It needs to have os.sep at its end.
    if prefix:
        prefix = prefix.strip()
        prefix = fix_separators(prefix)
        
        if not prefix.endswith('\\') or not prefix.endswith('/'):
            prefix = prefix + os.sep

    return prepare_list_entries(tag="filename", prefix=prefix, string_list=filename_list)

# ----------------------------------------------------------
# Error Explanations
# ----------------------------------------------------------

def exception_explain_required_tag(class_name="", tag=""):
    print
    print "ffmake: Required tag was not provided to the {0} constructor: {1}".format(class_name, tag)
    print "ffmake: Check your {0} instantiation, and make sure it has {1}='SomeValue' in it.".format(class_name, tag.replace("'", ""))
    print

def exception_explain_build_types(build_types=[]):
    print
    print "ffmake: build_type must be one of: "
    print "ffmake: " + ', '.join(build_types)
    print

# ----------------------------------------------------------
# Mixin
# ----------------------------------------------------------

def render_mixin(self, filename=''):
    """
    Any class that needs to render a template uses this mixin.
    
    The 'self' class instance needs to have the following variables
    set:

    :env:            The Jinja environment to use to render templates.
    :template_dirs:  Tells Mustache where to find templates and partials.
    :tags:           The tags Mustache uses when rendering.

    Optional parameters:

    :filename:       The file to render to.

    :return:         The rendered output, regardless of what :filename:
                     is set to.
    """
    # Fill out the correct path to the templates.
    # template_dirs = prefix_string_list_entries(MODULE_DIR, self.template_dirs)

    # Create a Renderer that will find the templates and partials.
    # self.renderer = pystache.Renderer(search_dirs=template_dirs)

    # Render to string.
    output = self.template.render(self.tags)

    if filename:
        # Open the file and dump info there.
        pass

    return output

# ----------------------------------------------------------
# Classes
# ----------------------------------------------------------

class Project(object):
    """
    Pulls and holds onto some of the most basic/common tags.
    
    Tags this class automatically gobbles up:
    
    :name: (Required)  
            Every Project, every Solution file has a name of some kind.
            It probably needs to be unique, but we're not going to check.
            No name == ValueError.

            :name: is used to generate the :project_name: and :project_file:
            tags.

    :uuid: (Optional)
            Unique identifier for the Project / Solution.
           
    Items in args and kwargs and .popped, meaning the caller loses
    them.
    """
    
    BUILD_TYPE_STATIC_LIBRARY = 'static_library'
    BUILD_TYPE_SHARED_LIBRARY = 'shared_library'
    BUILD_TYPE_EXECUTABLE     = 'executable'

    # Base class allowable build types.
    BUILD_TYPES = [BUILD_TYPE_STATIC_LIBRARY, BUILD_TYPE_SHARED_LIBRARY, BUILD_TYPE_EXECUTABLE]

    # Base class checks for certain required tags.
    REQUIRED_TAGS = ['name', 'build_type']

    # Tags that are dirname or filename lists, that need to be
    # run through the source_dir prefixer.
    FILENAMES_NEEDING_SOURCE_DIR = ['text_files', 
                                    'source_files',
                                    'unmanaged_source_files',
                                    'resource_files',
                                    'image_files']

    # Tags that are dirname lists, that need to have the paths
    # fixed.
    PATHS_NEEDING_FIX = ['include_dirs',
                         'include_dirs_shared',
                         'include_dirs_static',
                         'include_dirs_debug',
                         'include_dirs_release',
                         'include_dirs_32bit',
                         'include_dirs_64bit',
                         'lib_dirs',
                         'lib_dirs_shared',
                         'lib_dirs_static',
                         'lib_dirs_debug',
                         'lib_dirs_release',
                         'lib_dirs_32bit',
                         'lib_dirs_64bit']

    PREPROCESSOR_DEFS_NEEDING_FIX = ['preprocessor_defs',
                                     'preprocessor_defs_shared',
                                     'preprocessor_defs_static',
                                     'preprocessor_defs_executable',
                                     'preprocessor_defs_debug',
                                     'preprocessor_defs_release',
                                     'preprocessor_defs_32bit',
                                     'preprocessor_defs_64bit',
                                     'preprocessor_defs_build_type',
                                     'preprocessor_defs_project']

    def __init__(self, *args, **kwargs):
        # Contains information to be rendered to the project template.
        # This is used by all derived classes.
        self.tags = {}

        # Pull all kwargs into tags object.
        # Deeply processing these tags happens in derived classes.
        self.tags.update(kwargs)

        # Required parameters are checked here.
        try:
            for T in Project.REQUIRED_TAGS:
                self.tags[T]
        except KeyError as e:
            exception_explain_required_tag(self.__class__.__name__, str(e))
            raise e

        # Later derived-class __init__ methods will want to know:
        # which of the preprocessor_defs_{shared, static, executable}
        # flags to use.

        if   self.tags['build_type'] == Project.BUILD_TYPE_STATIC_LIBRARY:
             self.tags['preprocessor_defs_build_type'] = kwargs.pop('preprocessor_defs_static', [])
        elif self.tags['build_type'] == Project.BUILD_TYPE_SHARED_LIBRARY:
             self.tags['preprocessor_defs_build_type'] = kwargs.pop('preprocessor_defs_shared', [])
        elif self.tags['build_type'] == Project.BUILD_TYPE_EXECUTABLE:
             self.tags['preprocessor_defs_build_type'] = kwargs.pop('preprocessor_defs_executable', [])

        # if DEBUG: locals()
    

    # Mixin the rendering capability.
    render_mixin = render_mixin


    def render(self, filename=''):
        """
        Renders the Project file template. 

        :filename:  A fully-qualified filename including path. 

        :returns:   The rendered template string.
        """

        # Process the tags that need some fixing.

        # Process all of the file lists, prefixing them with source_dir.
        source_dir = self.tags.get('source_dir', '')

        # In other words: if text_files=['A.txt', 'B.txt'] then after
        # after this loop:   text_files=['source_dir/A.txt', 'source_dir/B.txt']   (Unix)
        # or:                text_files=['source_dir\\A.txt', 'source_dir\\B.txt'] (Windows)
        for T in Project.FILENAMES_NEEDING_SOURCE_DIR:
            if T in self.tags:
                self.tags[T] = prefix_files(prefix=source_dir, filename_list=self.tags[T])

        for T in Project.PATHS_NEEDING_FIX:
            if T in self.tags:
                self.tags[T] = prepare_list_entries(tag='dirname', string_list=fix_separators(self.tags[T]))

        # Prepare for Mustache.
        # After this loop: preprocessor_defs=['DEFINE_A', 'DEFINE_B']
        # Becomes:         preprocessor_defs=[{'define': 'DEFINE_A'}, {'define': 'DEFINE_B'}]

        for D in Project.PREPROCESSOR_DEFS_NEEDING_FIX:
            if D in self.tags:
                self.tags[D] = prepare_list_entries(tag='define', string_list=self.tags[D])

        output = self.render_mixin(filename)

        return output

class VisualStudioProject(Project):
    # Windows makes a distinction between Windows subsystem executables and
    # Console subsystem executables, so we have to slightly extend the list
    # of allowable build types.
    #
    # 'executable' == 'console_executable' by default (it's an alias)
    BUILD_TYPE_WINDOWS_EXECUTABLE = 'windows_executable'
    BUILD_TYPE_CONSOLE_EXECUTABLE = 'console_executable'

    BUILD_TYPES = list(Project.BUILD_TYPES)
    BUILD_TYPES.extend([BUILD_TYPE_WINDOWS_EXECUTABLE, 
                        BUILD_TYPE_CONSOLE_EXECUTABLE])

    # ['static_library', 'shared_library', 'executable', 'windows_executable', 'console_executable']
    
    BUILD_TYPE_MAPPING = {
        'static_library': {
            'windows_configuration_type': 'StaticLibrary',
            'windows_link_subsystem':     'Windows',
            'windows_incremental_link':   False,
            'preprocessor_defs_project':  ['_LIB']
        },
        'shared_library': {
            'windows_configuration_type': 'DynamicLibrary',
            'windows_link_subsystem':     'Windows',
            'windows_incremental_link':   True,
            'preprocessor_defs_project':  ["_WINDOWS", "_USRDLL"]
        },
        'windows_executable': {
            'windows_configuration_type': 'Application',
            'windows_link_subsystem':     'Windows',
            'windows_incremental_link':   True,
            'preprocessor_defs_project':  ["_WINDOWS"]
        },
        'console_executable': {
            'windows_configuration_type': 'Application',
            'windows_link_subsystem':     'Console',
            'windows_incremental_link':   True,
            'preprocessor_defs_project':  ["_CONSOLE"]
        }
    }

    def __init__(self, *args, **kwargs):
        # Call superclass (note: side effect, args and kwargs are modified)
        super(VisualStudioProject, self).__init__(*args, **kwargs)

        # Instantiate the default Jinja environment:
        #     make sure line endings are CRLF (which they aren't by default)
        #     make sure trailing newlines are kept
        #
        # See: http://jinja.pocoo.org/docs/dev/api/
        self.env = Environment(loader=PackageLoader('ffmake', 'templates/windows'), newline_sequence='\r\n', keep_trailing_newline=True)

        # Instantiate the default Jinja template.
        self.template = self.env.get_template('Project.vcxproj.jinja')
        
        # Convert some of the basic params to the Windows-specific
        # Mustache tags.
        self.tags['project_guid']           = self.tags.pop('uuid', create_windows_guid())
        self.tags['project_name']           = self.tags['name']
        self.tags['project_file']           = self.tags['name'] + '.vcxproj' # TODO: Add _static, _shared, _executable to the project name; convention over configuration.

        self.tags['windows_project_guid']   = self.tags['project_guid']
        self.tags['windows_root_namespace'] = self.tags.pop('name')

        # Figure out what kind of project this is.
        try:
            build_type = kwargs.pop('build_type')
            
            # Map 'executable' type to 'console_executable'
            if build_type == Project.BUILD_TYPE_EXECUTABLE:
                build_type = self.BUILD_TYPE_CONSOLE_EXECUTABLE
            
        except KeyError as e:
            exception_explain_required_tag(self.__class__.__name__, str(e))
            raise e

        if build_type not in self.BUILD_TYPES:
            exception_explain_build_types(self.BUILD_TYPES)
            raise ValueError()
        
        # Pull in the default config values and apply them to the tags.
        self.tags.update(self.BUILD_TYPE_MAPPING[build_type])
        
        # Start attaching parameters to the tags variable.
        # for k, v in kwargs.iteritems():
        #    print k
        #    print v

        # Set up template info.
        # self.template_dirs  = kwargs.pop('template_dirs', ['templates/windows', 'templates/windows/partials'])
        # self.template       = kwargs.pop('template',       'VS2012Project')
        
        # Template dirs need to be specified in relation to where ffmake.py is located,
        # NOT where ffmakefile.py is being called (current working dir).
        
        # TODO: Get User's TMPDIR and use that for all intermediate compilation.
        self.working_dir    = kwargs.pop('working_dir',  '')
        
        # Need to set a sensible Program Database (.pdb) filename.
        
        # Need to set intermediate compilation dirnames based on VS macros $(Configuration) and $(Platform)
        
        # Start layering on additional settings.
        
        # self.tags['lib_dirs']  = prepare_dirname_list_entries(dirname_list=kwargs.pop('lib_dirs', []))
        # self.tags['lib_files'] = prepare_filename_list_entries(filename_list=kwargs.pop('lib_files', []))

        # Convert those variables we need as lists, to be lists of filename dicts { 'filename': 'X' }

    def flatten(self):
        # Controlling whether 'dependencies' sections get rendered at all.
        self.tags['dependencies_count'] = len(self.tags.get('dependencies', []))

        # Recursively flatten projects, so it's just a bunch of nested tags.
        self.tags['dependencies'] = [P.flatten() for P in self.tags.get('dependencies', [])]

        return self.tags

class Solution():
    pass

class VS2012Solution(object):
    def __init__(self, *args, **kwargs):
        self.tags = {}

        # One and only one of these. Required.
        self.tags['solution_name'] = kwargs.get('name')

        # One and only one of these.
        self.tags['solution_guid'] = create_windows_guid()

        # There's a list of projects here.
        self.tags['projects'] = kwargs.get('projects', [])

        # Set up template info.
        self.template_dirs  = kwargs.pop('template_dirs', ['templates/windows', 'templates/windows/partials_VS2012Solution'])
        self.template       = kwargs.pop('template',       'VS2012Solution')


    def add_project(self, project=None):
        pass


    # Mixin the rendering capability.
    render_mixin = render_mixin

    def render(self, filename=''):
        # Controlling whether 'projects' sections get rendered at all.
        self.tags['projects_count'] = len(self.tags.get('projects', []))

        # Flatten the projects, by just using tags.
        self.tags['projects'] = [P.flatten() for P in self.tags.get('projects', [])]

        # print self.tags['projects']

        output = self.render_mixin(filename)
        
        return output


class ProjectFactory:
    """
    Creates Project-derived objects and returns these to caller.
    """
    def __init__(self, name="", build_types=[], *args, **kwargs):
        pass

    def render(self):
        pass
