'''
Modules, packages and subpackages
When developing packages, it will be important to know your terminology.

Can you name the different parts of this package directory tree?

    directory1/
    |-- __init__.py
    |-- directory2
    |   |-- __init__.py
    |   `-- file1.py
    `-- file2.py

Note that file1.py and file2.py contain general functions which are intended to be imported.

Instructions
*Assign each file or directory to the right label.
'''

'''
From script to package
One common way to begin writing a package is to start with code you have already written as a script. At the time you first write this code, you may not realize how useful it might be in other places.

If you did the prerequisite course, in one exercise you wrote a script to count the number of times cats were mentioned in the book Alice in Wonderland.

In this exercise, you'll copy from that script to make a generalized function you can use on any text file for any words. This will be the first function in a new library.

Instructions
*Create a new directory called textanalysis for your package. Click File > New Folder in the IDE.
*Create __init__.py and textanalysis.py modules inside textanalysis. Click the new textanalysis folder, then click File > New File in the IDE to create new files inside it.
*Copy the code from myscript.py into textanalysis.py.
*Modify textanalysis.py to create the function count_words(filepath, words_list) which opens the text file filepath, and returns the number of times the words in words_list appear.
'''


def count_words(filepath, words_list):
    # Open the text file
    with open(filepath) as file:
        text = file.read()

    n = 0
    for word in text.split():
        # Count the number of times the words in the list appear
        if word.lower() in words_list:
            n += 1

    print('Lewis Carroll uses the word "cat" {} times'.format(n))

    return n


'''
Putting your package to work
Now you have wrapped your word-counting function into a package, you can reuse it easily in other projects.

In the initial script, you were analyzing the book Alice in Wonderland. In this new project, you will use the same function to analyze hotel reviews from TripAdvisor.

The count_words() function has been imported for you at the top of this script. We'll talk more about importing from your packages in a later lesson.

Instructions
*Use your new package to count the number of times the positive words 'good' or 'great' appear in the file 'hotel-reviews.txt'.
*Use the package to count the number of times the negative words 'bad' or 'awful' appear.
'''
from textanalysis.textanalysis import count_words

# Count the number of positive words
# count_words(filepath, words_list)
nb_positive_words = count_words('hotel-reviews.txt', ['good', 'great'])

# Count the number of negative words
nb_negative_words = count_words('hotel-reviews.txt', ['bad', 'awful'])

print("{} positive words.".format(nb_positive_words))
print("{} negative words.".format(nb_negative_words))

'''
Documentation

help(functionName) >> eg. help(scipy.percentile)

pyment >> tool to create documentation as per one of the standards (Google, NumPy, reStrucured and Epytext). eg.  "pyment -w -o numpydoc testanalysis.py" 

where 
"-w" >> - overwrite file
"-o numpydoc" >> output in NumPy style
suppose you want to change the documentation style to the google style: "pyment -w -o google testanalysis.py"
'''

'''
Writing function documentation with pyment
Using documentation templates helps you stick to one of the standard styles.

In this exercise, you'll use pyment to create NumPy style documentation for a function.

Instructions
*In the terminal at the bottom of the screen, use pyment to create NumPy style documentation for the file impyrial/length/core.py
'''

# pyment -w -o numpydoc impyrial/length/core.py

INCHES_PER_FOOT = 12.0  # 12 inches in a foot
INCHES_PER_YARD = INCHES_PER_FOOT * 3.0  # 3 feet in a yard

UNITS = ("in", "ft", "yd")


def inches_to_feet(x, reverse=False):
    """

    Parameters
    ----------
    x :

    reverse :
         (Default value = False)

    Returns
    -------

    """
    if reverse:
        return x * INCHES_PER_FOOT
    else:
        return x / INCHES_PER_FOOT


'''
Writing function documentation with pyment II
Documentation helps your users learn how to use your functions, and can even help remind you how to use them.

In this exercise, you'll fill out your NumPy style documentation template to make some beautiful documentation.

Instructions
*In the text editor, complete the documentation for the inches_to_feet() function. The short description for this function should read "Convert lengths between inches and feet."
*Complete the x parameter documentation with type numpy.ndarray and description "Lengths in feet."
*Complete the reverse parameter documentation with type bool, optional and the description "If true this function converts from feet to inches instead of the default behavior of inches to feet. (Default value = False)".
*Set the return type to numpy.ndarray.
'''

