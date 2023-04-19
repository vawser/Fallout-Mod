# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\Xylozi\Documents\Python\Projects\EU4\Colour Generator\colour_generator2.py"

import os
import sys
import random
import time
import colorsys

"""
Generate EU4 province files from definition.csv with names
"""

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))

def main():
	os.chdir( getScriptPath() )
	
	targetDir = getScriptPath() + "//provinces"
	nameList = []
	
	with open( "proper_definition.csv", "rt" ) as sourceFile:
		text = sourceFile.readlines()
	
	for i in range( len( text ) - 1 ):
		line = text[i].split( ";" )
		print( line )
		name = line[4].strip( "\t" ).strip( "\n" ).strip( "\t" ).strip( " " ).strip( "-" ).strip( "'" )
		nameList.append( name )
	
	os.chdir( targetDir )
	
	for i in range( len( nameList ) ):
		output = open( "{0} - {1}.txt".format( i+1, nameList[i] ), "wt" )
		output.write( "# {0} \n".format( nameList[i] ) )
		output.write( "is_city = no\n" )
		output.write( "\n" )
		output.write( "base_tax = 1\n" )
		output.write( "base_manpower = 1\n" )
		output.write( "base_production = 1\n" )
		output.write( "\n" )
		output.write( "culture = noculture\n" )
		output.write( "religion = noreligion\n" )
		output.write( "\n" )
		output.write( "hre = no\n" )
		output.write( "trade_goods = grain\n" )
		output.write( "\n" )
		output.close()

	output.close()
		
if __name__ == "__main__":
	main()