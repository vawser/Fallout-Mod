# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\Xylozi\Documents\Python\Projects\EU4\Quick Gen\quick_gen.py"

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

	outputFile = open( "mod_output.txt", "wt" )
	total = 100
	current_value = 100
	for i in range( total ):
		outputFile.write( "\tif = {\n" )
		outputFile.write( "\t\tlimit = {\n" )
		outputFile.write( "\t\t\tis_variable_equal = {{ which = current_chance value = {0} }}\n".format( current_value ) )
		outputFile.write( "\t\t}\n" )
		outputFile.write( "\t\trandom_list = {\n" )
		outputFile.write( "\t\t\t{0} = {{\n".format( total ) )
		outputFile.write( "\t\t\t\tcountry_event = { id = GOT_SPY.2 }\n" )
		outputFile.write( "\t\t\t}\n" )
		outputFile.write( "\t\t\t{0} = {{\n".format( 100 - total ) )
		outputFile.write( "\t\t\t\tcountry_event = { id = GOT_SPY.3 }\n" )
		outputFile.write( "\t\t\t}\n" )
		outputFile.write( "\t\t}\n" )
		outputFile.write( "\t}\n" )
		total = total - 1
		current_value = current_value - 1
	outputFile.close()
	
if __name__ == "__main__":
	main()