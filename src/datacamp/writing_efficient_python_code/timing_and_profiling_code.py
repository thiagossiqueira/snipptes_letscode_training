'''
Using %timeit: your turn!
You'd like to create a list of integers from 0 to 50 using the range() function. However, you are unsure whether using list comprehension or unpacking the range object into a list is faster. Let's use %timeit to find the best implementation.

For your convenience, a reference table of time orders of magnitude is provided below (faster at the top).

symbol	   name	               unit (s)
ns	         nanosecond	10^-9
µs (us)	 microsecond	10^-6
ms	        millisecond	       10^-3
s	        second	               10^0

1)
Use list comprehension and range() to create a list of integers from 0 to 50 called nums_list_comp.
'''
# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

'''
2)
Use range() to create a list of integers from 0 to 50 and unpack its contents into a list called nums_unpack.
'''
# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*(nums_list_comp)]
print(nums_unpack)

'''
3)
Question
Use %timeit within your IPython console (i.e. not within the script.py window) to compare the runtimes for creating a list of integers from 0 to 50 using list comprehension vs. unpacking the range object. Don't include the print() statements when timing.

Which method was faster?

Answer:

%timeit nums_list_comp = [num for num in range(51)]

%timeit nums_unpack = [*(range(51))]

Unpacking the range object was faster than list comprehension.
'''

'''
Using %timeit: specifying number of runs and loops
A list of 480 superheroes has been loaded into your session (called heroes). You'd like to analyze the runtime for converting this heroes list into a set. Instead of relying on the default settings for %timeit, you'd like to only use 5 runs and 25 loops per each run.

What is the correct syntax when using %timeit and only using 5 runs with 25 loops per each run?

Answer:
%timeit -r5 -n25 set(heroes)
'''

'''
Using %timeit: formal name or literal syntax
Python allows you to create data structures using either a formal name or a literal syntax. In this exercise, you'll explore how using a literal syntax for creating a data structure can speed up runtimes.

data structure	formal name	     literal syntax
list	                       list()	             []
dictionary	       dict()	             {}
tuple	               tuple()	             ()

1)
Create an empty list called formal_list using the formal name (list()).
Create an empty list called literal_list using the literal syntax ([]).
'''
# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

'''
2)
Print out the type of formal_list and literal_list to show that both naming conventions create a list.
'''
# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

'''
3)
Question
Use %timeit in your IPython console to compare runtimes between creating a list using the formal name (list()) and the literal syntax ([]). Don't include the print() statements when timing.

Which naming convention is faster?

Answer:
%timeit formal_list = list()
%timeit literal_list = []

Using the literal syntax ([]) to create a list is faster.
'''

'''
Using cell magic mode (%%timeit)
From here on out, you'll be working with a superheroes dataset. For this exercise, a list of each hero's weight in kilograms (called wts) is loaded into your session. You'd like to convert these weights into pounds.

You could accomplish this using the below for loop:

hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)

Or you could use a numpy array to accomplish this task:

wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462

Use %%timeit in your IPython console to compare runtimes between these two approaches. Make sure to press SHIFT+ENTER after the magic command to add a new line before writing the code you wish to time. After you've finished coding, answer the following question:

Which of the above techniques is faster?

Instructions
Answer:

%%timeit
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)

# output: 1.02 ms +- 74 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)



%%timeit
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462

# output:  20 us +- 134 ns per loop (mean +- std. dev. of 7 runs, 10000 loops each)

The numpy technique was faster.
'''

'''
Pop quiz: steps for using %lprun
Below is the convert_units() function, which converts the heights and weights of our favorite superheroes from metric units to Imperial units.

def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

Suppose you have a list of superheroes (named heroes) along with each hero's height (in centimeters) and weight (in kilograms) loaded as NumPy arrays (named hts and wts respectively).

What are the necessary steps you need to take in order to profile the convert_units() function acting on your superheroes data if you'd like to see line-by-line runtimes?

Answer:
1)Use %load_ext line_profiler to load the line_profiler within your IPython 

2)Use %lprun -f convert_units convert_units(heroes, hts, wts) to get line-by-line runtimes.

answer: The first and second options from above are necessary.
'''

'''
Using %lprun: spot bottlenecks
Profiling a function allows you to dig deeper into the function's source code and potentially spot bottlenecks. When you see certain lines of code taking up the majority of the function's runtime, it is an indication that you may want to deploy a different, more efficient technique.

Lets dig deeper into the convert_units() function.

def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data
Load the line_profiler package into your IPython session. Then, use %lprun to profile the convert_units() function acting on your superheroes data. Remember to use the special syntax for working with %lprun (you'll have to provide a -f flag specifying the function you'd like to profile).

The convert_units() function, heroes list, hts array, and wts array have been loaded into your session. After you've finished coding, answer the following question:

What percentage of time is spent on the new_hts list comprehension line of code relative to the total amount of time spent in the convert_units() function?

Answers:
11% - 20%
'''

