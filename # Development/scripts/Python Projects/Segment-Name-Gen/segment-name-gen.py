# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\Xylozi\Documents\Python\Projects\EU4\Duo Name Generator\name_generator.py"

import os
import random
import sys

"""
Generate names from segments, and output them in EU4 script format for country file and culture file
"""

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))

input_dir = getScriptPath() + "\\input"
output_dir = getScriptPath() + "\\output"

GEN_AMOUNT = 1000
GEN_MINIMUM_LENGTH = 2
GEN_MAXIMUM_LENGTH = 3
GEN_FEMALE_CHANCE = 10

def main():
	os.chdir( input_dir )
	
	# Search input directory for segment lists
	for folderName, subFolders, filenameList in os.walk( input_dir ):	
			# For each list, get the name and then generate the names from the list
			for j in range( len( filenameList ) ):
				filename = filenameList[j]
				
				# Get name to use for save file
				splitString = filename.split( "_" )
				name = splitString[0]

				generateNames( filename, name )

def generateNames( filename, savename ):
	""" Generates a list of names from a list of segments """
	
	# Grab list of segments from file
	with open( filename, "rt" ) as sourceFile:
		text = sourceFile.readlines()
		
	# Create list of segments
	segmentList = []
	for i in range( len( text ) ):
		segmentList.append( text[i] )
	
	# End function if namelist is empty
	if len( segmentList ) <= 0:
		return
		
	# Create duplicate name list
	additionsList = []
		
	# Create output file
	os.chdir( output_dir )
	cultureNames = open( "namelist.txt", "wt" )
	os.chdir( input_dir )
	
	# Create names
	for i in range( GEN_AMOUNT ):
		length = random.randint( GEN_MINIMUM_LENGTH, GEN_MAXIMUM_LENGTH )
		
		nameList = []
		
		firstSegment = segmentList[random.randint( 0, len( segmentList )-1 )]
		firstSegment = firstSegment.strip( "\n" )
			
		nameList.append( "\"{0}".format( firstSegment.capitalize() ) )
		
		secondSegment = segmentList[random.randint( 0, len( segmentList )-1 )]
		secondSegment = secondSegment.strip( "\n" )
			
		nameList.append( "{0}\"\n".format( secondSegment ) )
		
		name = "".join( nameList )
		
		# Check if the name has already been made
		if name in additionsList:
			#print( "Duplicate name" )
			i = i - 1
		else:	
			additionsList.append( name )
		
		#print( nameList )
		#print( name )

		# Write out entry
		cultureNames.write( "10 = {\n" )
		cultureNames.write( "\tchange_province_name = {0}".format( name ) )
		cultureNames.write( "}\n" )
		
if __name__ == "__main__":
	main()