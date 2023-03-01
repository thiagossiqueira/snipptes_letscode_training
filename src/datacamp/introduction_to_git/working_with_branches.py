'''
What is a branch?
If you don't use version control, a common workflow is to create different subdirectories to hold different versions of your project in different states, for example development and final. Of course, then you always end up with final-updated and final-updated-revised as well. The problem with this is that it becomes difficult to work out if you have the right version of each file in the right subdirectory, and you risk losing work.

One of the reasons Git is popular is its support for creating branches, which allows you to have multiple versions of your work, and lets you track each version systematically.

Each branch is like a parallel universe: changes you make in one branch do not affect other branches (until you merge them back together).

Note: Chapter 2 described the three-part data structure Git uses to record a repository's history: blobs for files, trees for the saved states of the repositories, and commits to record the changes. Branches are the reason Git needs both trees and commits: a commit will have two parents when branches are being merged.

In the diagram below, each box is a commit and the arrows point to the next ("child") commit. How many merges have taken place?

Answer:
2
'''

'''
How can I see what branches my repository has?
By default, every Git repository has a branch called master (which is why you have been seeing that word in Git's output in previous lessons). To list all of the branches in a repository, you can run the command git branch. The branch you are currently in will be shown with a * beside its name.

You are in the dental repository. How many branches are in this repository (including master)?

git branch
Answer:
3.
'''

'''
How can I view the differences between branches?
Branches and revisions are closely connected, and commands that work on the latter usually work on the former. For example, just as git diff revision-1..revision-2 shows the difference between two versions of a repository, git diff branch-1..branch-2 shows the difference between two branches.

You are in the dental repository. How many files in the summary-statistics branch are different from their equivalents in the master branch?

git diff master..summary-statistics
Answer:
3.
'''

'''
How can I switch from one branch to another?
You previously used git checkout with a commit hash to switch the repository state to that hash. You can also use git checkout with the name of a branch to switch to that branch.

Two notes:
    
    1)When you run git branch, it puts a * beside the name of the branch you are currently in.
    2)Git will only let you do this if all of your changes have been committed. You can get around this, but it is outside the scope of this course.

In this exercise, you'll also make use of git rm. This removes the file (just like the shell command rm) then stages the removal of that file with git add, all in one step.

1)
You are in the master branch of the dental repository. Switch to the summary-statistics branch.
'''
# git checkout summary-statistics

'''
2)
Use git rm to delete report.txt.
'''
# git rm report.txt

'''
3)
Commit your change with `-m "Removing report" as a message.
'''
# git commit -m "Removing report"

'''
4)
Use ls to check that it's gone.
'''
# ls

'''
5)
Switch back to the master branch.
'''
# git checkout master

'''
6)
Use ls to ensure that report.txt is still there.
'''
# ls

'''
How can I create a branch?
You might expect that you would use git branch to create a branch, and indeed this is possible. However, the most common thing you want to do is to create a branch then switch to that branch.

In the previous exercise, you used git checkout branch-name to switch to a branch. To create a branch then switch to it in one step, you add a -b flag, calling git checkout -b branch-name,

The contents of the new branch are initially identical to the contents of the original. Once you start making changes, they only affect the new branch.

1)
You are in the master branch of the dental repository. Create a new branch called deleting-report.
'''
# git checkout -b deleting-report

'''
2)
Use git rm report.txt to delete the report.
'''
# git rm report.txt

'''
3)
Commit your changes with a log message.
'''
# git commit -m "Deleting report"

'''
4)
Use git diff with appropriate arguments to compare the master branch with the new state of the deleting-report branch.
'''
# git diff master..deleting-report

'''
How can I merge two branches?
Branching lets you create parallel universes; merging is how you bring them back together. When you merge one branch (call it the source) into another (call it the destination), Git incorporates the changes made to the source branch into the destination branch. If those changes don't overlap, the result is a new commit in the destination branch that includes everything from the source branch (the next exercises describe what happens if there are conflicts).

To merge two branches, you run git merge source destination (without .. between the two branch names). Git automatically opens an editor so that you can write a log message for the merge; you can either keep its default message or fill in something more informative.

1)
You are in the master branch of the dental repository. Merge the changes from the summary-statistics branch (the source) into the master branch (the destination) with the message "Merging summary statistics."
'''
# git merge summary-statistics master

