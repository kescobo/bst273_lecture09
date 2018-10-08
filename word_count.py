#!/usr/bin/env python

"""
============
Instructions
============

The prompts for hw5 can be found in the hw5.md file on the master branch of the
bst273_lecture09 repository. Answer questions 1-3 inside this multi-line string
where indicated

QUESTION 1:

What is the output of the `git branch` command?
----------
<paste answer here>
----------

How can you tell which branch you're on?
----------
<type answer here>
----------

QUESTION 2:

----------
$ <enter command here>
<enter output here>
----------

QUESTION 3:

----------
$ git remote add <What goes here?>
----------

"""

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to the file we want to read",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )

fh = open(args.data_file)

lines = 0
words = 0
chars = 0

for line in fh:
	lines += 1

	# ## Question 4a (2 pts)
	#
	# Before continuing - make sure you have the latest version of `word_count.py`.
	# This question should be included (starting at line 63).
	#
	# The current version of our `word_count.py` counts and prints the number of lines.
	# The next step is to get and print the number of words. According to our
	# [class notes](class_notes.md), the way to do this is:
	# 2. to count the number of words, use `.split()` on the line, then use `len()` on the list that's returned
	#       1. don't forget to add that number to the `words` variable!
	#
	# ***Edit `word_count.py` to count the number of words in each line,***
	# ***and add that number to the `words` variable.***
	# ***Be sure to print the number of words.***
	#
	# You can test that this works by running the test script. You should see the
	# following:
	#
	# ```sh
	# $ python test_word_count.py test_files/constitution.txt
	# Here is the result from running command-line <wc>:
	#      872    7652   45119 test_files/constitution.txt
	# Here is the result from running your python <wc>:
	#      872    7652
	# ```
	#
	# ## Question 4b (2 pts)
	#
	# The last step is to get the number of bytes (characters). According to our
	# notes, to do this:
	#
	# 1. to count the number of bytes, use `len()` on the line string itself
	#  1. don't forget to add that number to the `bytes` variable!
	#
	# ***Edit `word_count.py` to count the number of bytes in each line,***
	# ***and add that number to the `chars` variable.***
	# ***Be sure to print the number of characters.***
	#
	# You can test that this works by running the test script. You should see the
	# following:
	#
	# ```sh
	# $ python test_word_count.py test_files/constitution.txt
	# Here is the result from running command-line <wc>:
	#      872    7652   45119 test_files/constitution.txt
	# Here is the result from running your python <wc>:
	#      872    7652   45119
	# ```
	#
	#
	# ## Question 5 (4 pts)
	#
	# The `wc` utility has a number of options that enable one to get **only**
	# lines, **only** words, or **only** bytes. Eg.
	#
	# ```sh
	# $ wc -l test_files/constitution.txt
	#      872 test_files/constitution.txt
	# ```
	#
	# Add the additional command line arguments `-l`, `-w`, and `-c` options using
	# `argparse` to print just `lines`, `words` and `chars` respectively.
	# You should be able to run the following commands, and get the outputs shown.
	#
	# ```sh
	# $ python word_count.py -c test_files/constitution.txt
	# 45119
	# $ python word_count.py -w test_files/constitution.txt
	# 7652
	# $ python word_count.py -l test_files/constitution.txt
	# 872
	# ```
	#
	# **Hint:** - even though this question is at the end of the homework script,
	# you probably need to add some stuff to the beginning of the script too.



print("   ", lines)
