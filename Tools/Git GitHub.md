# Git GitHub

### Git

Git is a free and open source distributed version control system.

```
git version
```

```
git version 2.43.0
```

Set your identity

```
git config --global user.name “Yunxiu586”
git config --global user.name 15386742407@163.com
```

```
git config --l
```

```
user.email=15386742407@163.com
user.name=Yunxiu586
```

![gitpicture](/home/yunxiu/Desktop/ROS2_study/Pictures/gitpicture.png)

The file states in Git include 3 categories: Working Directory, Staging Area, and Local Repository.

##### `git init`

Create an empty Git repository, basically a `.git` directory with subdirectories for `objects`, `refs/heads`, `refs/tags`, and template files.

```
git init
```

##### `git status`

Show the working tree status.

+ **Untracked** : A file that exists in your working directory but is not part of Git's version control. Git is not monitoring it for changes.

```
git status
```

```
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Git GitHub.md

nothing added to commit but untracked files present (use "git add" to track)
```

##### `git add`

Add file contents to the staging area.

+ **Tracked** : A file that is already part of the Git repository.
+ **Modified** : A tracked file that has been changed in your working directory, but the changes are not yet staged for the next commit.
+ **Staged** : A modified file has been marked (via `git add`) to be included in the next commit snapshot. The changes are now in the staging area.

```
git add <file_name>
```

```
git add .
```

##### `git commit`

Record changes to the repository.

+ **Committed** : The file's staged snapshot has been permanently stored in the Git repository as part of a commit. The working directory is clean.

```
git commit
```

```
git commit -m "fix(file_name):change content"
```

##### `git checkout`

Create a new branch and switch to that branch.

```
git checkout -b <branch_name>
```

Switch the branch.

```
git checkout <branch_name>
```

##### `git branch`

View all branches.

```
git branch
```

View remote branches.

```
git branch -r
```

View all local and remote branches.

```
git branch -a
```

Delete a local branch.

```
git branch -d <branch_name>
```

Force delete an unmerged branch.

```
git branch -D <branch_name>
```

Delete a remote branch.

```
git push origin --delete <branch_name>
```

##### `git log`

Show the commit logs

```
git log
```

```
commit fa72e8300f785b4aea6c94c94a0f6a6d281fef83 (HEAD -> main)
Author: Yunxiu586 <15386742407@163.com>
Date:   Thu Apr 9 10:35:35 2026 +0800

    first commit
```

##### `git reset`

Resets HEAD to the specified commit, while keeping the staging area and working directory unchanged.

```
git reset --soft <commit_id>
```

Resets HEAD to the specified commit, resets the staging area, but keeps the working directory unchanged.

```
git reset --mixed <commit_id>
```

Resets HEAD to the specified commit, and resets both the staging area and the working directory.

```
git reset --hard <commit_id>
```

##### `git push`

Push the local repository's commits to the remote repository.

```
git push -u origin <branch_name>
```

`--set-upstream` or `-u`  links your local branch to the specified remote branch, allowing you to later use  `git push` or `git pull` without specifying the remote and branch.

`origin` is a shortcut alias for the URL of the remote Git repository.

```
git push origin main
```

##### `git pull`

Before pushing local changes, it is best to pull the latest changes from the remote repository to avoid conflicts.

```
git pull origin main
```

##### `git fetch`

Get updates from a remote repository.

```
git fetch origin <branch_name>
```

```
git fetch origin main
```

##### `git merge`

Merge other branches into the current branch.

```
git merge origin
```

```
git merge <branch_name>
```

##### `git clone`

Clone the remote repository locally.

```
git clone <URL>
```

```
git clone https://github.com/Yunxiu586/ROS2_study.git
```

##### `git remote`

List the short names (e.g., `origin`, `upstream`) of your configured remote repositories.

```
git remote
```

List the remote repositories configured for your local Git project, displaying both the short names and their corresponding URLs.

```
git remote -v
```

Add a new remote repository with the short name "upstream" pointing to the specified URL. `upstream` refers to the original repository that your fork is based on.

```
git remote add upstream <URL>
```



### GitHub

GitHub is a proprietary developer platform that allows developers to create, store, manage, and share their code. It uses Git to provide distributed version control and GitHub itself provides access control, bug, software feature requests, task management, continuous integration, and wikis for every project.

##### fork

A fork is a new repository that shares code and visibility settings with the original "upstream" repository.

##### pr

Create a **pull request** on GitHub or other hosting platforms that invite team members to code review. When PR merges, your changes merge into the main branch.

+ Pull requests.
+ New pull request.
+ Base repository: main, head repository: <branch_name>.
+ Add descriptions.
+ Create pull request.
+ Merge pull request.

##### Workflow

+ Fork a repository.
+ Clone your fork locally.

```
git clone <URL>
```

+ Add the original repository as an upstream remote to sync changes.

```
git remote add upstream <URL>
git remote -v
```

+ Always work on a new branch.

```
git checkout -b <branch_name>
```

+ Commit.

```
git add .
git commit -m "<description>"
```

+ Push to your fork.

`origin` points to your fork on GitHub.

`upstream` points to the original repository you forked from.

```
git push origin <branch_name>
```

+ Create a pull request.

+ Keep your fork updated.

```
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

