# Python Dependency Installation (example)

This workflow is a proof of concept showing how you could setup a workflow to install its own dependencies.

The structure of this plugin is as follows:

All python files are stored in the `src` directory while all libraries exist (_or will exist_) in `src/lib`


The way to implement a similar workflow in your own code is as follows:


At the top of any script you want to run add the following lines

```python
# Add the lib path into the library search path
lib_path = os.path.dirname(__file__) + '/lib'
sys.path.append(lib_path)
```
This will tell Pythyon to also look in `src/lib` for any packages you try to import.

Next you want to import the `missing` class from `RequirementsInstaller` which is in `RequirementsInstaller.py` which resides in the `src` directory.  

Once this is done you can try to import all the required libs - if one throws an exception it will jump into a block which will prompt the user for installing the packages

```python

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
```

# Requirements.txt

The actual list of what packages to install is determined based on the `src/requirements.txt` file - so you need to make sure that anything you are trying to import is also specified in this file