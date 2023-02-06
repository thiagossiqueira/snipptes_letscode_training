'''
How frequently is a function tested?
Many data scientists do not think much about testing, and just do it in the manual way when necessary. But once you see the big picture i.e. the life cycle of a function over the entire project, you appreciate how important testing really is and how frequently you need to test things.

Which of the following is true about testing?

Answer:
A function is tested after the first implementation and then any time the function is modified, which happens mainly when new bugs are found, new features are implemented or the code is refactored.
'''

'''
Manual testing
The function row_to_list(), which you met in the video lesson, has the following expected return values for the arguments listed below.

Argument	Expected return value	Explanation
"2,081\t314,942\n"	["2,081", "314,942"]	Correct row format
"\t293,410\n"	None	Missing area
"1,463238,765\n"	None	Missing tab separator
row_to_list() has been defined and imported for you. Your job is to test the function manually in the IPython console.

While testing manually, notice how many times you have to repeat the same steps! The point is to experience the inefficiency of manual testing.

1)
Question
Call row_to_list() in the IPython console on the three arguments listed in the table. Do the actual return values match the expected return values listed in the table?

Answer:
No. the function returns ["", "293,410"] for the argument "\t293,410\n" instead of the expected return value None.
'''

'''
2)
Question
In the last step, you discovered a bug in our implementation of row_to_list(). Good job!

We have implemented a corresponding bug fix in a new function row_to_list_bugfix(). Call row_to_list_bugfix() in the IPython console on the three arguments listed in the table. Do the actual return values now match the expected return values listed in the table?

Answer:
Yes, the implementation returns the expected value in each case.
'''

'''
Your first unit test using pytest
The data file containing housing area and prices uses commas as thousands separators, e.g. "2,081" or "314,942", as you can see in the IPython Shell.

The convert_to_int() function takes a comma separated integer string as argument, and returns the integer. Therefore, the expected return value of convert_to_int("2,081") is the integer 2081.

This function is defined in the module preprocessing_helpers.py. But it is not known if the function is working properly.

1)
Import the pytest package.
'''
# Import the pytest package
import pytest

'''
2)
Import the function convert_to_int().
'''
# Import the pytest package
import pytest

# Import convert_to_int() from the module preprocessing_helpers.py
from preprocessing_helpers import convert_to_int

'''
3)
Complete the name of the unit test by adding the prefix which pytest uses to distinguish unit tests from ordinary functions.
'''
# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  pass

'''
4)
Complete the assert statement to check if convert_to_int() returns the expected value for the argument "2,081".
'''
# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  # Complete the assert statement
  assert convert_to_int("2,081")==2081

'''
Running unit tests
The tests that you wrote in the previous exercise have been written to a test module test_convert_to_int.py. Try running the tests in the IPython console.

What is the correct IPython console command to run the tests in this test module?

Answer:
!pytest test_convert_to_int.py
'''

'''
What causes a unit test to fail?
In the test result report, the character ., as shown below, stands for a passing test. A passing test is good news as it means that your function works as expected. The character F stands for a failing test. A failing test is bad news as this means that something is broken.

test_row_to_list.py .F.                                                  [100%]
Which of the following describes best why a unit test fails?

Answer:
An exception is raised when running the unit test. This could be an AssertionError raised by the assert statement or another exception, e.g. NameError, which is raised before the assert statement can run.
'''

'''
Spotting and fixing bugs
To find bugs in functions, you need to follow a four step procedure.

Write unit tests.
Run them.
Read the test result report and spot the bugs.
Fix the bugs.
In a previous exercise, you wrote a unit test for the function convert_to_int(), which is supposed to convert a comma separated integer string like "2,081" to the integer 2081. You also ran the unit test and discovered that it is failing.

In this exercise, you will read the test result report from that exercise in detail, and then spot and fix the bug. This would equip you with all basic skills to start using unit tests for your projects.

The convert_to_int() function is defined in the file preprocessing_helpers.py. The unit test is available in the test module test_convert_to_int.py.

1)
Question
Run the unit test in the test module test_convert_to_int.py in the IPython console. Read the test result report and spot the bug.

Which of the following describes the bug in the function convert_to_int(), if any?

Command to run: "!pytest test_convert_to_int.py"
Answer:
convert_to_int("2,081") is expected to return the integer 2081, but it is actually returning the string "2081".
'''

'''
3)
Fix the convert_to_int() function so that it returns the integer 2081 instead of the string "2081" for the argument "2,081".
'''
def convert_to_int(string_with_comma):
    # Fix this line so that it returns an int, not a str
    return int(string_with_comma.replace(",", ""))

'''
Benefits of unit testing
You have been invited to a meeting where company executives are discussing whether developers should write unit tests. The CEO is unsure, and asks you about the benefits that unit testing might bring. In your response, which of the following benefits should you include?

1) Time savings, leading to faster development of new features.
2) Better user experience due to faster code execution.
3) Improved documentation, which will help new colleagues understand the code base better.
4) More user trust in the software product.
5) Better user experience due to improved visualizations.
6) Better user experience due to reduced downtime.

Answer:
1, 3, 4 and 6.
'''

'''
Unit tests as documentation
Assume that you are a new collaborator of our linear regression project on housing area and prices.

While inspecting the project, you come across a function mystery_function() in the feature module. You want to figure out what this function does. As you know, reading the unit tests might give you the answer quickly!

The unit tests for the function is available in the test module test_mystery_function.py. You can read it, and any other file that you encounter, by using the !cat command in the IPython shell.

Having read the unit tests, can you guess what mystery_function() does?

Answer:
It converts data in a data file into a NumPy array.
'''

