'''
 the setup.py file is an essential part of packaging and distributing
 python projects . It is used by setuptools to define the metadata and dependencies of the project, as well as to specify how the project should be built and installed.it defines configurations such as metadata, dependencies, entry points, and other settings that are necessary for building and distributing the project. The setup.py file is typically located in the root directory of the project and is executed using the python setup.py command.
 '''

# it will scan all the packages and sub-packages under the current directory and include them in the distribution package if __init__.py file is present in the directory. It will also include any data files specified in the package_data argument of the setup() function.

from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """
    This function will return the list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open("requirements.txt") as file:
            # Read lines from file
            lines = file.readlines()
            # Process each line
            for line in lines:
                # Strip whitespace and ignore comments
                requirement = line.strip()
                # ignore empty lines and comments
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

print(get_requirements())

# in order to setup our metadata and dependencies for our project, we will use the setup() function from setuptools. The setup() function takes various arguments that define the metadata and dependencies of the project. Here is an example of how to use the setup() function in a setup.py file:


setup(
    name="Network_Security",
    version="0.0.1",
    author="Nidhan",
    author_email="nidhanjain1406@gmail.com",
    description="A package for Network Security",
    packages=find_packages(),
    install_requires=get_requirements(),
)
