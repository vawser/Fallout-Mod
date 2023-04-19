# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\guest-new\Documents\Python\projects\Tech Year Changer\tech_year_changer.py"

import os
import random
import sys

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))
		
def changeTechFile( type, start_year, increment_year ):
	os.chdir( getScriptPath() )
	start_year = int( start_year )
	increment_year = int( increment_year )
	
	try:
		with open( "{0}.txt".format( type ), "rt" ) as sourceFile:
			text = sourceFile.readlines()
	except IOError:
		print( "Did not find {0}.txt".format( type ) )
		return

	current_year = start_year
	
	for i in range( len( text ) ):
		if "year" in text[i]:
			text[i] = "year = {0}\n".format( current_year )
			current_year = current_year + increment_year
			
	with open( "new_{0}.txt".format( type ), "wt" ) as sourceFile:
		text = "".join( text )
		sourceFile.write(text)	
	
def main():
	start_year = input( "Enter start year: " )
	increment_year = input( "Enter increment year: " )
	
	changeTechFile( "adm", start_year, increment_year )
	changeTechFile( "dip", start_year, increment_year )
	changeTechFile( "mil", start_year, increment_year )
	
	
if __name__ == "__main__":
	main()