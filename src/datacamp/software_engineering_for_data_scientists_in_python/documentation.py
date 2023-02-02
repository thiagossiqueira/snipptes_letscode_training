'''
Identifying good comments
We learned about what characteristics make a 'good' comment. In this exercise, you'll apply this knowledge to identify a function that utilizes comment best practices.

Instructions
*print the text variable that has been pre-loaded into your environment.
*print the result of calling the function with more useful commenting on text.
'''

import re

def extract_0(text):
    # match and extract dollar amounts from the text
    return re.findall(r'\$\d+\.\d\d', text)

def extract_1(text):
    # return all matches to regex pattern
    return re.findall(r'\$\d+\.\d\d', text)

# Print the text
print(text)

# Print the results of the function with better commenting
print(extract_0(text))

'''
Identifying proper docstrings
We covered how to write fully-fledged docstrings. Before writing one of your own, this exercise will help you practice by having you identify a properly formatted docstring.

In this exercise, you'll be using the functions goldilocks(), rapunzel(), mary(), and sleeping_beauty() which have been loaded in your environment.

1)
Run help() on each of the 4 functions to view their docstrings.
'''
# Run the help on all 4 functions
help(goldilocks)
help(rapunzel)
help(mary)
help(sleeping_beauty)

'''
2)
*Define result using the function that has the most complete docstring; only 1 of the 4 contains all the sections we covered. Call the function without any parameters.
*print the result of the most well documented function.
'''
# Run the help on all 4 functions
help(goldilocks)
help(rapunzel)
help(mary)
help(sleeping_beauty)

# Execute the function with most complete docstring
result = rapunzel()

# Print the result
print(result)

'''
Writing docstrings
We just learned some about the benefits of docstrings. In this exercise, you will practice writing docstrings that can be utilized by a documentation generator like Sphinx.

Note that your docstring submission must match the solution exactly. If you find yourself getting it wrong several times, it may be a good idea to refresh the sample code and start over.

Instructions
*Complete the portions of the docstring that document the parameters.
*Complete the portion of the docstring describing the return value.
*Complete the example function usage in the docstring.
'''
# Complete the function's docstring
def tokenize(text, regex=r'[a-zA-z]+'):
  """Split text into tokens using a regular expression

  :param text: text to be tokenized
  :param regex: regular expression used to match tokens using re.findall
  :return: a list of resulting tokens

  >>> tokenize('the rain in spain')
  ['the', 'rain', 'in', 'spain']
  """
  return re.findall(regex, text, flags=re.IGNORECASE)

# Print the docstring
help(tokenize)

'''
Using good function names
A good function name can go a long way for both user and maintainer understanding. A good function name is descriptive and describes what a function does. In this exercise, you'll choose a name for a function that will help aid in its readability when used.

Instructions
*The math module has been pre-loaded into your environment to be able to use its sqrt function.
*Give function the best possible name from the following options: do_stuff, hypotenuse_length, square_root_of_leg_a_squared_plus_leg_b_squared, pythagorean_theorem.
*Complete the docstring's example with the function's name.
*print the result of using the newly named function to find the length of the hypotenuse for a right triangle with legs of length 6 & 8.
'''
def hypotenuse_length(leg_a, leg_b):
    """Find the length of a right triangle's hypotenuse

    :param leg_a: length of one leg of triangle
    :param leg_b: length of other leg of triangle
    :return: length of hypotenuse

    >>> hypotenuse_length(3, 4)
    5
    """
    return math.sqrt(leg_a ** 2 + leg_b ** 2)


# Print the length of the hypotenuse with legs 6 & 8
print(hypotenuse_length(6, 8))

'''
Using good variable names
Just like functions, descriptive variable names can make your code much more readable. In this exercise, you'll write some code using good variable naming practices.

There's not always a clear best name for a variable. The exercise has been written to try and make a clear best choice from the provided options.

Instructions
*Choose the best variable name to hold the sample of pupil diameter measurements in millimeters from the following choices: d, diameter, pupil_diameter, or pupil_diameter_in_millimeters.
*Take the mean of the measurements and assign it to a variable. Choose the best variable name to hold this mean from the following options: m, mean, mean_diameter, or mean_pupil_diameter_in_millimeters.
*Print the resulting average pupil diameter.
'''
from statistics import mean

# Sample measurements of pupil diameter in mm
pupil_diameter = [3.3, 6.8, 7.0, 5.4, 2.7]

# Average pupil diameter from sample
mean_diameter = mean(pupil_diameter)

print(mean_diameter)