INCHES_PER_FOOT = 12.0  # 12 inches in a foot
INCHES_PER_YARD = INCHES_PER_FOOT * 3.0  # 3 feet in a yard

UNITS = ("in", "ft", "yd")


def inches_to_feet(x, reverse=False):
    """Convert lengths between inches and feet.

    Parameters
    ----------
    x : numpy.ndarray
        Lengths in feet.
    reverse : bool, optional
        If true this function converts from feet to inches
        instead of the default behavior of inches to feet.
        (Default value = False)

    Returns
    -------
    numpy.ndarray
    """
    if reverse:
        return x * INCHES_PER_FOOT
    else:
        return x / INCHES_PER_FOOT


'''
Package and module documentation
Package and module level documentation helps your users navigate your package.

In this exercise, you will write documentation for the impyrial package. Pay attention to this documentation, you're going to be working on this package throughout this course, and it's worth knowing what its different parts do.

Instructions
*Add the following package level documentation to impyrial:

	impyrial
	========
	A package for converting between imperial 
	measurements of length and weight.

*Add the following subpackage level documentation to impyrial.length:

	impyrial.length
	===============
	Length conversion between imperial units.

*Add the following module documentation to impyrial.length.core:
	Conversions between inches and 
	larger imperial length units

'''

# __init__.py (package/parent folder)
"""
impyrial
========
A package for converting between imperial 
measurements of length and weight.
"""

# __init__.py (module/child folder)
"""
impyrial.length
===============
Length conversion between imperial units.
"""

# script file.py
INCHES_PER_FOOT = 12.0  # 12 inches in a foot
INCHES_PER_YARD = INCHES_PER_FOOT * 3.0  # 3 feet in a yard

UNITS = ("in", "ft", "yd")


def inches_to_feet(x, reverse=False):
    """Convert lengths between inches and feet.
    Conversions between inches and
    larger imperial length units

    Parameters
    ----------
    x : numpy.ndarray
        Lengths in feet.
    reverse : bool, optional
        If true this function converts from feet to inches
        instead of the default behavior of inches to feet.
        (Default value = False)

    Returns
    -------
    numpy.ndarray
    """
    if reverse:
        return x * INCHES_PER_FOOT
    else:
        return x / INCHES_PER_FOOT


'''
Sibling imports
The module you documented in the last exercise, impyrial, is growing and you have separated the private functions (the ones you don't really want your users to use) from your public functions. The private functions are in the core.py module and the public ones are in the api.py module.

However, you need to use the private functions to make the public functions work. In this exercise, you will import them into the api.py module to get your package modules working together.

Instructions
*Import the functions inches_to_feet() and inches_to_yards(), and the variable UNITS from the impyrial/length/core.py module into impyrial/length/api.py. Use an absolute import.
*Import the function convert_unit() function in impyrial/length/api.py into the example_script.py script. You'll need to import this using the full filepath to the api module.
*Run the example script to check your imports work.
'''
from impyrial.length.core import (
    UNITS,
    inches_to_feet,
    inches_to_yards,
)

from impyrial.length.api import convert_unit

'''
Importing from parents
In this exercise, you will be importing a function from the utils.py module at the top of your package. A utils module is usually used for small, often unrelated, pieces of code each of which which aren't enough to justify their own module.

You'll import a function for checking the units passed to the convert_units() function. You'll use this checking function in another subpackage later. That's why we don't just put this function in one of the modules in the length subpackage.

Instructions
*Import the function check_units() from the impyrial/utils.py module into impyrial/length/api.py. Use an absolute import.
*Run example_script.py to make sure the check_units() function is working.
'''

'''
Exposing functions to users
Now that your impyrial package has some useful code and is properly organized, it is time to use import structures to expose the functions to users.

Currently, the only function you want to make easily available to users is the convert_unit() function inside the module imperial/length/api.py.

In this exercise, you'll write import statements so that the package can be imported and used like this:

	import impyrial

	result = impyrial.length.convert_unit(6, 'ft', 'yd')

Instructions
*In the __init__.py file within impyrial/length, import the convert_unit() function from the api.py module. Use a relative import.
*Navigate to the __init__.py file in the top level of the impyrial package and import the length subpackage. Use a relative import.
*Run example_script.py to verify that the package imports are correct.
'''