# "C:\Program Files (x86)\Python_3_5_1\Python.exe" "C:\Users\Xylozi\Documents\Python\Projects\EU4\Name Generator\name_generator.py"

import os
import random
import sys

def getScriptPath():
    """ Returns current path of script """
    return os.path.dirname(os.path.realpath(sys.argv[0]))

input_dir = getScriptPath() + "\\input"
output_dir = getScriptPath() + "\\output"

GEN_AMOUNT = 1000
GEN_MINIMUM_LENGTH = 2
GEN_MAXIMUM_LENGTH = 2
GEN_FEMALE_CHANCE = 10
GEN_SEPERATOR = [ "'", "" ]
GEN_USE_SEPERATOR = True
GEN_SEPERATOR_CHANCE = 0

GEN_USE_SPLIT_SEGMENTS = True

def main():
    os.chdir( input_dir )

    if GEN_USE_SPLIT_SEGMENTS == True:
        generateFormattedNames( "segments_1.txt", "segments_2.txt", "generated" )
    else:
        generateNames( "segments_1.txt", "generated" )
 
def generateFormattedNames( prefix_segments, suffix_segments, filename ):
    """ Generates a list of names from a list of segments """
    
    with open( prefix_segments, "rt" ) as sourceFile:
        prefix = sourceFile.readlines()

    with open( suffix_segments, "rt" ) as sourceFile:
        suffix = sourceFile.readlines()
 
    prefixList = []
    for i in range( len( prefix ) ):
        prefixList.append( prefix[i] )
    
    suffixList = []
    for i in range( len( suffix ) ):
        suffixList.append( suffix[i] )
        
    # End function if namelist is empty
    if len( prefixList ) <= 0 or len( suffixList ) <= 0:
        return
        
    # Create duplicate name list
    additionsList = []
        
    # Create output file
    os.chdir( output_dir )
    cultureNames = open( "{0}_culture.txt".format( filename ), "wt" )
    os.chdir( input_dir )
    
    for i in range( GEN_AMOUNT ):
        length = random.randint( GEN_MINIMUM_LENGTH, GEN_MAXIMUM_LENGTH )
        
        nameList = []
        
        for j in range( length ):
            prefixSegment = prefixList[random.randint( 0, len( prefixList )-1 )]
            prefixSegment = prefixSegment.strip( "\n" ) 
            suffixSegment = suffixList[random.randint( 0, len( suffixList )-1 )]
            suffixSegment = suffixSegment.strip( "\n" ) 
            seperator = GEN_SEPERATOR[random.randint( 0, len( GEN_SEPERATOR )-1)]
            
            # Prefix
            if j == 0:
                nameList.append( "\"{0}".format( prefixSegment.capitalize() ) )
            # Middle
            elif j == (length-1):
                if GEN_USE_SEPERATOR == True:
                    if random.randint( 0, 100 ) < GEN_SEPERATOR_CHANCE:
                        nameList.append( "{0}{1}\"".format(seperator, suffixSegment) )
                    else:
                        nameList.append( "{0}\"".format( suffixSegment ) )
                else:
                    nameList.append( "{0}\"".format( suffixSegment ) )
            else:
                if GEN_USE_SEPERATOR == True:
                    if random.randint( 0, 100 ) < GEN_SEPERATOR_CHANCE:
                        nameList.append( "{0}{1}".format(seperator, suffixSegment) )
                    else:
                        nameList.append( "{0}".format(suffixSegment) )
                else:
                    nameList.append( "{0}".format(suffixSegment) )
                    
            name = "".join( nameList )
        
        if name in additionsList:
            i = i - 1
        else:    
            additionsList.append( name )

        cultureNames.write( "{0} ".format( name ) )
        
def generateNames( first_segments, filename ):
    """ Generates a list of names from a list of segments """
    
    # Grab list of segments from file
    with open( first_segments, "rt" ) as sourceFile:
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
    cultureNames = open( "{0}_culture.txt".format( filename ), "wt" )
    monarchNames = open( "{0}_monarch.txt".format( filename ), "wt" )
    leaderNames = open( "{0}_leader.txt".format( filename ), "wt" )
    os.chdir( input_dir )
    
    # Create names
    for i in range( GEN_AMOUNT ):
        length = random.randint( GEN_MINIMUM_LENGTH, GEN_MAXIMUM_LENGTH )
        
        nameList = []
        
        for j in range( length ):
            # Get random segment
            segment = segmentList[random.randint( 0, len( segmentList )-1 )]
            segment = segment.strip( "\n" ) 
            seperator = GEN_SEPERATOR[random.randint( 0, len( GEN_SEPERATOR )-1)]
            
            if j == 0:
                # First segment
                nameList.append( "\"{0}".format( segment.capitalize() ) )
            elif j == (length-1):
                # Last segment
                if GEN_USE_SEPERATOR == True:
                    if random.randint( 0, 100 ) < GEN_SEPERATOR_CHANCE:
                        nameList.append( "{0}{1}\"".format(seperator, segment) )
                    else:
                        nameList.append( "{0}\"".format( segment ) )
                else:
                    nameList.append( "{0}\"".format( segment ) )
            else:
                # Other segments
                if GEN_USE_SEPERATOR == True:
                    if random.randint( 0, 100 ) < GEN_SEPERATOR_CHANCE:
                        nameList.append( "{0}{1}".format(seperator, segment) )
                    else:
                        nameList.append( "{0}".format(segment) )
                else:
                    nameList.append( "{0}".format(segment) )
            
        name = "".join( nameList )
        
        # Check if the name has already been made
        if name in additionsList:
            #print( "Duplicate name" )
            i = i - 1
        else:    
            additionsList.append( name )
        
        #print( nameList )
        #print( name )

        # Culture
        cultureNames.write( "{0} ".format( name ) )
        
        # Monarch
        if random.randint( 0, 100 ) > GEN_FEMALE_CHANCE:
            # Make male
            monarchNames.write( "\t{0} = 20\n".format( name ) )
        else:
            # Make female
            monarchNames.write( "\t{0} = -20\n".format( name ) )
        
        # Leader
        leaderNames.write( "\t{0}\n".format( name ) )
if __name__ == "__main__":
    main()