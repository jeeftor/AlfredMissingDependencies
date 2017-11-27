#!/usr/bin/python

import os
import sys

import pip
import pkg_resources



class RequirementsInstaller(object):
    """This class will look for a `requirements.txt` file in the local directory.  If found it will call
    pip internally to try to install (locally) the missing requirements.  This may allow alfred distribution
    to go faster for soem python libs and stuff,  My default it will install stuff in the ./lib directory - but you
    can program things to go elsewhere"""

    def __init__(self, install_dir='./lib'):
        super(RequirementsInstaller, self).__init__()

        self.lib_path = os.path.abspath(os.getcwd() + '/' + install_dir)
        self.prefix_option = '--prefix=' + self.lib_path
        self.target_option = '--target=' + self.lib_path
        self.create_setup_cfg()
        self.output_json = ""

    def create_setup_cfg(self):
        """When using homebrew and stuff there are issues wiht pip --target installs unless this file exists
        in the home directory of the project"""
        with open('setup.cfg', "w") as w:
            w.write('[install]\nprefix=\n')

    def install_requirements(self):
        """Will attempt to parse a `requirements.txt` file and check for which dependencies are missing"""
        # Read in requiremetns.txt file
        with open('requirements.txt') as f:
            dependencies = f.read().splitlines()

        # Process each dependency in turn
        for dependency in dependencies:

            try:
                pkg_resources.require(dependency)

            except:
                print('Missing: ' + dependency)
                print('\tInstalling to: ' + self.lib_path)
                self.install_requirement(dependency)

    def install_requirement(self, requirement):
        """Instals a requirement with the self.prefix_option as specified by the class"""
        pip.main(['install', self.target_option, requirement])

    def build_alfred_output(self):

        requirements = []

        # Read in requiremetns.txt file
        with open(os.path.dirname(__file__) + '/requirements.txt') as f:
            dependencies = f.read().splitlines()

        # Process each dependency in turn
        for dependency in dependencies:
            req, version = dependency.split('==')
            try:
                pkg_resources.require(dependency)
                requirements.append(
                    '{"valid": false,"subtitle": "(ALREADY INSTALLED) Version %s","title": "%s"}' % (version, req))
            except:
                requirements.append(
                    '{"valid": false,"subtitle": "Version %s","title": "%s"}' % (version, req))
        return """
{
    "items": [
        {
            "arg": "%s",
            "valid": true,
            "subtitle": "The plugin will attempt an install the following dependencies:",
            "icon": {
                "path": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertCautionIcon.icns"
            },
            "title": "Setup Plugin Dependencies"
        },%s
    ]
}
""" % (os.path.dirname(__file__),','.join(requirements))

def main(argv):
    # my code here
    installer = RequirementsInstaller()
    try:
        if argv[1] == 'install':
            installer.install_requirements()
    except IndexError:
        pass

if __name__ == "__main__":
    main(sys.argv)
