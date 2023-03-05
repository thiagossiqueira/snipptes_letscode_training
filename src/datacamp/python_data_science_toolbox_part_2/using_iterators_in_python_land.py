'''
Iterators vs. Iterables
Let's do a quick recall of what you've learned about iterables and iterators. Recall from the video that an iterable is an object that can return an iterator, while an iterator is an object that keeps state and produces the next value when you call next() on it. In this exercise, you will identify which object is an iterable and which is an iterator.

The environment has been pre-loaded with the variables flash1 and flash2. Try printing out their values with print() and next() to figure out which is an iterable and which is an iterator.

Answer:
flash1 is an iterable and flash2 is an iterator.
'''

'''
Iterating over iterables (1)
Great, you're familiar with what iterables and iterators are! In this exercise, you will reinforce your knowledge about these by iterating over and printing from iterables and iterators.

You are provided with a list of strings flash. You will practice iterating over the list by using a for loop. You will also create an iterator for the list and access the values from the iterator.

Instructions
*Create a for loop to loop over flash and print the values in the list. Use person as the loop variable.
*Create an iterator for the list flash and assign the result to superhero.
*Print each of the items from superhero using next() 4 times.
'''
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)


# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

'''
Iterating over iterables (2)
One of the things you learned about in this chapter is that not all iterables are actual lists. A couple of examples that we looked at are strings and the use of the range() function. In this exercise, we will focus on the range() function.

You can use range() in a for loop as if it's a list to be iterated over:
    
    for i in range(5):
        print(i)
        
Recall that range() doesn't actually create the list; instead, it creates a range object with an iterator that produces the values until it reaches the limit (in the example, until the value 4). If range() created the actual list, calling it with a value of may not work, especially since a number as big as that may go over a regular computer's memory. The value is actually what's called a Googol which is a 1 followed by a hundred 0s. That's a huge number!

Your task for this exercise is to show that calling range() with won't actually pre-create the list.

Instructions
*Create an iterator object small_value over range(3) using the function iter().
*Using a for loop, iterate over range(3), printing the value for every iteration. Use num as the loop variable.
*Create an iterator object googol over range(10 ** 100).
'''

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

'''
Iterators as function arguments
You've been using the iter() function to get an iterator object, as well as the next() function to retrieve the values one by one from the iterator object.

There are also functions that take iterators and iterables as arguments. For example, the list() and sum() functions return a list and the sum of elements, respectively.

In this exercise, you will use these functions by passing an iterable from range() and then printing the results of the function calls.

Instructions
*Create a range object that would produce the values from 10 to 20 using range(). Assign the result to values.
*Use the list() function to create a list of values from the range object values. Assign the result to values_list.
*Use the sum() function to get the sum of the values from 10 to 20 from the range object values. Assign the result to values_sum.
'''
# Create a range object: values
values = range(10,21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)

'''
Using enumerate
You're really getting the hang of using iterators, great job!

You've just gained several new ideas on iterators from the last video and one of them is the enumerate() function. Recall that enumerate() returns an enumerate object that produces a sequence of tuples, and each of the tuples is an index-value pair.

In this exercise, you are given a list of strings mutants and you will practice using enumerate() on it by printing out a list of tuples and unpacking the tuples using a for loop.

Instructions
*Create a list of tuples from mutants and assign the result to mutant_list. Make sure you generate the tuples using enumerate() and turn the result from it into a list using list().
*Complete the first for loop by unpacking the tuples generated by calling enumerate() on mutants. Use index1 for the index and value1 for the value when unpacking the tuple.
*Complete the second for loop similarly as with the first, but this time change the starting index to start from 1 by passing it in as an argument to the start parameter of enumerate(). Use index2 for the index and value2 for the value when unpacking the tuple.
'''
# Create a list of strings: mutants
mutants = ['charles xavier',
            'bobby drake',
            'kurt wagner',
            'max eisenhardt',
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)

