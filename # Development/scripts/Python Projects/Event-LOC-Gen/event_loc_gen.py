# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\guest-new\Documents\Python\projects\Colour Generator\colour_generator.py"

import os
import sys
import random
import time
import colorsys

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))

def main():
	os.chdir( getScriptPath() )
	
	name = input( "Enter namespace: " )
	count = input( "Enter iterations: " )
	count = int(count)
	
	loc = open( "loc.txt", "wt" )
	for i in range( 1, count + 1 ):
		loc.write( " {0}.{1}.title: \"\"\n".format( name, i ) )
		loc.write( " {0}.{1}.desc: \"\"\n".format( name, i ) )
		loc.write( " {0}.{1}.option.a: \"\"\n".format( name, i ) )
		loc.write( " {0}.{1}.option.b: \"\"\n\n".format( name, i ) )
		
if __name__ == "__main__":
	main()