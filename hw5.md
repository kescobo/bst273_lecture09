# Homework 5

Unlike previous homeworks, this week's homework will be submitted in two parts.
Edit this file (`hw5.md`) to answer questions 1-3 and 6. Edit the file
`word_count.py` to answer questions 4 and 5.

**Both files should be submitted to canvas when complete.**

Points for question 7 will depend on making a pull request on github.

After class on Thursday, you should have

1. a remote **fork** of `kescobo/best273_lecture09` on your github account
2. a local **clone** of your fork on your computer
3. a local **branch** other than `master`

In the questions below, ***bold italic*** text indicates instructions to
perform or questions to answer for credit.

Note - `<!-- This is the syntax for a comment in this type of document -->`.

## Question 1 (2 pts)

Open a terminal and change directories into your local git repo.
Use `git branch` to determine what branches are found locally.

***Enter the output in the code block below:***

```sh
$ git branch
# enter the output here
```

***How can you tell which branch you're on?***

<!-- Put your answer here -->

## Question 2 (2 pts)

Since you cloned your local repo from your fork of Kevin's repo on github,
your local repo knows about your fork.
By default, when you clone a repo, that repo's location is set as a "remote"
called `origin`. A remote is simply another location that your repo lives.
Most often, remotes are on websites like github or bitbucket,
but they can also be set up on computing clusters,
or even other disk locations on your own computer.

Investigate your remote(s) using `git remote` at the command line.
Use `git remote --help` to see what you can do with this command.

***Determine what the url of your current remote is.***
***Enter the command and output in the code block below.***

```sh
$ # Enter command here
# Enter output here
```

## Question 3 (2 pts)

In order to stay current with my repo - you need to set my repo as a remote.
You won't be able to push changes to my repo directly, but you can pull changes
to your local repo.

***Set a new remote called "kevin" that points to the url***
***https://github.com/kescobo/bst273_lecture09.git***

```sh
$ git remote add # Put in the command here
```

Assuming you haven't made any changes to your local master branch
(you shouldn't have!!), you can now do:

```sh
$ git checkout master # make sure you're on the master branch
$ git pull kevin master # pull the latest commits from the master branch in my github repo
```
