# Lecture 09 Live coding

Repo for creating a python version of
the command line tool `wc`.

## Class notes from 2018-10-02

### Step 1: Figure out what does `wc` actually do?

- use `$ man wc` at the command line to read the manual for `wc`
- it returns the number of lines, words, and bytes (characters) of a file

example:

```sh
$ wc test_files/constitution.txt
     872    7652   45119 test_files/constitution.txt
```

### Step 2: Write out a description of what your program needs to do

First, as with just about any program you write,
it's useful thinking about what the `INPUT`(s) and `OUTPUT`(s) should be.

In this case,
    - `INPUT`: a file path
    - `OUTPUT`s:
        - count of `lines`
        - count of `words`
        - count of `bytes`

Note: the `wc` utility actually allows you to provide many files as inputs
and returns counts for each of them.
In this assignment, we won't worry about that though.

Next, we should write out what our code will do in plain language.
In other words, given our `INPUT`s, how do we get to our `OUTPUT`s.
In class, here's what we came up with:

1. Get our input file as a commandline argument (probably using `argparse`)
2. Open the file
3. Initialize variables for `lines`, `words`, and `bytes`
4. Read the file line by line
    1. for each line, add `1` to the `lines` variable
    2. to count the number of words, use `.split()` on the line, then use `len()` on the list that's returned
        1. don't forget to add that number to the `words` variable!
    3. to count the number of bytes, use `len()` on the line string itself
        1. don't forget to add that number to the `bytes` variable!
5. Once we've read through the file, print the values of `lines`, `words`, and `bytes` to the screen

### Step 3: Start translating your plan into python syntax
