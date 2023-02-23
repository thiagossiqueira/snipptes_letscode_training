'''
Combining Pokémon names and types
Three lists have been loaded into your session from a dataset that contains 720 Pokémon:

The names list contains the names of each Pokémon.
The primary_types list contains the corresponding primary type of each Pokémon.
The secondary_types list contains the corresponding secondary type of each Pokémon (nan if the Pokémon has only one type).
We want to combine each Pokémon's name and types together so that you easily see a description of each Pokémon. Practice using zip() to accomplish this task.

1)
Combine the names list and the primary_types list into a new list object (called names_type1).
'''
# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

'''
2)
Combine names, primary_types, and secondary_types (in that order) using zip() and unpack the zip object into a new list.
'''
# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')

'''
3)
Use zip() to combine the first five items from the names list and the first three items from the primary_types list.
'''
# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')

'''
Counting Pokémon from a sample
A sample of 500 Pokémon has been generated, and three lists from this sample have been loaded into your session:

The names list contains the names of each Pokémon in the sample.
The primary_types list containing the corresponding primary type of each Pokémon in the sample.
The generations list contains the corresponding generation of each Pokémon in the sample.
You want to quickly gather a few counts from these lists to better understand the sample that was generated. Use Counter from the collections module to explore what types of Pokémon are in your sample, what generations they come from, and how many Pokémon have a name that starts with a specific letter.

Counter has already been imported into your session for convenience.

Instructions
*Collect the count of each primary type from the sample.
*Collect the count of each generation from the sample.
*Use list comprehension to collect the first letter of each Pokémon in the names list. Save this as starting_letters.
*Collect the count of starting letters from the starting_letters list. Save this as starting_letters_count.
'''
# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

'''
Combinations of Pokémon
Ash, a Pokémon trainer, encounters a group of five Pokémon. These Pokémon have been loaded into a list within your session (called pokemon) and printed into the console for your convenience.

Ash would like to try to catch some of these Pokémon, but his Pokédex can only store two Pokémon at a time. Let's use combinations from the itertools module to see what the possible pairs of Pokémon are that Ash could catch.

Instructions
*Import combinations from itertools.
*Create a combinations object called combos_obj that contains all possible pairs of Pokémon from the pokemon list. A pair has 2 Pokémon.
*Unpack combos_obj into a list called combos_2.
*Ash upgraded his Pokédex so that it can now store four Pokémon. Use combinations to collect all possible combinations of 4 different Pokémon. Save these combinations directly into a list called combos_4 using the star character (*).
'''
# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)

'''
Comparing Pokédexes
Two Pokémon trainers, Ash and Misty, would like to compare their individual collections of Pokémon. Let's see what Pokémon they have in common and what Pokémon Ash has that Misty does not.

Both Ash and Misty's Pokédex (their collection of Pokémon) have been loaded into your session as lists called ash_pokedex and misty_pokedex. They have been printed into the console for your convenience.

Instructions
*Convert both lists (ash_pokedex and misty_pokedex) to sets called ash_set and misty_set respectively.
*Find the Pokémon that both Ash and Misty have in common using a set method.
*Find the Pokémon that are within Ash's Pokédex but are not within Misty's Pokédex with a set method.
*Use a set method to find the Pokémon that are unique to either Ash or Misty (i.e., the Pokémon that exist in exactly one of the Pokédexes but not both).
'''
# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has, and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)

'''
Searching for Pokémon
Two Pokémon trainers, Ash and Brock, have a collection of ten Pokémon each. Each trainer's Pokédex (their collection of Pokémon) has been loaded into your session as lists called ash_pokedex and brock_pokedex respectively.

You'd like to see if certain Pokémon are members of either Ash or Brock's Pokédex.

Let's compare using a set versus using a list when performing this membership testing.

1)
Convert Brock's Pokédex list (brock_pokedex) to a set called brock_pokedex_set.
'''
# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

'''
2)
Check if 'Psyduck' is in Ash's Pokédex list (ash_pokedex) and if 'Psyduck' is in Brock's Pokédex set (brock_pokedex_set).
'''
# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

