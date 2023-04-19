# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\Xylozi\Documents\Python\Projects\EU4\Noun Name Gen\noun_name_gen.py"

import os
import sys
import random
import time

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))

def main():
    os.chdir( getScriptPath() )
    
    output = open( "output.txt", "w+" )
    
    with open( "prefix.txt", "rt" ) as sourceFile:
        prefix_text = sourceFile.readlines()
        
        with open( "postfix.txt", "rt" ) as sourceFile:
            postfix_text = sourceFile.readlines()
       
            for i in range( len( prefix_text ) ):
                for j in range( len( postfix_text ) ):
                    if prefix_text[i] != postfix_text[j]:
                        output.write( "\"{0}{1}\" ".format( prefix_text[i].strip( "\n" ).strip( "\r" ), postfix_text[j].strip( "\n" ).strip( "\r" ) ) )

    output.close()
    
if __name__ == "__main__":
	main()