'''
Using %lprun: fix the bottleneck
In the previous exercise, you profiled the convert_units() function and saw that the new_hts list comprehension could be a potential bottleneck. Did you notice that the new_wts list comprehension also accounted for a similar percentage of the runtime? This is an indication that you may want to create the new_hts and new_wts objects using a different technique.

Since the height and weight of each hero is stored in a numpy array, you can use array broadcasting rather than list comprehension to convert the heights and weights. This has been implemented in the below function:

def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data
    
Load the line_profiler package into your IPython session. Then, use %lprun to profile the convert_units_broadcast() function acting on your superheroes data. The convert_units_broadcast() function, heroes list, hts array, and wts array have been loaded into your session. After you've finished coding, answer the following question:

What percentage of time is spent on the new_hts array broadcasting line of code relative to the total amount of time spent in the convert_units_broadcast() function?

Answer:
0% - 10%
'''

'''
Pop quiz: steps for using %mprun
Suppose you have a list of superheroes (named heroes) along with each hero's height (in centimeters) and weight (in kilograms) loaded as NumPy arrays (named hts and wts, respectively). You also have a convert_units() function saved in a file titled hero_funcs.py.

What are the necessary steps you need to take in order to profile the convert_units() function acting on your superheroes data if you'd like to see the line-by-line memory consumption of convert_units()?

Answer:
1) Use the command from hero_funcs import convert_units to load the function you'd like to profile.

2) Use %load_ext memory_profiler to load the memory_profiler within your IPython session.

3) Use %mprun -f convert_units convert_units(heroes, hts, wts) to get line-by-line memory allocations.

[x] 4) All of the above.
'''

'''
Using %mprun: Hero BMI
You'd like to calculate the body mass index (BMI) for a selected sample of heroes. BMI can be calculated using the below formula:

BMI = mass(kg) / height(m)^2

A random sample of 25,000 superheroes has been loaded into your session as an array called sample_indices. This sample is a list of indices that corresponds to each superhero's index selected from the heroes list.

A function named calc_bmi_lists has also been created and saved to a file titled bmi_lists.py. For convenience, it is displayed below:

def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis
    
Notice that this function performs all necessary calculations using list comprehension (hence the name calc_bmi_lists()). Dig deeper into this function and analyze the memory footprint for performing your calculations using lists:

Load the memory_profiler package into your IPython session.
Import calc_bmi_lists from bmi_lists.
Once you've completed the above steps, use %mprun to profile the calc_bmi_lists() function acting on your superheroes data. The hts array and wts array have already been loaded into your session.
After you've finished coding, answer the following question:

How much memory do the list comprehension lines of code consume in the calc_bmi_lists() function? (i.e., what is the total sum of the Increment column for these four lines of code?)

Steps taken on the IPython:
%load_ext memory_profiler
from bmi_lists import calc_bmi_lists
%mprun -f calc_bmi_lists calc_bmi_lists(sample_indices, hts, wts)

Answer:
0.1 MiB - 2.0 MiB
'''

'''
Using %mprun: Hero BMI 2.0
Let's see if using a different approach to calculate the BMIs can save some memory. If you remember, each hero's height and weight is stored in a numpy array. That means you can use NumPy's handy array indexing capabilities and broadcasting to perform your calculations. A function named calc_bmi_arrays has been created and saved to a file titled bmi_arrays.py. For convenience, it is displayed below:

def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis
    
Notice that this function performs all necessary calculations using arrays.

Let's see if this updated array approach decreases your memory footprint:

Load the memory_profiler package into your IPython session.
Import calc_bmi_arrays from bmi_arrays.
Once you've completed the above steps, use %mprun to profile the calc_bmi_arrays() function acting on your superheroes data. The sample_indices array, hts array, and wts array have been loaded into your session.
After you've finished coding, answer the following question:

How much memory do the array indexing and broadcasting lines of code consume in the calc_bmi_array() function? (i.e., what is the total sum of the Increment column for these four lines of code?)

Answer:
0.1 MiB - 2.0 MiB
'''

'''
Bringing it all together: Star Wars profiling
A list of 480 superheroes has been loaded into your session (called heroes) as well as a list of each hero's corresponding publisher (called publishers).

You'd like to filter the heroes list based on a hero's specific publisher, but are unsure which of the below functions is more efficient.

def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes
    
def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes
    
1)
Use the get_publisher_heroes() function and the get_publisher_heroes_np() function to collect heroes from the Star Wars universe. The desired_publisher for Star Wars is 'George Lucas'.
'''
# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

'''
2)
Question
Within your IPython console, load the line_profiler and use %lprun to profile the two functions for line-by-line runtime. When using %lprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:
Which function has the fastest runtime?


%load_ext line_profiler
%lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')       >>> Total time: 0.000344 s
%lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas') >>> Total time: 0.000156 s

Answer:
get_publisher_heroes_np() is faster.
'''

'''
3)
Question
Within your IPython console, load the memory_profiler and use %mprun to profile the two functions for line-by-line memory consumption.
The get_publisher_heroes() function and get_publisher_heroes_np() function have been saved within a file titled hero_funcs.py (i.e., you can import both functions from hero_funcs). When using %mprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:

Which function uses the least amount of memory?

from hero_funcs import get_publisher_heroes
%load_ext memory_profiler
%mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas') >>> 115.6 MiB

from hero_funcs import get_publisher_heroes_np
%load_ext memory_profiler
%mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')  >>> 115.6 MiB

Answer:
Both functions have the same memory consumption.
'''

'''
4)
Question
Based on your runtime profiling and memory allocation profiling, which function would you choose to gather Star Wars heroes?

Answer:
I would use get_publisher_heroes_np().
'''