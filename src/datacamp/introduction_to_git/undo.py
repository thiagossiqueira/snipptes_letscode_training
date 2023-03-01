'''
How can I commit changes selectively?
You don't have to put all of the changes you have made recently into the staging area at once. For example, suppose you are adding a feature to analysis.R and spot a bug in cleanup.R. After you have fixed it, you want to save your work. Since the changes to cleanup.R aren't directly related to the work you're doing in analysis.R, you should save your work in two separate commits.

The syntax for staging a single file is git add path/to/file.

If you make a mistake and accidentally stage a file you shouldn't have, you can unstage the additions with git reset HEAD and try again.

1)
From the output of git status on the right, you'll see that two files were changed; data/northern.csv and data/eastern.csv. Stage only the changes made to data/northern.csv.
'''
# git add data/northrn.csv

'''
2)
Commit those changes with the message "Adding data from northern region."
'''
# git commit -m "Adding data from northern region"

'''
How do I re-stage files?
People often save their work every few minutes when they're using a desktop text editor. Similarly, it's common to use git add periodically to save the most recent changes to a file to the staging area. This is particularly useful when the changes are experimental and you might want to undo them without cluttering up the repository's history.

1)
You are in the dental repository. Use git status to check the status of the repository.
'''
# git status

'''
2)
It appears that some changes to data/northern.csv have already been staged, but there are new changes that haven't been staged yet. Use git add to stage these latest changes to data/northern.csv again.
'''
# git add data/northrn.csv

'''
How can I undo changes to unstaged files?
Suppose you have made changes to a file, then decide you want to undo them. Your text editor may be able to do this, but a more reliable way is to let Git do the work. The command:

    git checkout -- filename

will discard the changes that have not yet been staged. (The double dash -- must be there to separate the git checkout command from the names of the file or files you want to recover.)

Use this command carefully: once you discard changes in this way, they are gone forever.

Instructions
*You are in the dental repository, where all changes to .csv files in data were staged. git status shows that data/northern.csv was changed again after it was staged. Use a Git command to undo the changes to the file data/northern.csv.
'''
# git checkout -- data/northern.csv

'''
How can I undo changes to staged files?
At the start of this chapter you saw that git reset will unstage files that you previously staged using git add. By combining git reset with git checkout, you can undo changes to a file that you staged changes to. The syntax is as follows.

    git reset HEAD path/to/file
    git checkout -- path/to/file

(You may be wondering why there are two commands for re-setting changes. The answer is that unstaging a file and undoing changes are both special cases of more powerful Git operations that you have not yet seen.)

1)
Use git reset to unstage the file data/northern.csv (and only that file).
'''
# git reset data/northern.csv

'''
2)
Use git checkout -- to undo the changes since the last commit for data/northern.csv.
'''
# git checkout data/northern.csv

'''
How do I restore an old version of a file?
You previously saw how to use git checkout to undo the changes that you made since the last commit. This command can also be used to go back even further into a file's history and restore versions of that file from a commit. In this way, you can think of committing as saving your work, and checking out as loading that saved version.

The syntax for restoring an old version takes two arguments: the hash that identifies the version you want to restore, and the name of the file.

For example, if git log shows this:
    
    commit ab8883e8a6bfa873d44616a0f356125dbaccd9ea
    Author: Author: Rep Loop <repl@datacamp.com>
    Date:   Thu Oct 19 09:37:48 2017 -0400
    
        Adding graph to show latest quarterly results.
    
    commit 2242bd761bbeafb9fc82e33aa5dad966adfe5409
    Author: Author: Rep Loop <repl@datacamp.com>
    Date:   Thu Oct 16 09:17:37 2017 -0400
    
        Modifying the bibliography format.

then git checkout 2242bd report.txt would replace the current version of report.txt with the version that was committed on October 16. Notice that this is the same syntax that you used to undo the unstaged changes, except -- has been replaced by a hash.

Restoring a file doesn't erase any of the repository's history. Instead, the act of restoring the file is saved as another commit, because you might later want to undo your undoing.

One more thing: there's another feature of git log that will come in handy here. Passing - followed by a number restricts the output to that many commits. For example, git log -3 report.txt shows you the last three commits involving report.txt.

1)
The current contents of data/western.csv are shown in the terminal. Use git log -2 to list the last two changes to that file.
'''
# git log -2 data/western.csv

'''
2)
Use git checkout with the first few characters of a hash to restore the version of data/western.csv that has the commit message "Adding fresh data for southern and western regions.".
'''
# git checkout 29a5981 data/western.csv

'''
3)
Use cat data/western.csv to display the updated contents.
'''
# cata data/western.csv

'''
4)
Commit the restored version of data/western.csv, and be sure to include a message.
'''
# git commit -m "any message"

'''
How can I undo all of the changes I have made?
So far, you have seen how to undo changes to a single file at a time using git reset HEAD path/to/file. You will sometimes want to undo changes to many files.

One way to do this is to give git reset a directory. For example, git reset HEAD data will unstage any files from the data directory. Even better, if you don't provide any files or directories, it will unstage everything. Even even better, HEAD is the default commit to unstage, so you can simply write git reset to unstage everything.

Similarly git checkout -- data will then restore the files in the data directory to their previous state. You can't leave the file argument completely blank, but recall from Introduction to Shell for Data Science that you can refer to the current directory as .. So git checkout -- . will revert all files in the current directory.

1)
Use git reset to remove all files from the staging area.
'''
# git reset

'''
2)
Use git checkout to put those files back in their previous state. Use the directory name . to mean "all of the files in or below this directory", and separate it from the command with --.
'''
# git checkout .
