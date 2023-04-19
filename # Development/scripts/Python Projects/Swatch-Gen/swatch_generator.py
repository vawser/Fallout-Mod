# "C:\Program Files (x86)\Python_3_5_1\python.exe" "C:\Users\guest-new\Documents\Python\projects\Swatch Generator\swatch_generator.py"

import os
import sys
import random
import time
import colorsys

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))
	
class ColourList:
	def __init__(self, definitionFile):
		self.currentColours = []
		self.usedColours = []
		self.definitionFile = definitionFile

	def addColour(self, item):
		if item in self.usedColours:
			print( "Repeat colour found:  {0}".format( item ) )
			return False
		else:
			self.currentColours.append( item )
			self.usedColours.append( item )	
			return True

	def extractColour(self):
		with open( self.definitionFile, "rt" ) as sourceFile:
			text = sourceFile.readlines()
			
		for i in range( len( text )  ):
			temp_string = text[i].split( ";" )
			id = temp_string[0]
			r = temp_string[1]
			g = temp_string[2]
			b = temp_string[3]
			
			colourList = [ r, g, b ]
			self.usedColours.append( colourList )
		
	def getCurrentColours(self):
		return self.currentColours
		
	def getUsedColours(self):
		return self.usedColours
		
class SwatchSet:
	def __init__(self):
		self.rgb = [ 0, 0, 0 ]
		self.hsv = [ 0, 0, 0 ]
		
	def setRandomRGB(self):
		self.rgb[0] = random.randint( 256 )
		self.rgb[1] = random.randint( 256 )
		self.rgb[2] = random.randint( 256 )
	
	def setRandomHSV( self, hue, minSat, maxSat, minValue, maxValue ):
		self.hsv[0] = hue
		self.hsv[1] = random.uniform( minSat, maxSat )
		self.hsv[2] = random.uniform( minValue, maxValue )
		
	def setHSVtoRGB(self):
		self.hsv = colorsys.rgb_to_hsv( self.rgb[0], self.rgb[1], self.rgb[2] )
		
	def setRGBtoHSV(self):
		rgbTuple = colorsys.hsv_to_rgb( self.hsv[0], self.hsv[1], self.hsv[2] )
		
		# Denormalize
		for i in range( len( self.rgb ) ):
			self.rgb[i] = int(rgbTuple[i] * 255)
		
	def getRGB(self):
		return self.rgb
		
	def getHSV(self):
		return self.hsv
	
def main():
	swatchSet = SwatchSet()
	colourList = ColourList( getScriptPath() + "\definition.csv" )
	colourList.extractColour()
	#print( colourList.getUsedColours() )
	
	newDefinitionFile = open( "definition_new.csv", "wt" )
	newSwatchFile = open( "new_swatch.css", "wt" )
	
	minimumCount = 1740
	maximumCount = 2000
	iterations = maximumCount - 1740
	index = 0
	
	while index < iterations:
		swatchSet.setRandomHSV( 0.6, 0.2, 1, 0.2, 1 )
		print( swatchSet.getHSV() )
		swatchSet.setRGBtoHSV()
		print( swatchSet.getRGB() )
		
		if colourList.addColour( swatchSet.getRGB() ) == True:
			index = index + 1
	
	newColourList = colourList.getCurrentColours()
	
	for i in range( minimumCount, maximumCount ):
		newSwatchFile,write( "rgb({0},{1},{2})\n".format( newColourList[i][0], newColourList[i][1], newColourList[i][2]) )
		
	#time.sleep( 100 )
	

if __name__ == "__main__":
	main()