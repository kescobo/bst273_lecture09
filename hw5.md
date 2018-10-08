# Homework 5

In this assignment, you will complete our python `wc` clone, and learn more
about using git and github to collaborate. This file contains instructions
for each question, but you should submit your answers to questions 1-3
inside the indicated parts of `word_count.py`

After class on Thursday, you should have

1. a remote **fork** of `kescobo/best273_lecture09` on your github account
2. a local **clone** of your fork on your computer
3. a local **branch** other than `master`

In the questions below, ***bold italic*** text indicates instructions to
perform or questions to answer for credit.

## Question 1 (4 pts)

Open a terminal and change directories into your local git repo.
Use `git branch` to determine what branches are found locally.
Enter the answers to the following questions into the indicated location
in `word_count.py`

***What is the output of the following command?***

```sh
$ git branch
```

***How can you tell which branch you're on?***



## Question 2 (4 pts)

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
***Enter the command used and the output in the indicated place in `word_count.py`***

## Question 3 (2 pt)

In order to stay current with my repo - you need to set my repo as a remote.
You won't be able to push changes to my repo directly, but you can pull changes
to your local repo.

***Set a new remote called "kevin" that points to the url***
***https://github.com/kescobo/bst273_lecture09.git***

```sh
$ git remote add # What goes here?
```

Assuming you haven't made any changes to your local master branch
(you shouldn't have!!), you can now do:

```sh
$ git checkout master # make sure you're on the master branch
$ git pull kevin master # pull the latest commits from the master branch in my github repo
```

**NOTE:** If you have any errors or merge conflicts, you will have issues
with the following steps. If this happens, do the following

```sh
$ git fetch kevin
$ git reset --hard kevin master
```

## Question 4a (3 pts)

Before continuing - make sure you have the latest version of `word_count.py`.
This question should be included (starting at line 63).

The current version of our `word_count.py` counts and prints the number of lines.
The next step is to get and print the number of words. According to our
[class notes](class_notes.md), the way to do this is:
2. to count the number of words, use `.split()` on the line, then use `len()` on the list that's returned
      1. don't forget to add that number to the `words` variable!

***Edit `word_count.py` to count the number of words in each line,***
***and add that number to the `words` variable.***
***Be sure to print the number of words.***

You can test that this works by running the test script. You should see the
following:

```sh
$ python test_word_count.py test_files/constitution.txt
Here is the result from running command-line <wc>:
     872    7652   45119 test_files/constitution.txt
Here is the result from running your python <wc>:
     872    7652
```

## Question 4b (3 pts)

The last step is to get the number of bytes (characters). According to our
notes, to do this:

1. to count the number of bytes, use `len()` on the line string itself
 1. don't forget to add that number to the `bytes` variable!

***Edit `word_count.py` to count the number of bytes in each line,***
***and add that number to the `chars` variable.***
***Be sure to print the number of characters.***

You can test that this works by running the test script. You should see the
following:

```sh
$ python test_word_count.py test_files/constitution.txt
Here is the result from running command-line <wc>:
     872    7652   45119 test_files/constitution.txt
Here is the result from running your python <wc>:
     872    7652   45119
```


## Question 5 (9 pts)

The `wc` utility has a number of options that enable one to get **only**
lines, **only** words, or **only** bytes. Eg.

```sh
$ wc -l test_files/constitution.txt
     872 test_files/constitution.txt
```

Add the additional command line arguments `-l`, `-w`, and `-c` options using
`argparse` to print just `lines`, `words` and `chars` respectively.
You should be able to run the following commands, and get the outputs shown.

```sh
$ python word_count.py -c test_files/constitution.txt
45119
$ python word_count.py -w test_files/constitution.txt
7652
$ python word_count.py -l test_files/constitution.txt
872
```

**Hint:** - even though this question is at the end of the homework script,
you probably need to add some logical flags to the beginning of the script too.
