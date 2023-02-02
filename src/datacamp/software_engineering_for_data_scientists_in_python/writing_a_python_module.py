'''
Naming packages
We covered the PEP 8 guidelines for naming packages. In this exercise, you'll use that knowledge to identify a package following the requirements.

For additional reference, you can view the PEP 8 section on package naming here

Instructions
The possible package names to import are the following: text_analyzer, textAnalyzer, TextAnalyzer, & __text_analyzer__.
import the package from the list above that follows the PEP 8 naming conventions.
'''
# Import the package with a name that follows PEP 8
import text_analyzer

''' 
Recognizing packages
The structure of your directory tree is printed below. You'll be working in the file my_script.py that you can see in the tree.

recognizing_packages
├── MY_PACKAGE
│&nbsp;&nbsp; └── _init_.py
├── package
│&nbsp;&nbsp; └── __init__.py
├── package_py
│&nbsp;&nbsp; └── __init__
│&nbsp;&nbsp;     └── __init__.py
├── py_package
│&nbsp;&nbsp; └── __init__.py
├── pyackage
│&nbsp;&nbsp; └── init.py
└── my_script.py

Instructions
*Use the information from the context to identify the packages in the directory that follow the minimal structure.
*import the two packages that follow the minimal package requirements.
*Use help() to print information about each imported package.
'''
# Import local packages
import py_package
import package

# View the help for each package
help(py_package)
help(package)

'''
Adding functionality to your package
Thanks to your work before, you already have a skeleton for your python package. In this exercise, you will work to define the functions needed for a text analysis of word usage.

In the file counter_utils.py, you will write 2 functions to be a part of your package: plot_counter and sum_counters. The structure of your package can be seen in the tree below. For the coding portions of this exercise, you will be working in the file counter_utils.py.

text_analyzer
├── __init__.py
└── counter_utils.py

1)
Define top_items using plot_counter's inputs.
'''
# Import needed functionality
from collections import Counter

def plot_counter(counter, n_most_common=5):
  # Subset the n_most_common items from the input counter
  top_items = counter.most_common(n_most_common)
  # Plot `top_items`
  plot_counter_most_common(top_items)

'''
2)
Return the correct output from sum_counters.
'''
# Import needed functionality
from collections import Counter

def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())

'''
3)
Question
You just wrote two functions for your package in the file counter_utils.py named plot_counter & sum_counters. Which of the following lines would correctly import these functions in __init__.py using relative import syntax?

Answer:
from .counter_utils import plot_counter, sum_counters
'''

'''
Using your package's new functionality

You've now created some great functionality for text analysis to your package. In this exercise, you'll leverage your package to analyze some tweets written by DataCamp & DataCamp users.
The object word_counts is loaded into your environment. It contains a list of Counter objects that contain word counts from a sample of DataCamp tweets.
The structure you've created can be seen in the tree below. You'll be working in my_script.py.

working_dir
├── text_analyzer
│    ├── __init__.py
│    ├── counter_utils.py
└── my_script.py

Instructions
*import your text_analyzer at the top of the script.
*Use the sum_counters() function from text_analyzer to aggregate all the Counters in word_counts.
*Use the plot_counter() function from text_analyzer to visualize the tweet's most used words while tweeting.
'''

# Import local package
import text_analyzer

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
text_analyzer.plot_counter(word_count_totals)

'''
https://campus.datacamp.com/courses/software-engineering-for-data-scientists-in-python/writing-a-python-module?ex=8

Writing requirements.txt
We covered how having a requirements.txt file can help your package be more portable by allowing your users to easily recreate its intended environment. In this exercise, you will be writing the contents of a requirements file to a python variable.

Note, in practice, the code you write in this exercise would be written to it's own txt file instead of a variable in your python session.

Instructions
*Write the requirement for matplotlib with at least version 3.0.0 or above.
*Write the requirement for numpy version 1.15.4 exactly.
*Write the requirement for pandas with at most version 0.22.0.
*Write a non-version specific requirement for pycodestyle
'''
requirements = """
matplotlib>=3.0.0
numpy==1.15.4
pandas<=0.22.0
pycodestyle
"""

"""
Installing package requirements
You've now written a requirements.txt file to recreate your package's environment using a pip install command. Given that you are running a shell session in the work_dir structure shown below, what command would properly recreate the my_package environment from requirements.txt?

work_dir/
├── my_package
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; └── utils.py
├── requirements.txt
└── setup.py

Answer:
pip install -r requirements.txt
"""

"""
Creating setup.py
In order to make your package installable by pip you need to create a setup.py file. In this exercise you will create this file for the text_analyzer package you've been building.

Instructions
*import the needed function, setup, from the setuptools package.
*Complete the name & packages arguments; keep in mind your package is located in a directory named text_analyzer.
*List yourself as the author.
"""
# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='Thiago Siqueira',
      packages=['text_analyzer'])

'''
Listing requirements in setup.py
We created a setup.py file earlier, but we forgot to list our dependency on matplotlib in the install_requires argument. In this exercise you will practice listing your version specific dependencies by correcting the setup.py you previously wrote for your text_analyzer package.

Instructions
*import the needed function, setup, from the setuptools package.
*List yourself as the author.
*Specify your install_requires to require matplotlib version 3.0.0 or above.
'''
# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='Thiago Siqueira',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])