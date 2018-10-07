#!/usr/bin/env python

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

	# ## Question 4 (4 pts)
	#
	# Before continuing - make sure you have the latest version of `word_count.py`.
	# This question should be included (starting at line 27).
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

	

print("   ", lines)
