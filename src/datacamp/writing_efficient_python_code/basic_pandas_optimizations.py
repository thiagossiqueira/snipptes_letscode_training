'''
Iterating with .iterrows()
In the video, we discussed that .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs. But, what does this mean? Let's explore with a few coding exercises.

A pandas DataFrame has been loaded into your session called pit_df. This DataFrame contains the stats for the Major League Baseball team named the Pittsburgh Pirates (abbreviated as 'PIT') from the year 2008 to the year 2012. It has been printed into your console for convenience.

1)
Use .iterrows() to loop over pit_df and print each row. Save the first item from .iterrows() as i and the second as row.
'''
# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)

'''
2)
Add two lines to the loop: one before print(row) to print each index variable and one after to print each row's type.
'''
# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))

'''
3)
Instead of using i and row in the for statement to store the output of .iterrows(), use one variable named row_tuple.
'''
# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)

'''
4)
Add a line in the for loop to print the type of each row_tuple.
'''
# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))

'''
un differentials with .iterrows()
You've been hired by the San Francisco Giants as an analyst—congrats! The team's owner wants you to calculate a metric called the run differential for each season from the year 2008 to 2012. This metric is calculated by subtracting the total number of runs a team allowed in a season from the team's total number of runs scored in a season. 'RS' means runs scored and 'RA' means runs allowed.

The below function calculates this metric:

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

A DataFrame has been loaded into your session as giants_df and printed into the console. Let's practice using .iterrows() to add a run differential column to this DataFrame.

1)
Create an empty list called run_diffs that will be used to store the run differentials you will calculate.
'''
# Create an empty list to store run differentials
run_diffs = []

'''
2)
Write a for loop that uses .iterrows() to loop over giants_df and collects each row's runs scored and runs allowed.
'''
# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i, row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']

'''
3)
Add a line to the for loop that uses the provided function to calculate each row's run differential.
'''
# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']

    # Use the provided function to calculate run_diff for each row
    run_diff = runs_scored - runs_allowed

'''
4)
Add a line to the loop that appends each row's run differential to the run_diffs list.
'''
# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']

    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)

    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)

'''
Iterating with .itertuples()
Remember, .itertuples() returns each DataFrame row as a special data type called a namedtuple. You can look up an attribute within a namedtuple with a special syntax. Let's practice working with namedtuples.

A pandas DataFrame has been loaded into your session called rangers_df. This DataFrame contains the stats ('Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', and 'Playoffs') for the Major League baseball team named the Texas Rangers (abbreviated as 'TEX').

1)
Use .itertuples() to loop over rangers_df and print each row.
'''
# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
  print(row)

'''
2)
Loop over rangers_df with .itertuples() and save each row's Index, Year, and Wins (W) attribute as i, year, and wins.
'''
# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  print(i, year, wins)

'''
3)
Now, loop over rangers_df and print these values only for those rows where the Rangers made the playoffs.
'''
# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W

  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)

'''
Run differentials with .itertuples()
The New York Yankees have made a trade with the San Francisco Giants for your analyst contract— you're a hot commodity! Your new boss has seen your work with the Giants and now wants you to do something similar with the Yankees data. He'd like you to calculate run differentials for the Yankees from the year 1962 to the year 2012 and find which season they had the best run differential.

You've remembered the function you used when working with the Giants and quickly write it down:

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

Let's use .itertuples() to loop over the yankees_df DataFrame (which has been loaded into your session) and calculate run differentials.

1)
Use .itertuples() to loop over yankees_df and grab each row's runs scored and runs allowed values.
'''
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():

    runs_scored = row.RS
    runs_allowed = row.RA

'''
2)
Now, calculate each row's run differential using calc_run_diff(). Be sure to append each row's run differential to run_diffs.
'''
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():

    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)

    run_diffs.append(run_diff)

'''
3)
Append a new column called 'RD' to the yankees_df DataFrame that contains the run differentials you calculated.
'''
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():

    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)

    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

'''
4)
Question
In what year within your DataFrame did the New York Yankees have the highest run differential?
You'll need to rerun the code that creates the 'RD' column if you'd like to analyze the DataFrame with code rather than looking at the console output.

Possible Answers
In 1998 (with a Run Differential of 309)
'''

