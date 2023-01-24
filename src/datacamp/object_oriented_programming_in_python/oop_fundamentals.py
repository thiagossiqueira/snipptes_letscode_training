'''
Exploring object interface
The best way to learn how to write object-oriented code is to study the design of existing classes. You've already learned about exploration tools like type() and dir().
Another important function is help(): calling help(x) in the console will show the documentation for the object or class x.
Most real world classes have many methods and attributes, and it is easy to get lost, so in this exercise, you will start with something simpler. We have defined a class, and created an object of that class called mystery. Explore the object in the console using the tools that you learned.
'''

#Question
#What class does the mystery object have?
#type(mystery)
#__main__.Employee

'''
So the mystery object is an Employee! Explore it in the console further to find out what attributes it has.
-Print the mystery employee's name attribute.
-Print the employee's salary.
'''
# Print the mystery employee's name
#print(mystery.name)

# Print the mystery employee's salary
#print(mystery.salary)

#help(mystery)
# Give the mystery employee a raise of $2500
#mystery.give_raise(2500)

# Print the salary again
#print(mystery.salary)


class MyCounter:
    def set_count(self, n):
        self.count = n


mc = MyCounter()
mc.set_count(5)
mc.count = mc.count + 1
print(mc.count)


class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self, salary):
        self.mon_sal = self.salary / 12

    """
    def give_raise(self, amount):
        self.salary += amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12
    """


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary(emp.salary)

# Print mon_sal
print(emp.mon_sal)


'''
Add a class constructor
In this exercise, you'll continue working on the Employee class. Instead of using the methods like set_salary() that you wrote in the previous lesson, you will introduce a constructor that assigns name and salary to the employee at the moment when the object is created.
You'll also create a new attribute -- hire_date -- which will not be initialized through parameters, but instead will contain the current date.
Initializing attributes in the constructor is a good idea, because this ensures that the object has all the necessary attributes the moment it is created.

Define the class Employee with a constructor __init__() that:
accepts two arguments, name and salary (with default value0),
creates two attributes, also called name and salary,
sets their values to the corresponding arguments.
'''

# Import datetime from datetime
from datetime import datetime

class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name

        if salary > 0:
            self.salary = salary
        else:
            self.salary = 'Invalid salary!'

        self.hire_date = datetime.today()

    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary / 12


emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)


'''
Write a class from scratch
You are a Python developer writing a visualization package. For any element in a visualization, you want to be able to tell the position of the element, how far it is from other elements, and easily implement horizontal or vertical flip .
The most basic element of any visualization is a single point. In this exercise, you'll write a class for a point on a plane from scratch.

Define the class Point that has:

Two attributes, x and y - the coordinates of the point on the plane;
A constructor that accepts two arguments, x and y, that initialize the corresponding attributes. These arguments should have default value of 0.0;
A method distance_to_origin() that returns the distance from the point to the origin. The formula for that is .
A method reflect(), that reflects the point with respect to the x- or y-axis:
accepts one argument axis,
if axis="x" , it sets the y (not a typo!) attribute to the negative value of the y attribute,
if axis="y", it sets the x attribute to the negative value of the x attribute,
for any other value of axis, prints an error message.
'''


# Write the class Point as outlined in the instructions
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** .5

    def reflect(self, axis):
        if axis == "x":
            self.y = self.y * -1
        elif axis == "y":
            self.x = self.x * -1
        else:
            return "Error"


pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())

p = Point(5.0, 12.0)
p.reflect('x')
p.y