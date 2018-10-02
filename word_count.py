#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"arg",
	help="what does this do?",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
