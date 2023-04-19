# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\Xylozi\Documents\Python\Projects\EU4\Province Discovery Editor\province_discovery_custom.py"

import os
import random
import sys

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))
	
script_dir = getScriptPath()
input_dir = script_dir + "\\input"
	
def main():
	discoveryList = []
	discoveryList.append( readGroup( "westeros_tags.txt", False ) )
	discoveryList.append( readGroup( "essos_west_tags.txt", False ) )
	discoveryList.append( readGroup( "central_essos_tags.txt", False ) )
	discoveryList.append( readGroup( "essos_east_tags.txt", False ) )
	discoveryList.append( readGroup( "dothraki_tags.txt", False ) )
	discoveryList.append( readGroup( "pirate_tags.txt", False ) )
	discoveryList.append( readGroup( "summer_tags.txt", False ) ) 
	discoveryList.append( readGroup( "wildling_tags.txt", False ) )
	
	os.chdir( script_dir )
	
	for i in range( 0, len( discoveryList ) ):
		createGroup( discoveryList[i], i )
		
def createGroup( list, number ):
	if number == 0:
		groupName = "westeros"
	elif number == 1:
		groupName = "free_cities"
	elif number == 2:
		groupName = "slaver_cities"
	elif number == 3:
		groupName = "magical_cities"
	elif number == 4:
		groupName = "dothraki"
	elif number == 5:
		groupName = "pirate"
	elif number == 6:
		groupName = "summer_islands"
	elif number == 7:
		groupName = "wildling"
	else:
		groupName = "error"
		
	tempFile = open( "{0}.txt".format( groupName ), "wt" )
	tempFile.write( "discovery_{0} = {{\n".format( groupName ) )
	for i in range( len( list ) ):
		tempFile.write( "\t{0} = {{\n".format( list[i] ) )
		tempFile.write( "\t\tdiscover_province = PREV\n" )
		tempFile.write( "\t}\n" )
		
	tempFile.write( "}\n" )
	tempFile.close()
	
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