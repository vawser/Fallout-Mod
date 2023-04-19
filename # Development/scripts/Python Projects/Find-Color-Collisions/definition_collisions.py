# "C:\Program Files (x86)\Python314\Python.exe" "C:\Users\Ben\Documents\Python\projects\Definitions Appender\definitions_appender.py"

import os
import random
import sys

"""
Find color collisions in definition.csv file
"""

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))
		
		
def main():
	os.chdir( getScriptPath() )
	
	with open( "definition.csv", "rt" ) as sourceFile:
		text = sourceFile.readlines()

	fixFile = open( "fixlist.txt", "wt" )
	
	colorList = []
	idList = []
	
	for i in range( len( text ) ):
		tempString = text[i].split( ";" )
		id = tempString[0]
		r = tempString[1]
		g = tempString[2]
		b = tempString[3]
		
		colorEntry = "{0};{1};{2}".format( r, g, b )
		
		if id in idList:
			print( "Duplicate id: {0}".format( id ) )
			fixFile.write( "Duplicate id: {0}\n".format( id ) )
		else:
			idList.append( id )
		
		if colorEntry in colorList:
			print( "Duplicate colour: {0}".format( colorEntry ) )
			fixFile.write( "Duplicate: {0}\n".format( colorEntry ) )
			
		else:
			colorList.append( colorEntry )
		
	fixFile.close()
	
if __name__ == "__main__":
	main()