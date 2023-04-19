# "C:\Program Files (x86)\Python314\Python.exe" "C:\Users\Ben\Documents\Python\projects\Province Discovery Editor\province_discovery_editor.py"

import os
import random
import sys

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))
	
working_dir = "C:\\Users\\Ben\\Documents\\Paradox Interactive\\Europa Universalis IV\\mod\\asoiaf_test\\history\\provinces_testing"
script_dir = getScriptPath()
input_dir = script_dir + "\\input"
	
def main():
	provinceList = []
	provinceList.append( readGroup( "westeros.txt", True ) )
	provinceList.append( readGroup( "essos_west.txt", True ) )
	provinceList.append( readGroup( "central_essos.txt", True ) )
	provinceList.append( readGroup( "essos_east.txt", True ) )
	provinceList.append( readGroup( "dothraki.txt", True ) )
	provinceList.append( readGroup( "pirate.txt", True ) )
	provinceList.append( readGroup( "summer.txt", True ) )
	provinceList.append( readGroup( "wildling.txt", True ) )
	
	discoveryList = []
	discoveryList.append( readGroup( "westeros_tags.txt", False ) )
	discoveryList.append( readGroup( "essos_west_tags.txt", False ) )
	discoveryList.append( readGroup( "central_essos_tags.txt", False ) )
	discoveryList.append( readGroup( "essos_east_tags.txt", False ) )
	discoveryList.append( readGroup( "dothraki_tags.txt", False ) )
	discoveryList.append( readGroup( "pirate_tags.txt", False ) )
	discoveryList.append( readGroup( "summer_tags.txt", False ) ) 
	discoveryList.append( readGroup( "wildling_tags.txt", False ) )
	
	os.chdir( working_dir )
	
	#appendFile( "2 - Thenn.txt", discoveryList[7] ) 
	#appendFile( "3 - Northern Frostfangs.txt", discoveryList[7] ) 
	
	for i in range( 0, len( discoveryList ) ):
		for folderName, subFolders, filenameList in os.walk( working_dir ):
			for j in range( 0, len( filenameList ) - 1 ):
				id = filenameList[j].split( "-" )
				id = id[0].strip()
				
				if provinceList[i].count(id) > 0:
					appendFile( filenameList[j], discoveryList[i] ) 
					print( "Added to {0}".format( filenameList[j] ) )

def appendFile( filename, subList ):
	""" Iterate over the discovery list """
	
	writeToFile( filename, "", False, "", "\n" )
	
	subList.reverse()
	
	for j in range( 0, len( subList ) ):
		writeToFile( filename, subList[j], True, "", "\n" )
		
	writeToFile( filename, "", False, "", "\n" )
		
def writeToFile( filename, insertedText, checked, prefix, postfix ):
	""" Write current discovery to file """
	
	with open( filename, "rt" ) as sourceFile:
		text = sourceFile.readlines()

	if checked == True:
		if text.count(insertedText+"\n") > 0: 
			print( "\"{0}\" is already found in {1}".format( insertedText, filename ) )
		else:
			text.insert( 1, "{0}{1}{2}".format( prefix, insertedText, postfix ) )
	else:
		text.insert( 1, "{0}{1}{2}".format( prefix, insertedText, postfix ) )
		
	with open( filename, "wt" ) as sourceFile:
		text = "".join( text )
		sourceFile.write(text)	
		
def readGroup( currentFile, doSplit ):
	os.chdir( input_dir )
	
	tempList = []
	
	with open( currentFile, "rt" ) as sourceFile:
		text = sourceFile.readlines()
	
	if doSplit == True:
		numberList = text[0].split( " " )
		for i in range( 0, len( numberList ) ):
			tempList.append( numberList[i] .strip( "\n" ) )
	else:
		for i in range( 0, len( text )  ):
			tempList.append( text[i] .strip( "\n" ) )

	return tempList
	
if __name__ == "__main__":
	main()