#!/usr/bin/python
import os, sys

# Add the lib path into the library search path
lib_path = os.path.dirname(__file__) + '/lib'
sys.path.append(lib_path)


from missing import RequirementsInstaller

try:
    # Add the required dependencies into a try block
    from workflow import Workflow3
    import pycountry
    import dotmap
except:
    # If we cant get any dependencies - lets exit and add the install prompt
    print RequirementsInstaller().build_alfred_output()
    exit(2)


print  """
{
    "items": [
        {
            "arg": "install",
            "valid": false,
            "subtitle": "All dependencies correctly installed",
            "icon": {
                "path": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertCautionIcon.icns"
            },
            "title": "Good 2 Go!!!"
        },
        {
            "arg": "uninstall",
            "valid": true,
            "subtitle": "Delete install dependencies",
            "icon": {
                "path": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/BurningIcon.icns"
            },
            "title": "Reset Plugin"
        }
    ]
}
"""


