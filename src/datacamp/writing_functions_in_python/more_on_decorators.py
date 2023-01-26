'''
Print the return type
You are debugging a package that you've been working on with your friends. Something weird is happening with the data being returned from one of your functions, but you're not even sure which function is causing the trouble. You know that sometimes bugs can sneak into your code when you are expecting a function to return one thing, and it returns something different. For instance, if you expect a function to return a numpy array, but it returns a list, you can get unexpected behavior. To ensure this is not what is causing the trouble, you decide to write a decorator, print_return_type(), that will print out the type of the variable that gets returned from every call of any function it is decorating.

Instructions
*Create a nested function, wrapper(), that will become the new decorated function.
*Call the function being decorated.
*Return the new decorated function.
'''
def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(
            func.__name__, type(result)
        ))
        return result

    # Return the decorated function
    return wrapper


@print_return_type
def foo(value):
    return value


print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

'''
Counter
You're working on a new web app, and you are curious about how many times each of the functions in it gets called. So you decide to write a decorator that adds a counter to each function that you decorate. You could use this information in the future to determine whether there are sections of code that you could remove because they are no longer being used by the app.

Instructions
*Call the function being decorated and return the result.
*Return the new decorated function.
*Decorate foo() with the counter() decorator.
'''
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return counter

    wrapper.count = 0
    # Return the new decorated function
    return wrapper


# Decorate foo() with the counter() decorator
@counter
def foo():
    print('calling foo()')


foo()
foo()

print('foo() was called {} times.'.format(foo.count))

'''
Preserving docstrings when decorating functions
Your friend has come to you with a problem. They've written some nifty decorators and added them to the functions in the open-source library they've been working on. However, they were running some tests and discovered that all of the docstrings have mysteriously disappeared from their decorated functions. Show your friend how to preserve docstrings and other metadata when writing decorators.

1)
Decorate print_sum() with the add_hello() decorator to replicate the issue that your friend saw - that the docstring disappears.
'''


def add_hello(func):
    def wrapper(*args, **kwargs):
        print('Hello')
        return func(*args, **kwargs)

    return wrapper


# Decorate print_sum() with the add_hello() decorator
@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

'''
2)
To show your friend that they are printing the wrapper() function's docstring, not the print_sum() docstring, add the following docstring to wrapper():
"""Print 'hello' and then call the decorated function."""
'''


def add_hello(func):
    # Add a docstring to wrapper
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)

    return wrapper


@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

'''
3)
Import a function that will allow you to add the metadata from print_sum() to the decorated version of print_sum().
'''
# Import the function you need to fix the problem
from functools import wraps

def add_hello(func):
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)

    return wrapper


@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

'''
4)
Finally, decorate wrapper() so that the metadata from func() is preserved in the new decorated function.
'''
from functools import wraps


def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)

    return wrapper


@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

'''
Measuring decorator overhead
Your boss wrote a decorator called check_everything() that they think is amazing, and they are insisting you use it on your function. However, you've noticed that when you use it to decorate your functions, it makes them run much slower. You need to convince your boss that the decorator is adding too much processing time to your function. To do this, you are going to measure how long the decorated function takes to run and compare it to how long the undecorated function would have taken to run. This is the decorator in question:

def check_everything(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    check_inputs(*args, **kwargs)
    result = func(*args, **kwargs)
    check_outputs(result)
    return result
  return wrapper
  
Instructions
Call the original function instead of the decorated version by using an attribute of the function that the wraps() statement in your boss's decorator added to the decorated function.
'''
@check_everything
def duplicate(my_list):
  """Return a new list that repeats the input twice"""
  return my_list + my_list

t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))

'''
Run_n_times()
In the video exercise, I showed you an example of a decorator that takes an argument: run_n_times(). The code for that decorator is repeated below to remind you how it works. Practice different ways of applying the decorator to the function print_sum(). Then I'll show you a funny prank you can play on your co-workers.

def run_n_times(n):
  """Define and return a decorator"""
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

1)
Add the run_n_times() decorator to print_sum() using decorator syntax so that print_sum() runs 10 times.
'''


# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
    print(a + b)


print_sum(15, 20)

'''
2)
Use run_n_times() to create a decorator run_five_times() that will run any function five times.
'''
# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)


@run_five_times
def print_sum(a, b):
    print(a + b)


print_sum(4, 100)

'''
3)
Here's the prank: use run_n_times() to modify the built-in print() function so that it always prints 20 times!
'''
# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')

'''
HTML Generator
You are writing a script that generates HTML for a webpage on the fly. So far, you have written two decorators that will add bold or italics tags to any function that returns a string. You notice, however, that these two decorators look very similar. Instead of writing a bunch of other similar looking decorators, you want to create one decorator, html(), that can take any pair of opening and closing tags.

def bold(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<b>{}</b>'.format(msg)
  return wrapper
  
def italics(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<i>{}</i>'.format(msg)
  return wrapper

1)
Return the decorator and the decorated function from the correct places in the new html() decorator.
'''
def html(open_tag, close_tag):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '{}{}{}'.format(open_tag, msg, close_tag)
    # Return the decorated function
    return wrapper
  # Return the decorator
  return decorator

'''
2)
Use the html() decorator to wrap the return value of hello() in the strings <b> and </b> (the HTML tags that mean "bold").
'''
# Make hello() return bolded text
@html('<b>', '</b>')
def hello(name):
    return 'Hello {}!'.format(name)


print(hello('Alice'))

'''
3)
Use html() to wrap the return value of goodbye() in the strings <i> and </i> (the HTML tags that mean "italics").
'''


# Make goodbye() return italicized text
@html('<i>', '</i>')
def goodbye(name):
    return 'Goodbye {}.'.format(name)


print(goodbye('Alice'))

'''
4)
Use html() to wrap hello_goodbye() in a DIV, which is done by adding the strings <div> and </div> tags around a string.
'''


# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>', '</div>')
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))


print(hello_goodbye('Alice'))

'''
Tag your functions
Tagging something means that you have given that thing one or more strings that act as labels. For instance, we often tag emails or photos so that we can search for them later. You've decided to write a decorator that will let you tag your functions with an arbitrary list of tags. You could use these tags for many things:

Adding information about who has worked on the function, so a user can look up who to ask if they run into trouble using it.
Labeling functions as "experimental" so that users know that the inputs and outputs might change in the future.
Marking any functions that you plan to remove in a future version of the code.
Etc.

Instructions
*Define a new decorator, named decorator(), to return.
*Ensure the decorated function keeps its metadata.
*Call the function being decorated and return the result.
*Return the new decorator.
'''
def tag(*tags):
  # Define a new decorator, named "decorator", to return
  def decorator(func):
    # Ensure the decorated function keeps its metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
      # Call the function being decorated and return the result
      return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
  # Return the new decorator
  return decorator

@tag('test', 'this is a tag')
def foo():
  pass

print(foo.tags)

'''
Check the return type
Python's flexibility around data types is usually cited as one of the benefits of the language. It can sometimes cause problems though if incorrect data types go unnoticed. You've decided that in order to ensure your code is doing exactly what you want it to do, you will explicitly check the return types in all of your functions and make sure they're returning what you expect. To do that, you are going to create a decorator that checks if the return type of the decorated function is correct.

Note: assert is a keyword that you can use to test whether something is true. If you type assert condition and condition is True, this function doesn't do anything. If condition is False, this function raises an error. The type of error that it raises is called an AssertionError.

1)
Start by completing the returns_dict() decorator so that it raises an AssertionError if the return type of the decorated function is not a dictionary.
'''
def returns_dict(func):
    # Complete the returns_dict() decorator
    def wrapper(value):
        result = value
        assert type(result) == dict
        return result

    return wrapper


@returns_dict
def foo(value):
    return value


try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')

'''
2)
Now complete the returns() decorator, which takes the expected return type as an argument.
'''

def returns(return_type):
    # Complete the returns() decorator
    def decorator(func):
        def wrapper(value):
            result = value
            assert type(result) == return_type
            return result

        return wrapper

    return decorator


@returns(dict)
def foo(value):
    return value


try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')