'''
Analyzing baseball stats with .apply()
The Tampa Bay Rays want you to analyze their data.

They'd like the following metrics:

*The sum of each column in the data
*The total amount of runs scored in a year ('RS' + 'RA' for each year)
*The 'Playoffs' column in text format rather than using 1's and 0's

The below function can be used to convert the 'Playoffs' column to text:

def text_playoffs(num_playoffs): 
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No' 

Use .apply() to get these metrics. A DataFrame (rays_df) has been loaded and printed to the console. This DataFrame is indexed on the 'Year' column.

1)
Apply sum() to each column of rays_df to collect the sum of each column. Be sure to specify the correct axis.
'''
# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

'''
2)
Apply sum() to each row of rays_df, only looking at the 'RS' and 'RA' columns, and specify the correct axis.
'''
# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

'''
3)
Use .apply() and a lambda function to apply text_playoffs() to each row's 'Playoffs' value of the rays_df DataFrame.
'''
# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

'''
Settle a debate with .apply()
Word has gotten to the Arizona Diamondbacks about your awesome analytics skills. They'd like for you to help settle a debate amongst the managers. One manager claims that the team has made the playoffs every year they have had a win percentage of 0.50 or greater. Another manager says this is not true.

Let's use the below function and the .apply() method to see which manager is correct.

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

A DataFrame named dbacks_df has been loaded into your session.

1)
Print the first five rows of the dbacks_df DataFrame to see what the data looks like.
'''
# Display the first five rows of the DataFrame
print(dbacks_df.head())

'''
2)
Create a pandas Series called win_percs by applying the calc_win_perc() function to each row of the DataFrame with a lambda function.
'''

# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

'''
3)
Create a new column in dbacks_df called WP that contains the win percentages you calculated in the above step.
'''
# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])

'''
4)
Question
Which manager was correct in their claim?

Answer:
The manager who claimed the team has not made the playoffs every year they've had a win percentage of 0.50 or greater.
'''

'''
Replacing .iloc with underlying arrays
Now that you have a better grasp on a DataFrame's internals let's update one of your previous analyses to leverage a DataFrame's underlying arrays. You'll revisit the win percentage calculations you performed row by row with the .iloc method:

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list

Let's update this analysis to use arrays instead of the .iloc method. A DataFrame (baseball_df) has been loaded into your session.

1)
Use the right method to collect the underlying 'W' and 'G' arrays of baseball_df and pass them directly into the calc_win_perc() function. Store the result as a variable called win_percs_np.
'''
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

'''
2)
Create a new column in baseball_df called 'WP' that contains the win percentages you just calculated.
'''
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

'''
3)
Question
Use timeit in cell magic mode within your IPython console to compare the runtimes between the old code block using .iloc and the new code you developed using NumPy arrays.

Don't include the code that defines the calc_win_perc() function or the print() statements or when timing.

You should include eight lines of code when timing the old code block and two lines of code when timing the new code you developed. You may need to press SHIFT+ENTER when using timeit in cell magic mode to get to a new line within your IPython console.

Which approach was the faster?

Answer:
The NumPy array approach is faster than the .iloc approach.
'''

'''
Bringing it all together: Predict win percentage
A pandas DataFrame (baseball_df) has been loaded into your session. For convenience, a dictionary describing each column within baseball_df has been printed into your console. You can reference these descriptions throughout the exercise.

You'd like to attempt to predict a team's win percentage for a given season by using the team's total runs scored in a season ('RS') and total runs allowed in a season ('RA') with the following function:

def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

Let's compare the approaches you've learned to calculate a predicted win percentage for each season (or row) in your DataFrame.

1)
Use a for loop and .itertuples() to predict the win percentage for each row of baseball_df with the predict_win_perc() function. Save each row's predicted win percentage as win_perc_pred and append each to the win_perc_preds_loop list.
'''
win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

'''
2)
Apply predict_win_perc() to each row of the baseball_df DataFrame using a lambda function. Save the predicted win percentage as win_perc_preds_apply.
'''
win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

'''
3)
Calculate the predicted win percentages by passing the underlying 'RS' and 'RA' arrays from baseball_df into predict_win_perc(). Save these predictions as win_perc_preds_np.
'''
win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())

'''
4)
Question
Compare runtimes within your IPython console between all three approaches used to calculate the predicted win percentages.

Use %%timeit (cell magic mode) to time the six lines of code (not including comment lines) for the .itertuples() approach. You may need to press SHIFT+ENTER after entering %%timeit to get to a new line within your IPython console.

Use %timeit (line magic mode) to time the .apply() approach and the NumPy array approach separately. Each has only one line of code (not including comment lines).

What is the order of approaches from fastest to slowest?

Answer:
Using NumPy arrays was the fastest approach, followed by the .itertuples() approach, and the .apply() approach was slowest.
'''