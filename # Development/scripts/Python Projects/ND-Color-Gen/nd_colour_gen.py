import os
import sys
import random
import time
import colorsys

"""
Generate color definitions for EU4 Nation Designer configuration
"""

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))

def main():
	os.chdir( getScriptPath() )
	
	colourList = []
	step = 25
	
	for i in range( int(255 / step) ):
		for j in range( int(255 / step) ):
			for k in range( int(255 / step) ):
				if i > 220 and j > 100 and k > 140:
					pass
				else:
					colourList.append( "{0} {1} {2}".format( (k*step), (j*step), (i*step) ) )
	
	print( colourList[0] )
	
	# Format into file
	output = open( "output_lines.txt", "wt" )
	
	for i in range( len( colourList ) ):
		colour = colourList[i].split( " " )
		output.write( "color = {{ {0} {1} {2} }}\n".format( colour[0], colour[1], colour[2] ) )
		output.write( "flag_color = {{ {0} {1} {2} }}\n".format( colour[0], colour[1], colour[2] ) )
		
	output.close()
		
if __name__ == "__main__":
	main()