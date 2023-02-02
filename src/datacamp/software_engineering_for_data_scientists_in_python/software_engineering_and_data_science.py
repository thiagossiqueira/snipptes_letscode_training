'''
Python modularity in the wild
In the slides, we covered 3 ways that you can write modular code with Python: packages, classes, and methods. For reference, you can see the example code we reviewed below.

# Import the pandas PACKAGE
import pandas as pd

# Create some example data
data = {'x': [1, 2, 3, 4],
        'y': [20.1, 62.5, 34.8, 42.7]}

# Create a dataframe CLASS object
df = pd.DataFrame(data)

# Use the plot METHOD
df.plot('x', 'y')
In this exercise, you'll utilize a class & a method from the popular package numpy.

Instructions
*Complete the import statement to load the numpy package.
*Use numpy's array class to define arr.
*Use arr's sort method to sort the numpy array.
'''
# import the numpy package
import numpy as np

# create an array class object
arr = np.array([8, 6, 7, 5, 3, 0, 9])

# use the sort method
arr.sort()

# print the sorted array
print(arr)

'''
Leveraging documentation
When writing code for Data Science, it's inevitable that you'll need to install and use someone else's code. You'll quickly learn that using someone else's code is much more pleasant when they use good software engineering practices. In particular, good documentation makes the right way to call a function obvious. In this exercise you'll use python's help() method to view a function's documentation so you can determine how to correctly call a new method.
The list 'words' has been loaded in your session.

1)
View the documentation of the Counter.most_common method using the help() function. Note, you need to run the import statement before completing this step.
'''
# load the Counter function into our environment
from collections import Counter

# View the documentation for Counter.most_common
help(Counter.most_common)

'''
2)
*Correctly call Counter.most_common() by reading its documentation.
*Print the results stored in top_5_words.
'''
# load the Counter function into our environment
from collections import Counter

# View the documentation for Counter.most_common
help(Counter.most_common)

# use Counter to find the top 5 most common words
top_5_words = Counter(words).most_common(5)

# display the top 5 most common words
print(top_5_words)

'''
Using pycodestyle
We saw earlier that pycodestyle can be run from the command line to check a file for PEP 8 compliance. Sometimes it's useful to run this kind of check from a Python script.

In this exercise, you'll use pycodestyle's StyleGuide class to check multiple files for PEP 8 compliance. Both files accomplish the same task, but they differ greatly in formatting and readability. You can view the contents of the files by following their links below.

Instructions
*Import the pycodestyle package.
*Create an instance of StyleGuide named style_checker.
*There are two files that we'll be checking; they're named 'nay_pep8.py' and 'yay_pep8.py'. Pass a list containing these file names to our style_checker's check_files method.
*print() the results of our style check to the console. Make sure to read the output!
'''
# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['nay_pep8.py', 'yay_pep8.py'])

# Print result of PEP 8 style check
print(result.messages)

'''
Conforming to PEP 8
As we've covered, there are tools available to check if your code conforms to the PEP 8 guidelines. One possible way to stay compliant is to use an IDE that warns you when you accidentally stray from the style guide. Another way to check code is to use the pycodestyle package.

The results below show the output of running pycodestyle check against the code shown in your editor. The leading number in each line shows how many occurrences there were of that particular violation.

my_script.py:2:2:  E225 missing whitespace around operator
my_script.py:2:7:  E231 missing whitespace after ','
my_script.py:2:9:  E231 missing whitespace after ','
my_script.py:5:7:  E201 whitespace after '('
my_script.py:5:11: E202 whitespace before ')'

Instructions
Leverage the output of pycodestyle to edit the code to be compliant with PEP 8.
'''
# Assign data to x
x = [8, 3, 4]

# Print the data
print(x)

'''
PEP 8 in documentation
So far we've focused on how PEP 8 affects functional pieces of code. There are also rules to help make comments and documentation more readable. In this exercise, you'll be fixing various types of comments to be PEP 8 compliant.

The result of a pycodestyle style check on the code can be seen below.

my_script.py:2:15: E261 at least two spaces before inline comment
my_script.py:5:16: E262 inline comment should start with '# '
my_script.py:11:1: E265 block comment should start with '# '
my_script.py:13:2: E114 indentation is not a multiple of four (comment)
my_script.py:13:2: E116 unexpected indentation (comment)

Instructions
Leverage the output of pycodestyle to edit the code's comments to be compliant with PEP 8.
'''
def print_phrase(phrase, polite=True, shout=False):
    if polite:  # It's generally polite to say please
        phrase = 'Please ' + phrase

    if shout:  # All caps looks like a written shout
        phrase = phrase.upper() + '!!'

    print(phrase)


# Politely ask for help
print_phrase('help me', polite=True)
# Shout about a discovery
print_phrase('eureka', shout=True)

