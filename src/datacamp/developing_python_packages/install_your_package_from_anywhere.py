
'''
Adding the setup script
The final step before you can install your package is to write the setup.py file.

In this exercise, you'll write this file, including all the metadata for your package.

P.S. If you look into the impyrial source code, you'll see a new subpackage has been added to convert weights.

Instructions
*Import the setup() and find_packages() functions from setuptools.
*Fill out the metadata, including your name. Give it the version number 0.1.0 and the description "A package for converting imperial lengths and weights."
*Use the find_packages() function to include the package and its subpackages.
'''
# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author="Thiago Siqueira",
    description="A package for converting imperial lengths and weights.",
    name="impyrial",
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    version="0.1.0",
)

'''
Installing your package locally
Great work on writing the setup script. Now its time to install your new package.

Instructions
*Using the terminal, install the package in editable mode using pip.
'''
# pip install -e .

import impyrial

result = impyrial.length.convert_unit(10, 'in', 'yd')
print(result)

'''
Utilizing editable installs
The great part about installing your package in editable mode is that you don't need to reinstall it when you make changes to it.

In this exercise, you have found a bug in the impyrial.weight subpackage. You should fix it and check that your installed version of the package reflects this change.

Instructions
*Run example_script.py to check what 2 lb (2 pounds weight) is in ounces. The real answer should be 32.
*Fix the bug in the impyrial/weight/core.py file. The OUNCES_PER_POUND variable should be 16.0.
*Run the example script again to ensure that your bug is fixed.
'''
import impyrial

result = impyrial.weight.convert_unit(2, 'lb', 'oz')
print(result)

'''
User dependencies
Inside any package you develop, you will probably use other packages. This stops you having to rewrite code which has already been optimized for speed and ease of use, like NumPy.

The users of your package will need to have these other packages installed, and have one of the correct versions. If they don't, then your package won't actually work.

In this exercise, you will modify the setup.py file so that these packages are installed when your package is installed using pip.

Instructions
*Add numpy version 1.10 or above as a dependency.
*Add any version of pandas as a dependency.
'''
from setuptools import setup, find_packages

# Add install requirements
setup(
    author="<your-name>",
    description="A package for converting imperial lengths and weights.",
    name="impyrial",
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    version="0.1.0",
    install_requires=[
        'numpy>=1.10',
        'pandas'
    ],
)

'''
Development dependencies
You need to include a requirements file which includes all of the versions of packages used during development. This means any bugs can be reproduced, and ensures you and anyone else working on your package have the exact same versions of other packages.

This is different to the install_requires parameter which tries to allow as many dependency versions as possible. The install_requires is for users and the requirements.txt is for developers.

Instructions
*Use pip to save the packages installed into a file called requirements.txt in the top level of impyrial.
'''
# pip freeze > requirements.txt

'''
Writing a README
Its time to write the front page of your impyrial package. This is the page your users will see when they find your package on GitHub or PyPI.

This is the impression your package will make on people, so you should try to make it look good! Including a brief description, the package features, and some examples of usage is a good place to start.

Instructions
*Add a title at the top of the file for impyrial.
*In the second sentence of the description, turn the word "DataCamp" into a link to https://www.datacamp.com.
*Add backticks so that the usage example will display as code.
'''

# README.md

'''
# impyrial

A package for converting between imperial unit lengths and weights.

This package was created for the [DataCamp](https://www.datacamp.com) course "Developing Python Packages".

### Features

- Convert lengths between miles, yards, feet and inches.
- Convert weights between hundredweight, stone, pounds and ounces.

### Usage

```
import impyrial

# Convert 500 miles to feet
impyrial.length.convert_unit(500, from_unit='yd', to_unit='ft')  # returns 1500.0

# Convert 100 ounces to pounds
impyrial.weight.convert_unit(100, from_unit='oz', to_unit='lb')  # returns 6.25
```

'''

'''
MANIFEST - Including extra files with your package
The MANIFEST.in file lists all the extra files (those other than your package source code) which should be included when your package is sent out. This is really important so that your license is always included with your software.

In this exercise, you'll write your MANIFEST.in file for impyrial.

P.S. We have added a license to your directory which is the MIT License. This is a common and very open license which allows anyone to use this package in any way they like.

Instructions
*Create a MANIFEST.in file in the topmost package directory.
*Add the README.md and LICENSE files to MANIFEST.in so they are included with your source code.
'''

# MANIFEST.in

'''
include LICENSE
include README.md
'''

'''
Building a distribution
It's time to get your package out there! It's not a finished product yet, and when building packages, you always find there is so much more you'd like to add or change. But this package has been developed enough that it could be useful to someone, and the sooner you release it, the sooner you can get feedback or find collaborators!

In this exercise, you will build the two types of distributions, wheel and source distributions, for your impyrial package. The only thing left after this step will be to upload it.

Instructions
*In the terminal, run setup.py with the appropriate arguments to build source and wheel distributions.
'''

# python setup.py sdist bdist_wheel

'''
Uploading distributions
Your distributions are ready to go, the only step is to upload them now so that anyone can access them.

Normally, you would need to register for an account on PyPI to be able to upload a package. In this exercise, you will be using the exact commands you normally would, but your distribution won't actually be uploaded.

Instructions
*Use twine to upload your distributions.
'''
# twine upload dist/*