'''
Using zip
Another interesting function that you've learned is zip(), which takes any number of iterables and returns a zip object that is an iterator of tuples. If you wanted to print the values of a zip object, you can convert it into a list and then print it. Printing just a zip object will not return the values unless you unpack it first. In this exercise, you will explore this for yourself.

Three lists of strings are pre-loaded: mutants, aliases, and powers. First, you will use list() and zip() on these lists to generate a list of tuples. Then, you will create a zip object using zip(). Finally, you will unpack this zip object in a for loop to print the values in each tuple. Observe the different output generated by printing the list of tuples, then the zip object, and finally, the tuple values in the for loop.

Instructions
*Using zip() with list(), create a list of tuples from the three lists mutants, aliases, and powers (in that order) and assign the result to mutant_data.
*Using zip(), create a zip object called mutant_zip from the three lists mutants, aliases, and powers.
*Complete the for loop by unpacking the zip object you created and printing the tuple values. Use value1, value2, value3 for the values from each of mutants, aliases, and powers, in that order.
'''
# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

'''
Using * and zip to 'unzip'
You know how to use zip() as well as how to print out values from a zip object. Excellent!

Let's play around with zip() a little more. There is no unzip function for doing the reverse of what zip() does. We can, however, reverse what has been zipped together by using zip() with a little help from *! * unpacks an iterable such as a list or a tuple into positional arguments in a function call.

In this exercise, you will use * in a call to zip() to unpack the tuples produced by zip().

Two tuples of strings, mutants and powers have been pre-loaded.

Instructions
*Create a zip object by using zip() on mutants and powers, in that order. Assign the result to z1.
*Print the tuples in z1 by unpacking them into positional arguments using the * operator in a print() call.
*Because the previous print() call would have exhausted the elements in z1, recreate the zip object you defined earlier and assign the result again to z1.
*'Unzip' the tuples in z1 by unpacking them into positional arguments using the * operator in a zip() call. Assign the results to result1 and result2, in that order.
*The last print() statements prints the output of comparing result1 to mutants and result2 to powers. Click Submit Answer to see if the unpacked result1 and result2 are equivalent to mutants and powers, respectively.
'''
# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)

'''
Processing large amounts of Twitter data
Sometimes, the data we have to process reaches a size that is too much for a computer's memory to handle. This is a common problem faced by data scientists. A solution to this is to process an entire data source chunk by chunk, instead of a single go all at once.

In this exercise, you will do just that. You will process a large csv file of Twitter data in the same way that you processed 'tweets.csv' in Bringing it all together exercises of the prequel course, but this time, working on it in chunks of 10 entries at a time.

If you are interested in learning how to access Twitter data so you can work with it on your own system, refer to Part 2 of the DataCamp course on Importing Data in Python.

The pandas package has been imported as pd and the file 'tweets.csv' is in your current directory for your use.

Be aware that this is real data from Twitter and as such there is always a risk that it may contain profanity or other offensive content (in this exercise, and any following exercises that also use real Twitter data).

Instructions
*Initialize an empty dictionary counts_dict for storing the results of processing the Twitter data.
*Iterate over the 'tweets.csv' file by using a for loop. Use the loop variable chunk and iterate over the call to pd.read_csv() with a chunksize of 10.
*In the inner loop, iterate over the column 'lang' in chunk by using a for loop. Use the loop variable entry.
'''
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)

'''
Extracting information for large amounts of Twitter data
Great job chunking out that file in the previous exercise. You now know how to deal with situations where you need to process a very large file and that's a very useful skill to have!

It's good to know how to process a file in smaller, more manageable chunks, but it can become very tedious having to write and rewrite the same code for the same task each time. In this exercise, you will be making your code more reusable by putting your work in the last exercise in a function definition.

The pandas package has been imported as pd and the file 'tweets.csv' is in your current directory for your use.

Instructions
*Define the function count_entries(), which has 3 parameters. The first parameter is csv_file for the filename, the second is c_size for the chunk size, and the last is colname for the column name.
*Iterate over the file in csv_file file by using a for loop. Use the loop variable chunk and iterate over the call to pd.read_csv(), passing c_size to chunksize.
*In the inner loop, iterate over the column given by colname in chunk by using a for loop. Use the loop variable entry.
*Call the count_entries() function by passing to it the filename 'tweets.csv', the size of chunks 10, and the name of the column to count, 'lang'. Assign the result of the call to the variable result_counts.
'''


# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict


# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)
