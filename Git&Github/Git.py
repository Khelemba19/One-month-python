# What is Git?
# It is a tool that helps to track change in code. It is popularl, free, open source, fast & scalable.
# It track history and helps in collaborate with multiple people.

# Github
# It is a website that allows developers to store and manage their code using Git.
# https://github.com

# Configuration
# git config --global user.name "Your Name"
# git config --global user.email "Email"
# git config --list

# Clone & Status
# Clone: It clones a repository on our local machine
# git clone <Link>

# Status: It displays the state of the code 
# git status 

# cd : change directory
# ls : list
# ls -a: shows hidden files

# Untracked/U
# New files that git does not yet tracked

# Modified/M 
# Changed in the local but not in the remote repository

# Staged/S 
# Files is ready to be committed

# Unmodified
# Unchanged

# Add
# Add new or changed files in your working divice to the git staging area
# git add <name>

# Commit 
# It is the record of the change
# git commit -m "Example"

# Push
# Upload the local repository to github
# git push origin main 

# Init commands
# init : used to create new git repository
# git init <new repository name>
# git remote add origin <Link>
# git remove -v (to verify)
# git branch (to check current branch)
# git branch -M <name> (to rename)
# git push origin main (to push the commit)
# mkdir : make directory
# git checkout <branch name> (to navigate branch)
# git checkout -b <new branch name> (to create new branch)
# git branch -d <branch name> (to delete the branch)

# Merge 
# git diff <branch name> (to compare current branch with the other branch)
# git merge <branch name> (to merge the branch)

# Pull request
# It lets you to tell others about changes you pushed to a branch in a repository on Github.

# Undoing changes
# Staged
# git reset <name>
# git reset (for multiple)

# Committed change
# git reset HEAD~1
# git reset <commit hash>
# git reset --hard <commit hash>

# Fork 
# A fork is a new repository that shares code and visibility settings with the original upstream repository