'''
What are conflicts?
Sometimes the changes in two branches will conflict with each other: for example, bug fixes might touch the same lines of code, or analyses in two different branches may both append new (and different) records to a summary data file. In this case, Git relies on you to reconcile the conflicting changes.

The file todo.txt initially contains these two lines:

A) Write report.
B) Submit report.
You create a branch called update and modify the file to be:

A) Write report.
B) Submit final version.
C) Submit expenses.
You then switch back to the master branch and delete the first line, so that the file contains:

B) Submit report.
When you try to merge update and master, what conflicts does Git report? You can use git diff master..update to view the difference between the two branches.

git diff master..update

Answer:
Just line B, since it is the only one to change in both branches.
'''

'''
How can I merge two branches with conflicts?
When there is a conflict during a merge, Git tells you that there's a problem, and running git status after the merge reminds you which files have conflicts that you need to resolve by printing both modified: beside the files' names.

Inside the file, Git leaves markers that look like this to tell you where the conflicts occurred:
    
    <<<<<<< destination-branch-name
    ...changes from the destination branch...
    =======
    ...changes from the source branch...
    >>>>>>> source-branch-name

In many cases, the destination branch name will be HEAD because you will be merging into the current branch. To resolve the conflict, edit the file to remove the markers and make whatever other changes are needed to reconcile the changes, then commit those changes.

1)
You are in the master branch of the dental repository. Merge the changes from the alter-report-title branch (the source) into the master branch (the destination).
'''
# git merge alter-report-title master

'''
2)
Use git status to see which file has conflicts.
'''
# git status
'''
3)
It turns out that report.txt has some conflicts. Use nano report.txt to open it and remove some lines so that only the second title is kept. Save your work with Ctrl+O and Enter, and then leave the editor with Ctrl+X. You can easily remove entire lines with Ctrl+K.
'''
# nano report.txt
# ctrl + k (remove whole line)
# leave only the row containing "Dental Work by Season 2017-18"
# ctrl + o (save changes)
# press enter
# ctrl + x (exit nano)

'''
4)
Add the merged file to the staging area.
'''
# git add report.txt

'''
5)
Commit your changes with a log message.
'''
# git commit -m "log message"

'''
How can I create a brand new repository?
So far, you have been working with pre-existing repositories. If you want to create a repository for a new project in the current working directory, you can simply say git init project-name, where "project-name" is the name you want the new repository's root directory to have.

One thing you should not do is create one Git repository inside another. While Git does allow this, updating nested repositories becomes very complicated very quickly, since you need to tell Git which of the two .git directories the update is to be stored in. Very large projects occasionally need to do this, but most programmers and data analysts try to avoid getting into this situation.

Instructions
*Use a single command to create a new Git repository called optical in your current directory.
'''
# git init optical

'''
How can I turn an existing project into a Git repository?
Experienced Git users instinctively start new projects by creating repositories. If you are new to Git, though, or working with people who are, you will often want to convert existing projects into repositories. Doing so is simple, just run:

git init
in the project's root directory, or:

git init /path/to/project
from anywhere else on your computer.

1)
You are in the directory dental, which is not yet a Git repository. Use a single command to convert it to a Git repository.
'''
# git init

'''
2)
Check the status of your new repository.
'''
# git status

'''
How can I create a copy of an existing repository?
Sometimes you will join a project that is already running, inherit a project from someone else, or continue working on one of your own projects on a new machine. In each case, you will clone an existing repository instead of creating a new one. Cloning a repository does exactly what the name suggests: it creates a copy of an existing repository (including all of its history) in a new directory.

To clone a repository, use the command git clone URL, where URL identifies the repository you want to clone. This will normally be something like

    https://github.com/datacamp/project.git

but for this lesson, we will use a repository on the local file system, so you can just use a path to that directory. When you clone a repository, Git uses the name of the existing repository as the name of the clone's root directory, for example:

    git clone /existing/project

will create a new directory called project inside your home directory. If you want to call the clone something else, add the directory name you want to the command:

    git clone /existing/project newprojectname

Instructions
*You have just inherited the dental data analysis project from a colleague, who tells you that all of their work is in a repository in /home/thunk/repo. Use a single command to clone this repository to create a new repository called dental inside your home directory.
'''
# git clone /home/thunk/repo/ dental

