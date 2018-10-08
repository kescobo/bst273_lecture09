#!/usr/bin/env python

import os
import sys

if len( sys.argv ) < 2:
	sys.exit( "ERROR, usage is: python <this>.py <WC ARGUMENTS>" )

print( "Here is the result from running command-line <wc>:" )
os.system( " ".join( ["wc"] + sys.argv[1:] ) )

print( "Here is the result from running your python <wc>:" )
os.system( " ".join( ["python", "word_count.py"] + sys.argv[1:] ) )
