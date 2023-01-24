'''
Polymorphic methods
To design classes effectively, you need to understand how inheritance and polymorphism work together.
In this exercise, you have three classes - one parent and two children - each of which has a talk() method. Analyze the following code:
'''
class Parent:
    def talk(self):
        print("Parent talking!")

class Child(Parent):
    def talk(self):
        print("Child talking!")

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild talking!")
        Parent.talk(self)


p, c, tc = Parent(), Child(), TalkativeChild()

for obj in (p, c, tc):
    obj.talk()

'''
https://campus.datacamp.com/courses/object-oriented-programming-in-python/best-practices-of-class-design?ex=3

Square and rectangle
The classic example of a problem that violates the Liskov Substitution Principle is the Circle-Ellipse problem, sometimes called the Square-Rectangle problem.

By all means, it seems like you should be able to define a class Rectangle, with attributes h and w (for height and width), and then define a class Square that inherits from the Rectangle. After all, a square "is-a" rectangle!

Unfortunately, this intuition doesn't apply to object-oriented design.

1)
Create a class Rectangle with a constructor that accepts two parameters, h and w, and sets its h and w attributes to the values of h and w.
Create a class Square inherited from Rectangle with a constructor that accepts one parameter w, and sets both the h and w attributes to the value of w.
'''


# Define a Rectangle class
class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w


# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        self.h = w
        self.w = w


'''
A Square inherited from a Rectangle will always have both the h and w attributes, but we can't allow them to change independently of each other.

Define methods set_h() and set_w() in Rectangle, each accepting one parameter and setting h and w.
Define methods set_h() and set_w() in Square, each accepting one parameter, and setting both h and w to that parameter in both methods.
'''


class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    # Define set_h to set h
    def set_h(self, h):
        self.h = h

    # Define set_w to set w
    def set_w(self, w):
        self.w = w


class Square(Rectangle):
    def __init__(self, w):
        self.w, self.h = w, w

    # Define set_h to set w and h
    def set_h(self, h):
        self.h = h
        self.w = h

    # Define set_w to set w and h
    def set_w(self, w):
        self.w = w
        self.h = w


'''
Attribute naming conventions
In Python, all data is public. Instead of access modifiers common in languages like Java, Python uses naming conventions to communicate the developer's intention to class users, shifting the responsibility of safe class use onto the class user.

Python uses underscores extensively to signal the purpose of methods and attributes. In this exercise, you will match a use case with the appropriate naming convention.

_name >>> A helper method that checks validity of an attributite's value but isn't considered a part of class's public interface

__name >>> A 'version' attribute that stores the current version of the class and shouldn't be passed to child class, who will have their own versions.

__name__ >>> A method that is run whenever the object is printed
'''
'''
Using internal attributes
In this exercise, you'll return to the BetterDate class of Chapter 2. Your date class is better because it will use the sensible convention of having exactly 30 days in each month.

You decide to add a method that checks the validity of the date, but you don't want to make it a part of BetterDate's public interface.

The class BetterDate is available in the script pane.

Instructions
    Add a class attribute _MAX_DAYS storing the maximal number of days in a month - 30.
    Add another class attribute storing the maximal number of months in a year - 12. Use the appropriate naming convention to indicate that this is an internal attribute.
    Add an _is_valid() method that returns True if the day and month attributes are less than or equal to the corresponding maximum values, and False otherwise. Make sure to refer to the class attributes by their names!
'''


# Add class attributes for max number of days and months
class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTHS = 12

    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    # Add _is_valid() checking day and month values
    def _is_valid(self):
        if self.day <= self._MAX_DAYS:
            print(True)
        else:
            print(False)

        if self.month <= self._MAX_MONTHS:
            print(True)
        else:
            print(False)


bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())

'''
What do properties do?
You could think of properties as attributes with built-in access control. They are especially useful when there is some additional code you'd like to execute when assigning values to attributes.

Which of the following statements is NOT TRUE about properties?

Answers:
  Properties can be used to implement "read-only" attributes
  Properties can be accessed using the dot syntax just like regular attributes
  Properties allow for validation of values that are assigned to them
'''

'''
Create and set properties
There are two parts to defining a property:

first, define an "internal" attribute that will contain the data;
then, define a @property-decorated method whose name is the property name, and that returns the internal attribute storing the data.
If you'd also like to define a custom setter method, there's an additional step:

define another method whose name is exactly the property name (again), and decorate it with @prop_name.setter where prop_name is the name of the property. The method should take two arguments -- self (as always), and the value that's being assigned to the property.
In this exercise, you'll create a balance property for a Customer class - a better, more controlled version of the balance attribute that you worked with before.

1)
Create a Customer class with the __init__() method that:

takes parameters name and new_bal,
assigns name to the attribute name,
raises a ValueError if new_bal is negative,
otherwise, assigns new_bal to the attribute _balance (with _).
'''


# Create a Customer class
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal


'''
2)
Add a method balance() with a @property decorator that returns the _balance attribute.
'''


class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal

        # Add a decorated balance() method returning _balance

    @property
    def balance(self):
        return self._balance


'''
3)
Define another balance() method to serve as a setter, with the appropriate decorator and an additional parameter:

Raise a ValueError if the parameter is negative,
otherwise assign it to _balance ;
print "Setter method is called".
'''


class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal

        # Add a decorated balance() method returning _balance

    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal
        # Print "Setter method is called"
        print("Setter method is called")


'''
4)
Create a Customer named Belinda Lutz with the balance of 2000 and save it as cust.
Use the dot syntax and the = to assign 3000 to cust.balance.
Print cust.balance.
In the console, try assigning -1000 to cust.balance. What happens?
'''


class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal

        # Add a decorated balance() method returning _balance

    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")


# Create a Customer
cust = Customer("Belinda Lutz", 2000)

# Assign 3000 to the balance property
cust.balance = 3000

# Print the balance property
print(cust.balance)

'''
Read-only properties
The LoggedDF class from Chapter 2 was an extension of the pandas DataFrame class that had an additional created_at attribute that stored the timestamp when the DataFrame was created, so that the user could see how out-of-date the data is.

But that class wasn't very useful: we could just assign any value to created_at after the DataFrame was created, thus defeating the whole point of the attribute! Now, using properties, we can make the attribute read-only.

The LoggedDF class from Chapter 2 is available for you in the script pane.

Instructions 1)
Assign a new value of '2035-07-13' to the created_at attribute.
Print the value of ldf's created_at attribute to verify that your assignment was successful.
'''
import pandas as pd
from datetime import datetime


# LoggedDF class definition from Chapter 2
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self.created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)

    # Instantiate a LoggedDF called ldf


ldf = LoggedDF({"col1": [1, 2], "col2": [3, 4]})

# Assign a new value to ldf's created_at attribute and print
ldf.created_at = '2035-07-13'
print(ldf.created_at)

'''
2)
Create an internal attribute called _created_at to turn created_at into a read-only attribute.
Modify the class to use the internal attribute, _created_at, in place of created_at.
'''

import pandas as pd
from datetime import datetime


# MODIFY the class to use _created_at instead of created_at
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)

        # Add a read-only property: _created_at

    @property
    def created_at(self):
        return self._created_at


# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1, 2], "col2": [3, 4]})
