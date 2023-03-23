'''
What is version control?
A version control system is a tool that manages changes made to the files and directories in a project. Many version control systems exist; this lesson focuses on one called Git, which is used by many of the data science tools covered in our other lessons. Its strengths are:

Nothing that is saved to Git is ever lost, so you can always go back to see which results were generated by which versions of your programs.

Git automatically notifies you when your work conflicts with someone else's, so it's harder (but not impossible) to accidentally overwrite work.

Git can synchronize work done by different people on different machines, so it scales as your team does.

Version control isn't just for software: books, papers, parameter sets, and anything that changes over time or needs to be shared can and should be stored and shared using something like Git.

Which of the following does Git do?

Answer:
1) Keep track of changes to files.
2) Notice conflicts between changes made by different people.
3) Synchronize files between different computers.
[x] 4) All of the above.
'''
'''
Where does Git store information?
Each of your Git projects has two parts: the files and directories that you create and edit directly, and the extra information that Git records about the project's history. The combination of these two things is called a repository.

Git stores all of its extra information in a directory called .git located in the root directory of the repository. Git expects this information to be laid out in a very precise way, so you should never edit or delete anything in .git.

Suppose your home directory /home/repl contains a repository called dental, which has a sub-directory called data. Where is information about the history of the files in /home/repl/dental/data stored?

Answer:
/home/repl/dental/.git
'''

'''
How can I check the state of a repository?
When you are using Git, you will frequently want to check the status of your repository. To do this, run the command git status, which displays a list of the files that have been modified since the last time changes were saved.

You have been put in the dental repository. Use git status to discover which file(s) have been changed since the last save. Which file(s) are listed?

Answer:
report.txt.
'''

'''
How can I tell what I have changed?
Git has a staging area in which it stores files with changes you want to save that haven't been saved yet. Putting files in the staging area is like putting things in a box, while committing those changes is like putting that box in the mail: you can add more things to the box or take things out as often as you want, but once you put it in the mail, you can't make further changes.

Staging Area

git status shows you which files are in this staging area, and which files have changes that haven't yet been put there. In order to compare the file as it currently is to what you last saved, you can use git diff filename. git diff without any filenames will show you all the changes in your repository, while git diff directory will show you the changes to the files in some directory.

Instructions
*You have been put in the dental repository. Use git diff to see what changes have been made to the files.
'''
# git diff

'''
What is in a diff?
A diff is a formatted display of the differences between two sets of files. Git displays diffs like this:

diff --git a/report.txt b/report.txt
index e713b17..4c0742a 100644
--- a/report.txt
+++ b/report.txt
@@ -1,4 +1,5 @@
-# Seasonal Dental Surgeries 2017-18
+# Seasonal Dental Surgeries (2017) 2017-18
+# TODO: write new summary

This shows:

*The command used to produce the output (in this case, diff --git). In it, a and b are placeholders meaning "the first version" and "the second version".
*An index line showing keys into Git's internal database of changes. We will explore these in the next chapter.
*--- a/report.txt and +++ b/report.txt, wherein lines being removed are prefixed with - and lines being added are prefixed with +.
*A line starting with @@ that tells where the changes are being made. The pairs of numbers are start line and number of lines (in that section of the file where changes occurred). This diff output indicates changes starting at line 1, with 5 lines where there were once 4.
*A line-by-line listing of the changes with - showing deletions and + showing additions (we have also configured Git to show deletions in red and additions in green). Lines that haven't changed are sometimes shown before and after the ones that have in order to give context; when they appear, they don't have either + or - in front of them.

Desktop programming tools like RStudio can turn diffs like this into a more readable side-by-side display of changes; you can also use standalone tools like DiffMerge or WinMerge.

You have been put in the dental repository. Use git diff data/northern.csv to look at the changes to that file. How many lines have been added or removed?

git diff data/northern

Answer:
1.
'''

'''
What's the first step in saving changes?
You commit changes to a Git repository in two steps:

1) Add one or more files to the staging area.
2) Commit everything in the staging area.

To add a file to the staging area, use git add filename.

Instructions 
1)
*You have been put in the dental repository. Use git add to add the file report.txt to the staging area.
'''
# git add report.txt

'''
2)
Use another Git command to check the repository's status.
'''
# git status