'''
3)
Check if 'Machop' is in Ash's Pokédex list (ash_pokedex) and if 'Machop' is in Brock's Pokédex set (brock_pokedex_set).
'''
# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

'''
4)
Question
Within your IPython console, use %timeit to compare membership testing for 'Psyduck' in ash_pokedex, 'Psyduck' in brock_pokedex_set, 'Machop' in ash_pokedex, and 'Machop' in brock_pokedex_set (a total of four different timings).

Don't include the print() function. Only time the commands that you wrote inside the print() function in the previous steps.

Which membership testing was faster?

%timeit 'Psyduck' in ash_pokedex
%timeit 'Psyduck' in brock_pokedex_set
%timeit 'Machop' in ash_pokedex
%timeit 'Machop' in brock_pokedex_set

output:
228 ns +- 41.9 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each)
36.5 ns +- 4.96 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)
226 ns +- 36 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each)
37.8 ns +- 5.41 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

Answer:
Member testing using a set is faster than using a list in all four cases.
'''

'''
Gathering unique Pokémon
A sample of 500 Pokémon has been created with replacement (meaning a Pokémon could be selected more than once and duplicates exist within the sample).

Three lists have been loaded into your session:

*The names list contains the names of each Pokémon in the sample.
*The primary_types list containing the corresponding primary type of each Pokémon in the sample.
*The generations list contains the corresponding generation of each Pokémon in the sample.
*The below function was written to gather unique values from each list:

def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques
    
Let's compare the above function to using the set data type for collecting unique items.

1)
Use the provided function to collect the unique Pokémon in the names list. Save this as uniq_names_func.
'''
# Use the provided function to collect unique Pokémon names
uniq_names_func = set(names)
print(len(uniq_names_func))

'''
2)
Use a set data type to collect the unique Pokémon in the names list. Save this as uniq_names_set.
'''
# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

'''
3)
Question
Within your IPython console, use %timeit to compare the find_unique_items() function with using a set data type to collect unique Pokémon character names in names.

Which membership testing was faster?

%timeit find_unique_items(names)
%timeit set(names)

Answer:
Using a set to collect unique values is faster.
'''

'''
4)
Use the most efficient approach for gathering unique items to collect the unique Pokémon types (from the primary_types list) and Pokémon generations (from the generations list).
'''
# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n')

'''
Gathering Pokémon without a loop
A list containing 720 Pokémon has been loaded into your session as poke_names. Another list containing each Pokémon's corresponding generation has been loaded as poke_gens.

A for loop has been created to filter the Pokémon that belong to generation one or two, and collect the number of letters in each Pokémon's name:

gen1_gen2_name_lengths_loop = []

for name,gen in zip(poke_names, poke_gens):
    if gen < 3:
        name_length = len(name)
        poke_tuple = (name, name_length)
        gen1_gen2_name_lengths_loop.append(poke_tuple)

Instructions
*Eliminate the above for loop using list comprehension and the map() function:

    *Use list comprehension to collect each Pokémon that belongs to generation 1 or generation 2. Save this as gen1_gen2_pokemon.
    *Use the map() function to collect the number of letters in each Pokémon's name within the gen1_gen2_pokemon list. Save this map object as name_lengths_map.
    *Combine gen1_gen2_pokemon and name_length_map into a list called gen1_gen2_name_lengths.
'''
# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = [*map(len, poke_names)]

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(poke_names, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

'''
Pokémon totals and averages without a loop
A list of 720 Pokémon has been loaded into your session called names. Each Pokémon's corresponding statistics has been loaded as a NumPy array called stats. Each row of stats corresponds to a Pokémon in names and each column represents an individual Pokémon stat (HP, Attack, Defense, Special Attack, Special Defense, and Speed respectively.)

You want to gather each Pokémon's total stat value (i.e., the sum of each row in stats) and each Pokémon's average stat value (i.e., the mean of each row in stats) so that you find the strongest Pokémon.

The below for loop was written to collect these values:

poke_list = []

for pokemon,row in zip(names, stats):
    total_stats = np.sum(row)
    avg_stats = np.mean(row)
    poke_list.append((pokemon, total_stats, avg_stats))

Instructions
*Replace the above for loop using NumPy:
    *Create a total stats array (total_stats_np) using the .sum() method and specifying the correct axis.
    *Create an average stats array (avg_stats_np) using the .mean() method and specifying the correct axis.
    *Create a final output list (poke_list_np) by combining the names list, the total_stats_np array, and the avg_stats_np array.
'''
# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

'''
One-time calculation loop
A list of integers that represents each Pokémon's generation has been loaded into your session called generations. You'd like to gather the counts of each generation and determine what percentage each generation accounts for out of the total count of integers.

The below loop was written to accomplish this task:

for gen,count in gen_counts.items():
    total_count = len(generations)
    gen_percent = round(count / total_count * 100, 2)
    print(
      'generation {}: count = {:3} percentage = {}'
      .format(gen, count, gen_percent)
    )
Let's make this loop more efficient by moving a one-time calculation outside the loop.

Instructions
*Import Counter from the collections module.
*Use Counter() to collect the count of each generation from the generations list. Save this as gen_counts.
*Write a better for loop that places a one-time calculation outside (above) the loop. Use the exact same syntax as the original for loop (simply copy and paste the one-time calculation above the loop).
'''
# Import Counter
from collections import Counter

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))

