'''
Using package templates
Using project templates, like cookiecutter, makes it much faster and easier to begin writing a package. These templates create all of the basic files and structure your package needs.

In this exercise, you will use cookiecutter to create a new package as if you were restarting impyrial from scratch.

Instructions
*Use cookiecutter to create a blank Python package to restart impyrial. Use the template at https://github.com/audreyfeldroy/cookiecutter-pypackage.git.
*Set the project_name and project_slug to impyrial.
*Fill in the other options however you'd like.
'''

#  cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git

'''
CONTRIBUTING.md
What is the purpose of the CONTRIBUTING.md file?

Answer:
To tell potential users and developers how they can get involved with your project.
'''

'''
History file
We have added all your work from the previous chapters into the empty cookiecutter package you just created.

Since you last made a release of the package, you have written some pytest tests, fixed a bug, changed the supported versions of Python, re-styled some of the code using flake8, and added a few new additional files.

Now it is time for a new minor version release, so you need to update your package's HISTORY.md file.

Instructions
*Add a subtitle above the 0.1.0 section for a new minor version release.
*Add a "Fixed" section for the new release, similar to the "Added" section for 0.1.0.
*Add a bullet point to tell the users that "Bug fixed in `length` subpackage for inches-to-feet conversion."
*Add a "Deprecated" section and add the bullet point "Removed Python 2.7 support.
'''

#HISTORY.md
"""
# History

## 0.1.0
### Fixed
- Bug fixed in `length` subpackage for inches-to-feet conversion.
### Deprecated
- Removed Python 2.7 support.

## 0.2.0
### Added
- First release on PyPI.
"""

'''
Tracking version number with bumpversion
When making a new release you need to increase the version number. You will change the patch, minor or major version number, depending on how much you have changed in the package.

This time you have implemented a bug fix, changed the code style, changed the supported Python versions and written tests. If it weren't for the change to the supported Python version, this would probably only be a patch, as the only thing a user would notice is the bug fix. But because of this more serious change, it will instead be a minor version update.

Instructions
*In the terminal, use bumpversion once to increase the minor version number by one.
'''
# bumpversion minor

'''
PyPI classifiers
Classifiers help your users discover your code on PyPI, and it is best practice to include them. They also add a more professional feel to your package.

The classifiers in this setup.py file are those which cookiecutter picked, but they don't line up with the versions of Python that your package supports.

Instructions
*Remove some of the classifiers so that only the versions of Python that your package supports are included.
'''
# check the versions on the file: tox.ini

# go to setup.py and update accordingly, as per the following script:

'''

#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

setup(
    author="All credit to you",
    author_email='you@chapter4.com',
    description="A package for converting between imperial unit lengths and weights.",
    name='impyrial',
    packages=find_packages(include=['impyrial', 'impyrial.*']),
    version='0.1.0',
    install_requires=['numpy>=1.10', 'pandas'],
    python_requires="==3.6.*",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    keywords='impyrial',    
    zip_safe=False,
)

'''

'''
Using makefiles
You have added some new features to your package and it is time to make a new release. To speed up this process, you will use the commands in the Makefile, saving you time and helping you to avoid missing important steps.

Remember, the Makefile bundles up commands used to modify your package, just like a Python function bundles up several lines of code.

Instructions
*Use make to remove the old distributions.
*Use make to run the package tests.
*Use make to build new source and wheel distributions.
'''
# make clean
# make test
# make dist