'''
How can I tell what's going to be committed?
To compare the state of your files with those in the staging area, you can use git diff -r HEAD. The -r flag means "compare to a particular revision", and HEAD is a shortcut meaning "the most recent commit".

You can restrict the results to a single file or directory using git diff -r HEAD path/to/file, where the path to the file is relative to where you are (for example, the path from the root directory of the repository).

We will explore other uses of -r and HEAD in the next chapter.

1)
You have been put in the dental repository, where data/northern.csv has been added to the staging area. Use git diff with -r and an argument to see how files differ from the last saved revision.
'''
# git diff -r HEAD

'''
2)
Use a single Git command to view the changes in the file that has been staged (and only that file).
'''
# git diff -r HEAD data/northern.csv

'''
3)
data/eastern.csv hasn't been added to the staging area yet. Use a Git command to do this now.
'''
# git add data/eastern.csv

'''
Interlude: how can I edit a file?
Unix has a bewildering variety of text editors. In this course, we will sometimes use a very simple one called Nano. If you type nano filename, it will open filename for editing (or create it if it doesn't already exist). You can then move around with the arrow keys, delete characters with the backspace key, and so on. You can also do a few other operations with control-key combinations:

Ctrl-K: delete a line.
Ctrl-U: un-delete a line.
Ctrl-O: save the file ('O' stands for 'output').
Ctrl-X: exit the editor.

Instructions

*Run nano names.txt to edit a new file in your home directory and enter the following four lines:

Lovelace
Hopper
Johnson
Wilson

To save what you have written, type Ctrl-O to write the file out, then Enter to confirm the filename, then Ctrl-X and Enter to exit the editor.
'''
# nano names.txt
# Ctrl-O >> save the file
# Enter >> confirm
# Ctrl-X >> exit

'''
How do I commit changes?
To save the changes in the staging area, you use the command git commit. It always saves everything that is in the staging area as one unit: as you will see later, when you want to undo changes to a project, you undo all of a commit or none of it.

When you commit changes, Git requires you to enter a log message. This serves the same purpose as a comment in a program: it tells the next person to examine the repository why you made a change.

By default, Git launches a text editor to let you write this message. To keep things simple, you can use -m "some message in quotes" on the command line to enter a single-line message like this:

git commit -m "Program appears to have become self-aware."

If you accidentally mistype a commit message, you can change it using the --amend flag.

git commit --amend - m "new message"

1)
*You have been put in the dental repository, and report.txt has been added to the staging area. Use a Git command to check the status of the repository.
'''
# git status

'''
2)
Commit the changes in the staging area with the message "Adding a reference."
'''
# git commit -m "Adding a reference."

'''
How can I view a repository's history?
The command git log is used to view the log of the project's history. Log entries are shown most recent first, and look like this:

commit 0430705487381195993bac9c21512ccfb511056d
Author: Rep Loop <repl@datacamp.com>
Date:   Wed Sep 20 13:42:26 2017 +0000

    Added year to report title.

The commit line displays a unique ID for the commit called a hash; we will explore these further in the next chapter. The other lines tell you who made the change, when, and what log message they wrote for the change.

When you run git log, Git automatically uses a pager to show one screen of output at a time. Press the space bar to go down a page or the 'q' key to quit.

You are in the directory dental, which is a Git repository. Use a single Git command to view the repository's history. What is the message on the very first entry in the log (which is displayed last)?

Keep in mind that not all entries may be visible on the first screen, and that you might need to check additional pages to see the very first entry.


Answer:

"Added summary report file."
'''

'''
How can I view a specific file's history?
A project's entire log can be overwhelming, so it's often useful to inspect only the changes to particular files or directories. You can do this using git log path, where path is the path to a specific file or directory. The log for a file shows changes made to that file; the log for a directory shows when files were added or deleted in that directory, rather than when the contents of the directory's files were changed.

You have been put in the dental repository. Use git log to display only the changes made to data/southern.csv. How many have there been?

git log data/southrn.txt
Answer:
2.
'''

'''
How do I write a better log message
Writing a one-line log message with git commit -m "message"is good enough for very small changes, but your collaborators (including your future self) will appreciate more information. If you run git commit without -m "message", Git launches a text editor with a template like this:

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Your branch is up-to-date with 'origin/master'.
#
# Changes to be committed:
#       modified:   skynet.R
#

The lines starting with # are comments, and won't be saved. (They are there to remind you what you are supposed to do and what files you have changed.) Your message should go at the top, and may be as long and as detailed as you want.

Instructions
*You have been put in the dental repository, and report.txt has been added to the staging area. The changes to report.txt have already been staged. Use git commit without -m to commit the changes. The Nano editor will open up. Write a meaningful message and use Ctrl+O and Enter to save, and then Ctrl+X to leave the editor.
'''
# git commit