'''
How can I find out where a cloned repository originated?

When you a clone a repository, Git remembers where the original repository was. It does this by storing a remote in the new repository's configuration. A remote is like a browser bookmark with a name and a URL.

If you use an online git repository hosting service like GitHub or Bitbucket, a common task would be that you clone a repository from that site to work locally on your computer. Then the copy on the website is the remote.

If you are in a repository, you can list the names of its remotes using git remote.

If you want more information, you can use git remote -v (for "verbose"), which shows the remote's URLs. Note that "URLs" is plural: it's possible for a remote to have several URLs associated with it for different purposes, though in practice each remote is almost always paired with just one URL.

You are in the dental repository. How many remotes does it have?

# git remote
Answer:
1.
'''

'''
How can I define remotes?
When you clone a repository, Git automatically creates a remote called origin that points to the original repository. You can add more remotes using:

    git remote add remote-name URL
    
and remove existing ones using:

    git remote rm remote-name
    
You can connect any two Git repositories this way, but in practice, you will almost always connect repositories that share some common ancestry.

Instructions
*You are in the dental repository. Add /home/thunk/repo as a remote called thunk to it.
'''
# git remote add thunk /home/thunk/repo

'''
How can I pull in changes from a remote repository?

Git keeps track of remote repositories so that you can pull changes from those repositories and push changes to them.

Recall that the remote repository is often a repository in an online hosting service like GitHub. A typical workflow is that you pull in your collaborators' work from the remote repository so you have the latest version of everything, do some work yourself, then push your work back to the remote so that your collaborators have access to it.

Pulling changes is straightforward: the command git pull remote branch gets everything in branch in the remote repository identified by remote and merges it into the current branch of your local repository. For example, if you are in the quarterly-report branch of your local repository, the command:

    git pull thunk latest-analysis

would get changes from latest-analysis branch in the repository associated with the remote called thunk and merge them into your quarterly-report branch.

Instructions
*You are in the master branch of the repository dental. Pull the changes from the master branch of the remote repository called origin.
'''
# git pull origin master

'''
What happens if I try to pull when I have unsaved changes?
Just as Git stops you from switching branches when you have unsaved work, it also stops you from pulling in changes from a remote repository when doing so might overwrite things you have done locally. The fix is simple: either commit your local changes or revert them, and then try to pull again.

1)
You are in the dental repository, which was cloned from a remote called origin. Use git pull to bring in changes from that repository.
'''
# git pull origin master

'''
2)
Discard the changes in your repository.
'''
# git checkout report.txt

'''
3)
Re-try the git pull.
'''
# git pull origin master

'''
How can I push my changes to a remote repository?
The complement of git pull is git push, which pushes the changes you have made locally into a remote repository. The most common way to use it is:

    git push remote-name branch-name

which pushes the contents of your branch branch-name into a branch with the same name in the remote repository associated with remote-name. It's possible to use different branch names at your end and the remote's end, but doing this quickly becomes confusing: it's almost always better to use the same names for branches across repositories.

1)
You are in the master branch of the dental repository, which has a remote called origin. You have changed data/northern.csv; add it to the staging area.
'''
# git add data/northern.csv

'''
2)
Commit your changes with the message "Added more northern data."
'''
# git commit -m "Added more northern data"

'''
3)
Push your changes to the remote repository origin, specifying the master branch.
'''
# git push origin master

'''
What happens if my push conflicts with someone else's work?
Overwriting your own work by accident is bad; overwriting someone else's is worse.

To prevent this happening, Git does not allow you to push changes to a remote repository unless you have merged the contents of the remote repository into your own work.

In this exercise, you have made and committed changes to the dental repository locally and want to push your changes to a remote repository.

1)
Use git push to push those changes to the remote repository origin, specifying the master branch.
'''
# git push origin master

'''
2)
In order to prevent you overwriting remote work, Git has refused to execute your push. Use git pull to bring your repository up to date with origin. It will open up an editor that you can exit with Ctrl+X.
'''
# git pull origin master

'''
3)
Now that you have merged the remote repository's state into your local repository, try the push again.
'''
# git push origin master