'''
Refactoring for readability
Refactoring longer functions into smaller units can help with both readability and modularity. In this exercise, you will refactor a function into smaller units. The function you will be refactoring is shown below. Note, in the exercise, you won't be using docstrings for the sake of space; in a real application, you should include documentation!

def polygon_area(n_sides, side_len):
    """Find the area of a regular polygon

    :param n_sides: number of sides
    :param side_len: length of polygon sides
    :return: area of polygon

    >>> round(polygon_area(4, 5))
    25
    """
    perimeter = n_sides * side_len

    apothem_denominator = 2 * math.tan(math.pi / n_sides)
    apothem = side_len / apothem_denominator

    return perimeter * apothem / 2
    
Instructions
*Move the logic for calculating the perimeter into the polygon_perimeter function.
*Complete the definition of the polygon_apothem function, by moving the logic seen in the context. The math module has already been imported for you.
*Utilize the new unit functions to complete the definition of polygon_area.
*Use the more unitized polygon_area to calculate the area of a regular hexagon with legs of size 10.
'''
def polygon_perimeter(n_sides, side_len):
    return n_sides * side_len

def polygon_apothem(n_sides, side_len):
    denominator = 2 * math.tan(math.pi / n_sides)
    return side_len / denominator

def polygon_area(n_sides, side_len):
    perimeter = polygon_perimeter(n_sides, side_len)
    apothem = polygon_apothem(n_sides, side_len)

    return perimeter * apothem / 2

# Print the area of a hexagon with legs of size 10
print(polygon_area(n_sides=6, side_len=10))

'''
Using doctest
We just learned about doctest, which, if you're writing full docstrings with examples, is a simple way to minimally test your functions. In this exercise, you'll get some hands-on practice testing and debugging with doctest.

The following have all be pre-loaded in your environment: doctest, Counter, and text_analyzer.

Note that your docstring submission must match the solution exactly. If you find yourself getting it wrong several times, it may be a good idea to refresh the sample code and start over.

Instructions
*Complete the input code of the example in the docstring for sum_counters.
*Complete the docstring example by filling in the expected output.
*Run the testmod function from doctest to test your function's example code.
'''
def sum_counters(counters):
    """Aggregate collections.Counter objects by summing counts

    :param counters: list/tuple of counters to sum
    :return: aggregated counters with counts summed

    >>> d1 = text_analyzer.Document('1 2 fizz 4 buzz fizz 7 8')
    >>> d2 = text_analyzer.Document('fizz buzz 11 fizz 13 14')
    >>> sum_counters([d1.word_counts, d2.word_counts])
    Counter({'fizz': 4, 'buzz': 2})
    """
    return sum(counters, Counter())

doctest.testmod()

'''
Using pytest
doctest is a great tool, but it's not nearly as powerful as pytest. In this exercise, you'll write tests for your SocialMedia class using the pytest framework.

1)
Question
Before you start writing tests, you need to be working in an appropriately named file for pytest to find your test. Which of the following would be the best, valid name for file containing tests for the SocialMedia class?

Answer:
test_social_media.py
'''

'''
2)
*import the SocialMedia class.
*Complete the name of the test function so it is run by pytest.
*Use the appropriate keyword to test that the hashtag_counts are as expected.
'''
from collections import Counter
from text_analyzer import SocialMedia

# Create an instance of SocialMedia for testing
test_post = 'learning #python & #rstats is awesome! thanks @datacamp!'
sm_post = SocialMedia(test_post)

# Test hashtag counts are created properly
def test_social_media_hashtags():
    expected_hashtag_counts = Counter({'#python': 1, '#rstats': 1})
    assert sm_post.hashtag_counts == expected_hashtag_counts

'''
Documenting classes for Sphinx
sphinx is a great tool for rendering documentation as HTML. In this exercise, you'll write a docstring for a class that can be taken advantage of by sphinx.

Note that your docstring submission must match the solution exactly. If you find yourself getting it wrong several times, it may be a good idea to refresh the sample code and start over.

Instructions
*import the Document class from the text_analyzer package for use in the class definition.
*Complete the line of the docstring dealing with the parameters of the __init__ method.
*Complete the docstring by filling out the documentation for the attributes or 'instance variables' of the SocialMedia class.
'''
from text_analyzer import Document


class SocialMedia(Document):
    """Analyze text data from social media

    :param text: social media text to analyze

    :ivar hashtag_counts: Counter object containing counts of hashtags used in text
    :ivar mention_counts: Counter object containing counts of @mentions used in text
    """

    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

'''
Identifying tools
Which of following lists of tools best corresponds to the 3 software engineering concepts of Modularity, Documentation, & Automated Testing. The correct answer will have the tools listed in the order that best corresponds to which concept they help you with.

After this exercise you will be nearly done with the course! If you enjoyed it, feel free to send Adam a thank you via Twitter - he'll appreciate it! Tweet to Adam

Answer:
Code Climate, Sphinx, & Travis CI
'''