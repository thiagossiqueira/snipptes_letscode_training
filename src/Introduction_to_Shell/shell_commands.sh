#Manipulating files and directories
pwd # To find out where you are in the filesystem, run the command pwd (short for "print working directory"). This prints the absolute path of your current working directory
ls # To find out what's there, type ls (which is short for "listing").  For example, ls /home/repl shows you what's in your starting directory (usually called your home directory).
cd # Just as you can move around in a file browser by double-clicking on folders, you can move around in the filesystem using the command cd (which stands for "change directory").
cd .. # moves you up to parent folder
ls ~ # will always list the contents of your home directory
cd ~ # will always take you home.  (the tilde character '~'), which means "your home directory"
cp # cp original.txt duplicate.txt >> creates a copy of original.txt called duplicate.txt. If there already was a file called duplicate.txt, it is overwritten.
mv # "mv autumn.csv winter.csv .." >> moves the files autumn.csv and winter.csv from the current working directory up one level to its parent directory (because .. always refers to the directory above your current location).
mv # used to rename files. If you run: "mv course.txt old-course.txt"  then the file course.txt in the current working directory is "moved" to the file old-course.txt. This is different from the way file browsers work, but is often handy.
rm # to delete files, we use rm, which stands for "remove". "rm thesis.txt backup/thesis-2017-08.txt" >> removes both thesis.txt and backup/thesis-2017-08.txt
rmdir # deleting an entire directory. it only works when the directory is empty
mkdir # to create a new (empty) directory
cat # prints the contents of files onto the screen. (Its name is short for "concatenate", meaning "to link things together", since it will print all the files whose names you give it, one after the other.
less # When you less a file, one page is displayed at a time;
q # you can press spacebar to page down or type q to quit.
:n # you can type :n (colon and a lower-case 'n') to move to the next file,
:p # to go back to the previous one, or
:q # to quit.
head # prints the first few lines of a file (where "a few" means 10)
head -n 100 # display the first 100 (assuming there are that many), and so on.
ls -R # list everything below a directory. the flag -R (which means "recursive"). This shows every file and directory in the current level, then everything in each sub-directory, and so on.
ls -F # prints a / after the name of every directory
ls * # prints the name of every runnable program
ls -R -F # Run ls with the two flags, -R and -F, and the absolute path to your home directory to see everything it contains. (The order of the flags doesn't matter, but the directory name must come last.)
man # help for a command (short for "manual").  For example, the command "man head"
cut -f 2-5,8 -d , values.csv # to select columns, you can use the command cut. It has several options (use man cut to explore them). "cut -f 2-5,8 -d , values.csv" means "select columns 2 through 5 and columns 8, using comma as the separator". cut uses -f (meaning "fields") to specify columns and -d (meaning "delimiter") to specify the separator. You need to specify the latter because some files may use spaces, tabs, or colons to separate columns.
cut -d , -f 1 seasonal/spring.csv # will select the first column (containing dates) from the file spring.csv
history # repeat command. It will print a list of commands you have run recently. Each one is preceded by a serial number to make it easy to re-run particular commands: just type !55 to re-run the 55th command in your history (if you have that many). You can also re-run a command by typing an exclamation mark followed by the command's name, such as !head or !cut, which will re-run the most recent use of that command.
grep bicuspid seasonal/winter.csv # prints lines from winter.csv that contain "bicuspid".
grep -c # print a count of matching lines rather than the lines themselves
grep -h # do not print the names of files when searching multiple files
grep -i # ignore case (e.g., treat "Regression" and "regression" as matches)
grep -l # print the names of files that contain matches, not the matches
grep -n # print line numbers for matching lines
grep -v # invert the match, i.e., only show lines that don't match
grep -v -n molar seasonal/spring.csv # exclude the lines containaing 'molar' (-v) and add an index (-n)
grep incisor -c seasonal/autumn.csv seasonal/winter.csv # Count how many lines contain the word incisor in autumn.csv and winter.csv combined.
head -n 5 seasonal/summer.csv > top.csv # store a command's output in a file. head's output is put in a new file called top.csv >> The greater-than sign > tells the shell to redirect head's output to a file. It isn't part of the head command; instead, it works with every shell command that produces output.
tail -n 5 seasonal/winter.csv > last.csv # store the last 5 lines of winter.csv into a file called last.csv
head -n 5 seasonal/summer.csv | tail -n 3 # combine commands >> The pipe symbol tells the shell to use the output of the command on the left as the input to the command on the right. The pipe symbol tells the shell to use the output of the command on the left as the input to the command on the right.
cut -f 2 -d , seasonal/summer.csv | grep -v Tooth # selecione a coluna 2, delimitada por ",". Depois exclude the lines containaing 'Tooth' (-v)
cut -d , -f 1 seasonal/spring.csv | grep -v Date | head -n 10 #  combine many commands: 1) select the first column from the spring data; 2) remove the header line containing the word "Date"; and 3) select the first 10 lines of actual data.
grep 2017-07 seasonal/spring.csv | wc -l # count how many records in the file spring.csv have dates in 2017-07: the command wc (short for "word count") prints the number of characters, words, and lines in a file. You can make it print only one of these using -c, -w, or -l respectively.
cut -d , -f 1 seasonal/winter.csv seasonal/spring.csv seasonal/summer.csv seasonal/autumn.csv # specify many files at once
#alternatively to above sentence because typing the names of many files over and over is a bad idea: it wastes time, and sooner or later you will either leave a file out or repeat a file's name. To make your life better, the shell allows you to use wildcards to specify a list of files with a single expression. The most common wildcard is *, which means "match zero or more characters". Using it, we can shorten the cut command above to this:
cut -d , -f 1 seasonal/* # specify many files at once
cut -d , -f 1 seasonal/*.csv # specify many files at once
#Wildcards:
#1)  '*' matches everything within a folder
#2)  '?' matches a single character, so 201?.txt will match 2017.txt or 2018.txt, but not 2017-01.txt.
#3)  '[...]' matches any one of the characters inside the square brackets, so 201[78].txt matches 2017.txt or 2018.txt, but not 2016.txt.
#4)  '{...}' matches any of the comma-separated patterns inside the curly brackets, so {*.txt, *.csv} matches any file whose name ends with .txt or .csv, but not files whose names end with .pdf.
#5)  '{singh.pdf, j*.txt}' matches singh.pdf and johel.txt
#  sort lines of text >> 'sort' puts data in order. By default it does this in ascending alphabetical order, but the flags '-n' and '-r' can be used to sort numerically and reverse the order of its output, while '-b' tells it to ignore leading blanks and '-f' tells it to fold case (i.e., be case-insensitive). Pipelines often use 'grep' to get rid of unwanted records and then 'sort' to put the remaining records in order.
cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort # sort ascending order the second column of the winter file, disconsidering the line 'Tooth'
cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort -r # sort reverse order the second column of the winter file, disconsidering the line 'Tooth'
cut -f 2 -d , seasonal/winter.csv | grep -v Tooth | sort | uniq -c # remove duplicate lines: Another command that is often used with 'sort' is 'uniq', whose job is to remove duplicated lines. More specifically, it removes adjacent duplicated lines.
cut -d , -f 2 seasonal/*.csv | grep -v Tooth > teeth-only.txt #  save the output of a pipe
> result.txt head -n 3 seasonal/winter.csv # The command's output is redirected to the file as usual.
Ctrl + C # stop a running program
cat seasonal/*.csv | wc -l # list the number of lines in all seasonal data files
wc -l seasonal/*.csv # list individual and total the number of lines in all seasonal data files
# list the number of lines in all seasonal data files
wc -l seasonal/*.csv | grep -v total # same as above but remove the label 'total'
wc -l seasonal/*.csv | grep -v total | sort -n | head -n 1 # find the file containing the fewest lines
set # get a complete list of variables >> how does shell store information ? >> Like other programs, the shell stores information in variables. Some of these, called environment variables, are available all the time. Environment variables' names are conventionally written in upper case, and a few of the more commonly-used ones are shown below. >> Variables: HOME, PWD, SHELL, USER
set | grep HISTFILESIZE # how many old commands are stored in your command history
echo # print a variable's value >> This is true everywhere: to get the value of a variable called X, you must write $X. (This is so that the shell can tell whether you mean "a file named X" or "the value of a variable named X".)
echo USER! # prints 'USER!'
echo $USER # prints 'tsiqueira4' >> To get the variable's value, you must put a dollar sign $ in front of it.
echo $OSTYPE # prints 'linux-gnu' >> The variable OSTYPE holds the name of the kind of operating system you are using.
training=seasonal/summer.csv # To create a shell variable
echo $training # check the variable's value
head -n 1 $training # get the first line of seasonal/summer.csv
for filetype in gif jpg png; do echo $filetype; done # repeat commands many times.
for filename in seasonal/*.csv; do echo $filetype; done # print all files within a folder
clear # clear the screen
files=seasonal/*.csv # create a variable
for f in $files; do echo $f; done # output the values within the variable
for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done # run many commands in a single loop
for file in seasonal/*.csv; do grep 2017-07 $file |tail -n 1; done #output the last line containing 2017-07 for each file in the folders
mv 'July 2017.csv' '2017 July data.csv' # remame files >>  have to quote the files' names so that the shell treats each one as a single parameter:
for f in seasonal/*.csv; do echo $f; head -n 2 $f | tail -n 1; done # do many things in a single loop >> The loops you have seen so far all have a single command or pipeline in their body, but a loop can contain any number of commands. To tell the shell where one ends and the next begins, you must separate them with semi-colons
nano filename # edit a file >> Unix has a bewildering variety of text editors. For this course, we will use a simple one called Nano. If you type nano filename, it will open filename for editing (or create it if it doesn't already exist). You can move around with the arrow keys, delete characters using backspace, and do other operations with control-key combinations:
Ctrl + K # delete a line.
Ctrl + U # un-delete a line.
Ctrl + O # save the file ('O' stands for 'output'). You will also need to press Enter to confirm the filename!
Ctrl + X # exit the editor.
cp seasonal/s* ~ # Copy the files starting with "s" from the seasonal folder (seasonal/spring.csv and seasonal/summer.csv) to your home directory "~".
grep -h -v Tooth spring.csv summer.csv > temp.csv # Use grep with the -h flag (to stop it from printing filenames) and -v Tooth (to select lines that don't match the header line) to select the data records from spring.csv and summer.csv in that order and redirect the output to temp.csv.
history | tail -n 3 > steps.txt # Save the last 3 commands in the file 'steps.txt'
head -n 1 seasonal/*.csv > headers.sh # save commands to re-run later >>  since the commands you type in are just text, you can store them in files for the shell to run over and over again.
head -n 1 seasonal/*.csv # selects the first row from each of the CSV files in the seasonal directory. Once you have created this file
bash headers.sh # This tells the shell (which is just a program called bash) to run the commands contained in the file headers.sh, which produces the same output as running the commands directly.
nano dates.sh # Used to create a file called dates.sh that contains this command:
cut -d , -f 1 seasonal/*.csv # to extract the first column from all of the CSV files in seasonal.
bash dates.sh # used to run the command saved in the file
# if all-dates.sh contains this line:
cut -d , -f 1 seasonal/*.csv | grep -v Date | sort | uniq # re-use pipes >> A file full of shell commands is called a *shell script, or sometimes just a "script" for short. Scripts don't have to have names ending in .sh, but this lesson will use that convention to help you keep track of which files are scripts.
#then:
bash all-dates.sh > dates.out # will extract the unique dates from the seasonal data files and save them in dates.out.
cut -d , -f 2 seasonal/*.csv | grep -v Tooth | sort | uniq -c # prints a count of the number of times each tooth name appears in the CSV files in the seasonal directory.
#if unique-lines.sh contains sort $@ | uniq (eg. tail -q -n +2 $@ | wc -l), when you run:
bash unique-lines.sh seasonal/summer.csv # the shell replaces $@ with seasonal/summer.csv and processes one file.
cut -d , -f $2 $1 #  As well as $@, the shell lets you use $1, $2, and so on to refer to specific command-line parameters. You can use this to write commands that feel simpler or more natural than the shell's. For example, you can create a script called column.sh that selects a single column from a CSV file when the user provides the filename as the first parameter and the column as the second
bash column.sh seasonal/autumn.csv 1 # Notice how the script uses the two parameters in reverse order.
#How can I write loops in a shell script?
"""
# Print the first and last data records of each file.
for filename in $@
do
    head -n 2 $filename | tail -n 1
    tail -n 1 $filename
done
"""