'''
Holistic conversion loop
A list of all possible Pokémon types has been loaded into your session as pokemon_types. It's been printed in the console for convenience.

You'd like to gather all the possible pairs of Pokémon types. You want to store each of these pairs in an individual list with an enumerated index as the first element of each list. This allows you to see the total number of possible pairs and provides an indexed label for each pair.

The below loop was written to accomplish this task:

enumerated_pairs = []

for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_pair_list = list(enumerated_pair_tuple)
    enumerated_pairs.append(enumerated_pair_list)
    
Let's make this loop more efficient using a holistic conversion.

Instructions
*combinations from the itertools module has been loaded into your session. Use it to create a list called possible_pairs that contains all possible pairs of Pokémon types (each pair has 2 Pokémon types).
*Create an empty list called enumerated_tuples above the for loop.
*Within the for loop, append each enumerated_pair_tuple to the empty list you created in the above step.
*Use a built-in function to convert each tuple in enumerated_tuples to a list.
'''
# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

# Append each enumerated_pair_tuple to the empty list above
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)

'''
Bringing it all together: Pokémon z-scores
A list of 720 Pokémon has been loaded into your session as names. Each Pokémon's corresponding Health Points is stored in a NumPy array called hps. You want to analyze the Health Points using the z-score to see how many standard deviations each Pokémon's HP is from the mean of all HPs.

The below code was written to calculate the HP z-score for each Pokémon and gather the Pokémon with the highest HPs based on their z-scores:

poke_zscores = []

for name,hp in zip(names, hps):
    hp_avg = hps.mean()
    hp_std = hps.std()
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))
    
    
highest_hp_pokemon = []

for name,hp,zscore in poke_zscores:
    if zscore > 2:
        highest_hp_pokemon.append((name, hp, zscore))

1)
Use NumPy to eliminate the for loop used to create the z-scores.
Then, combine the names, hps, and z_scores objects together into a list called poke_zscores2.
'''
# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

'''
2)
Use list comprehension to replace the for loop used to collect Pokémon with the highest HPs based on their z-score.
'''
# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name,hp,zscore) for name,hp,zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')

'''
3)
Question
Use %%timeit (cell magic mode) within your IPython console to compare the runtimes between the original code blocks and the new code you developed using NumPy and list comprehension.

Don't include the print() statements when timing. You should include ten lines of code when timing the original code blocks and five lines of code when timing the new code you developed. You may need to press SHIFT+ENTER after entering %%timeit to get to a new line within your IPython console.

Which approach was the faster?

Answer:
The total time for executing the updated solution using NumPy and list comprehension was faster.
'''