# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\Xylozi\Documents\Python\Projects\EU4\quick_text_gen.py"

import os
import sys
import random
import time
import shutil

"""
Strip old definition.csv of listed province IDs and generate a new and reordered definition.csv without them.
"""

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))

def getFileAsString( filepath ):
    with open( filepath, "rt", encoding='windows-1252' ) as sourceFile:
        text = sourceFile.readlines()
        
    text_string = ""
    
    for i in range( len( text ) ):
        text_string = text_string + text[i]
        
    return text_string
    
def main():
    os.chdir( getScriptPath() )
    
    base_path = getScriptPath()
    
    idFilestring = getFileAsString( base_path + "//strip_ids.txt" )
    idFilestring = " ".join(idFilestring.split())
    
    idList = idFilestring.split( " " )
    #print( idList )
    
    inputDir = base_path + "//dirty//"
    outputDir = base_path + "//clean//"
    
    strippedFile = open( outputDir + "//definition.csv", "wt" )
    
    with open( inputDir + "definition.csv", "rt", encoding='windows-1252' ) as sourceFile:
        text = sourceFile.readlines()
        
        for i in range( len( text ) ):
            defString = text[i].split( ";" )
            id = defString[0]
            
            if id in idList:
                print( "Skip" )
            else:
                strippedFile.write( text[i] )
                
            
if __name__ == "__main__":
	main()