'''
Creating the test directory
To get started writing tests for your code, the first thing you need to do is create a test directory inside your package. Matching the structure of this directory to that of your source code directory makes it easier for users and automated tools to examine and run these tests.

Instructions
*Create a new directory in the top level of impyrial called tests. You can do this from the terminal using mkdir, or using the IDE menus.
*Add an empty test module inside tests for the impyrial/length/core.py module. Remember to use the naming convention described in the video.
*Inside the new test module, import the inches_to_feet() and the inches_to_yards() functions from impyrial/length/core.py using an absolute import.
'''

# mkdir tests (create the folder test)

# cd tests (enter the folder tests)

# mkdir length (create the folder length)

# cat > core.py (create the file core.py)

# rm core.py (remove the file core.py)

# cat > test_core.py

from impyrial.length.core import inches_to_feet, inches_to_yards

'''
Writing some basic tests
If you have written a full suite of tests for your code, it means you can develop and modify it more freely. If you make some changes that break your code, you'll be able to find this out right away. It also signals to users that your code is more likely to be error free, and can be trusted to do its job.

The tests you write will check that your functions give the expected outputs for given inputs. In this case you will be writing numeric tests to make sure that the correct answer is returned when converting a number of inches to feet and vice versa.

In this exercise, you'll write a test for one of your functions inside impyrial.

Instructions
*Define a function which takes no arguments to test the inches_to_feet() function.
*Inside the test function, check that 12 inches is converted to 1.0 feet.
*Check that 2.5 feet is converted to 30.0 inches when using option reverse=True in inches_to_feet().
'''
from impyrial.length.core import inches_to_feet, inches_to_yards

# Define tests for inches_to_feet function
def test_inches_to_feet():
	# Check that 12 inches is converted to 1.0 foot
    assert inches_to_feet(12) == 1.0
    # Check that 2.5 feet is converted to 30.0 inches
    assert inches_to_feet(2.5, reverse=True) == 30.0


'''
Running your tests
One of your collaborators has just made some changes to your code which has introduced an error. This can happen in the wild, but if you have written tests you will easily be able to find out where this error has come from.

In the exercise, you will use pytest to search for that error in your package and fix it.

Instructions
*Run pytest from the terminal to run all the package tests. You should see a test failure.
*Try to work out where the failure is coming from. (Remember that the error you corrected in Chapter 2 came from a wrong global variable.)
*Rerun pytest. All the tests should run successfully.
'''

# pytest

"""Conversions between inches and larger imperial length units"""
INCHES_PER_FOOT = 12.0  # 12.0 inches in a foot
INCHES_PER_YARD = INCHES_PER_FOOT * 3.0  # 3 feet in a yard

UNITS = ("in", "ft", "yd")


def inches_to_feet(x, reverse=False):
    """Convert lengths between inches and feet.
    Parameters
    ----------
    x : array_like
        Lengths in feet.
    reverse : bool, optional
        If this is set to true this function converts from feet to inches
        instead of the default behaviour of inches to feet.
    Returns
    -------
    ndarray
        An array of converted lengths with the same shape as `x`. If `x` is a
        0-d array, then a scalar is returned.
    """
    if reverse:
        return x * INCHES_PER_FOOT
    else:
        return x / INCHES_PER_FOOT


def inches_to_yards(x, reverse=False):
    """Convert lengths between inches and yards.
    Parameters
    ----------
    x : array_like
        Lengths in feet.
    reverse : bool, optional
        If this is set to true this function converts from yards to inches
        instead of the default behaviour of inches to yards.
    Returns
    -------
    ndarray
        An array of converted lengths with the same shape as `x`. If `x` is a
        0-d array, then a scalar is returned.
    """
    if reverse:
        return x * INCHES_PER_YARD
    else:
        return x / INCHES_PER_YARD

'''
Setting up tox
Before your next release, you are going to need to figure out which versions of Python your package will work with.

An easy way to find this out is to use tox to run all of your tests using different versions of Python.

It is also important to keep testing your package with these different Python versions as you develop it further.

Instructions
*Edit the tox.ini file to test Python versions 2.7 and 3.6.
*Add pytest as a dependency of the test environment.
*Edit the file so tox runs pytest.
'''

# tox.ini
"""
[tox]
envlist = py27,py36

[testenv]
deps = 
	pytest
commands =
	pytest
"""

'''
Running tox
Now it's time to directly test which versions of Python will function with your package. This is important information for your users so they can know whether or not they can actually install it.

Instructions
*Run tox from the terminal.
*In setup.py, update the required Python version based on the tox results. Remember to remove the #.
'''
# from the terminal, run the following command:
# tox

# setup.py >> update the following doc as per:

from setuptools import setup, find_packages

# Add install requirements
setup(
    author="<your-name>",
    description="A package for converting imperial lengths and weights.",
    name="impyrial",
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    version="0.1.0",
    install_requires=['numpy>=1.10', 'pandas'],
    python_requires="==3.6.*",
)

'''
Appropriate style filtering
You are coding a one-line equation in one file within your package. This file is called calculation.py. You'd like to add extra white spaces to make the equation easier to read, but this will cause flake8 to report an E222 violation. What is the most appropriate way to filter out this warning?

Answer:
Add # noqa : E222 to the line of the equation.
'''

'''
Using flake8 to tidy up a file
You have just written a module for calculating the absolute value of a given number. It's passing all your tests, but you are concerned that it does not conform to proper style guidelines. Sticking to style guidelines means your users, collaborators, and you, will be able to read and understand your code more easily.

As the Zen of Python states,

Readability counts.

In this exercise, you will use flake8 to point out style violations and fix them.

Instructions
*Using the terminal, run flake8 on the absolute.py module.
*Use the feedback from flake8 to bring the code into line with PEP8.

reference on the error codes: https://flake8.pycqa.org/en/latest/user/error-codes.html
'''
# flake8 absolute.py

"""Main module."""


def absolute_value(num):
    """Return the absolute value of the number"""
    if num >= 0:
        return num
    else:
        return -num


'''
Ignoring specific errors
Occasionally you may find that applying the PEP8 guidelines makes your code harder to read, or harder to use.

From the Zen of Python,

Special cases aren't special enough to break the rules.

Although practicality beats purity.

In these practical cases, you will make deliberate decisions to break the rules and filter out these flake8 violations.

Instructions
*Using the terminal, run flake8 on the pythagoras.py module.
*Identify the violation code caused by using the variable name l.
*Add a noqa comment to this line to filter out this message only.
*Run flake8 again.
'''
import numpy as np


def calculate_hypotenuse(side1, side2):
    """Calculate the length of the hypotenuse."""
    l = np.sqrt(side1 ** 2 + side2 ** 2)  # noqa: E741
    return l


'''
Configuring flake8
In the top-level __init__.py file, you imported the length and weight subpackages to expose them to users. However, these imports aren't used, so flake8 will keep notifying you about them.

You also might have some style violations in your tests directory, which you would like to ignore.

In this exercise, you will configure flake8 to ignore these violations.

Instructions
*Run flake8 on the whole package.
*Modify the config to ignore unused imports (F401) violations in the impyrial/__init__.py file. Make sure to uncomment the sample lines.
*Modify the config to ignore all violations in tests/*. Make sure to uncomment the sample lines.
*Run flake8 again to see the difference.
'''
# setup.cfg

"""
[flake8]

# Ignore F401 violations in the main __init__.py file
per-file-ignores =
    impyrial/__init__.py: F401

# Ignore all violations in the tests directoory
exclude = tests/*

"""