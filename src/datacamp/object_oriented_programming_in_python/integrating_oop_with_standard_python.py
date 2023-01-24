'''
Overloading equality
When comparing two objects of a custom class using ==, Python by default compares just the object references, not the data contained in the objects. To override this behavior, the class can implement the special __eq__() method, which accepts two arguments -- the objects to be compared -- and returns True or False. This method will be implicitly called when two objects are compared.
The BankAccount class from the previous chapter is available for you in the script pane. It has one attribute, balance, and a withdraw() method. Two bank accounts with the same balance are not necessarily the same account, but a bank account usually has an account number, and two accounts with the same account number should be considered the same.

Try selecting the code in lines 1-7 and pressing the "Run code" button. Then try to create a few BankAccount objects in the console and compare them.
  Modify the __init__() method to accept a new parameter - number - and initialize a new number attribute.
  Define an __eq__() method that returns True if the number attribute of two objects is equal.
  Examine the print statements and the output in the console.
'''

class BankAccount:
    # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

        # Define __eq__ that returns True if the number attributes are equal

    def __eq__(self, other):
        return (self.balance == other.balance) and \
               (self.number == other.number)


# Create accounts and compare them
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)

'''
Checking class equality
In the previous exercise, you defined a BankAccount class with a number attribute that was used for comparison. But if you were to compare a BankAccount object to an object of another class that also has a number attribute, you could end up with unexpected results.

For example, consider two classes

class Phone:
  def __init__(self, number):
     self.number = number

  def __eq__(self, other):
    return self.number == \
          other.number

pn = Phone(873555333)

class BankAccount:
  def __init__(self, number):
     self.number = number

  def __eq__(self, other):
    return self.number == \
           other.number

acct = BankAccount(873555333)


Running acct == pn will return True, even though we're comparing a phone number with a bank account number.
It is good practice to check the class of objects passed to the __eq__() method to make sure the comparison makes sense.

Both the Phone and the BankAccount classes have been defined. Try running the code as-is using the "Run code" button and examine the output.
  Modify the definition of BankAccount to only return True if the number attribute is the same and the type() of both objects passed to it is the same.
Run the code and examine the output again.
'''


class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance

    def withdraw(self, amount):
        self.balance -= amount

        # MODIFY to add a check for the type()

    def __eq__(self, other):
        return ((self.number == other.number) and (type(self) == type(other)))


acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)

'''
Comparison and inheritance
What happens when an object is compared to an object of a child class? Consider the following two classes:

class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return True

class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return True
The Child class inherits from the Parent class, and both implement the __eq__() method that includes a diagnostic printout.

Question
Which __eq__() method will be called when the following code is run?

p = Parent()
c = Child()

p == c 
Feel free to experiment in the console -- the classes have already been defined for you.

Possible Answers

Parent's __eq__() method will be called.

Child's __eq__() method will be called.

The code will cause an error.
'''

'''
String formatting review
Before you start defining custom string representations for objects, make sure you are comfortable working with strings and formatting them. If you need a refresher, take a minute to look through the official Python tutorial on string formatting (https://docs.python.org/3/library/stdtypes.html#str.format).
In this exercise, consider the following code
'''
my_num = 5
my_str = "Hello"

#f = "my_num is {0}, and my_str is {1}.".format(my_num, my_str)
f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str)
print(f)

'''
String representation of objects
There are two special methods in Python that return a string representation of an object. __str__() is called when you use print() or str() on an object, and __repr__() is called when you use repr() on an object, print the object in the console without calling print(), or instead of __str__() if __str__() is not defined.
__str__() is supposed to provide a "user-friendly" output describing an object, and __repr__() should return the expression that, when evaluated, will return the same object, ensuring the reproducibility of your code.

In this exercise, you will continue working with the Employee class from Chapter 2.

1)
Add the __str__() method to Employee that satisfies the following:

  If emp is an Employee object with name "Amar Howard" and salary of 40000, then print(emp) outputs
  
Employee name: Amar Howard
Employee salary: 40000
'''
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    # Add the __str__() method
    def __str__(self):
        employee_str = """
            Employee name: {name}  
            Employee salary: {salary}
        """.format(name=self.name,\
                   salary=self.salary)
        return employee_str


emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)
'''
2)
Add the __repr__() method to Employee that satisfies the following:

If emp is an Employee object with name "Amar Howard" and salary of 40000, then repr(emp) outputs
Employee("Amar Howard", 40000)
'''


class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)
        return s

    # Add the __repr__method
    def __repr__(self):
        f = "Employee(\"{name}\", {salary})".format(name=self.name, salary=self.salary)
        return f


emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))

'''
Catching exceptions
Before you start writing your own custom exceptions, let's make sure you have the basics of handling exceptions down.
In this exercise, you are given a function invert_at_index(x, ind) that takes two arguments, a list x and an index ind, and inverts the element of the list at that index. For example invert_at_index([5,6,7], 1) returns 1/6, or 0.166666 .
Try running the code as-is and examine the output in the console. There are two unsafe operations in this function: first, if the element that we're trying to invert has the value 0, then the code will cause a ZeroDivisionError exception. Second, if the index passed to the function is out of range for the list, the code will cause a IndexError. In both cases, the script will be interrupted, which might not be desirable.

Instructions
Use a try - except - except pattern (with two except blocks) inside the function to catch and handle two exceptions as follows:
  try executing the code as-is,
  if ZeroDivisionError occurs, print "Cannot divide by zero!",
  if IndexError occurs, print "Index out of range!"
You know you got it right if the code runs without errors, and the output in the console is:

0.16666666666666666
Cannot divide by zero!
None
Index out of range!
None
'''

# MODIFY the function to catch exceptions
def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")

a = [5,6,0,7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))

'''
Custom exceptions
You don't have to rely solely on built-in exceptions like IndexError: you can define your own exceptions more specific to your application. You can also define exception hierarchies. All you need to define an exception is a class inherited from the built-in Exception class or one of its subclasses.
In Chapter 1, you defined an Employee class and used print statements and default values to handle errors like creating an employee with a salary below the minimum or giving a raise that is too big. A better way to handle this situation is to use exceptions. Because these errors are specific to our application (unlike, for example, a division by zero error which is universal), it makes sense to use custom exception classes.

1)
Define an empty class SalaryError inherited from the built-in ValueError class.
Define an empty class BonusError inherited from the SalaryError class.
'''
# Define SalaryError inherited from ValueError
class SalaryError(ValueError):
    pass

# Define BonusError inherited from SalaryError
class BonusError(SalaryError):
    pass

'''
2)
Complete the definition of __init__() to raise a SalaryError with the message "Salary is too low!" if the salary parameter is less than MIN_SALARY class attribute.
There's no need for else because raise terminates the program anyway.
'''
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
    MIN_SALARY = 30000
    MAX_RAISE = 5000

    def __init__(self, name, salary=30000):
        self.name = name

        # If salary is too low
        if self.salary < Employee.MIN_SALARY:
            # Raise a SalaryError exception
            raise SalaryError("Salary is too low!")
        self.salary = salary

'''
3)
Examine the give_bonus() method, and the rewrite it using exceptions instead of print statements:
  raise a BonusError if the bonus amount is too high;
  raise a SalaryError if the result of adding the bonus would be too low.
'''


class SalaryError(ValueError): pass


class BonusError(SalaryError): pass


class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")
        self.salary = salary

    # Rewrite using exceptions
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus amount is too high!")

        elif self.salary + amount < Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")

        else:
            self.salary += amount

'''
Handling exception hierarchies
Previously, you defined an Employee class with a method get_bonus() that raises a BonusError and a SalaryError depending on parameters. But the BonusError exception was inherited from the SalaryError exception. How does exception inheritance affect exception handling?
The Employee class has been defined for you. It has a minimal salary of 30000 and a maximal bonus amount of 5000.

1)
Question
Experiment with the following code

emp = Employee("Katze Rik", salary=50000)

try:
  emp.give_bonus(7000)
except SalaryError:
  print("SalaryError caught!")

try:
  emp.give_bonus(7000)
except BonusError:
  print("BonusError caught!")

try:
  emp.give_bonus(-100000)
except SalaryError:
  print("SalaryError caught again!")

try:
  emp.give_bonus(-100000)
except BonusError:
  print("BonusError caught again!")  
  
and select the statement which is TRUE about handling parent/child exception classes:

Answer:
a) except block for a parent exception will catch child exceptions
'''

