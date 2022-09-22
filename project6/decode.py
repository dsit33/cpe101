"""
Project 6 - Pixel Magic

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""
from pixel_io import *
from pixel_lib import *
import sys

numCol = 0
colorVal = 0
pixel = [None, None, None]
count = 0

file = sys.argv[len(sys.argv)-1]
# get the text from the command line to check the file name
printUsage(file)
# pass the input through printUsage
f = open(file, 'r')
# open the file for reading
newFile = open("{}_decoded.ppm".format(file[0:len(file)-4]),"w+")
# create new file to write pixels to
for i, line in enumerate(f):
# run a for loop that reads information broken up by white space
	lineLst = line.split()
	if i == 0:
		newFile.write("P3\n")
	if i == 1:
		numCol = int(lineLst[0])
		newFile.write(lineLst[0]+" ")
		newFile.write(lineLst[1]+"\n")
	# store the second element of the file as the number of columns of pixels

	# store the third element of the file as the number of rows of pixels
	if i == 2:
		colorVal = line[0:len(line)-1]
		newFile.write("{}".format(line[0:len(line)-1]) + "\n")
	# store the fourth element of the file as the value that represents a colored pixel
	if i >= 3:
		for j, item in enumerate(lineLst):
			if pixel[0] == None:
				pixel[0] = lineLst[j]
			elif pixel[1] == None:
				pixel[1] = lineLst[j]
			elif pixel[2] == None:
				pixel[2] = lineLst[j]
	# run a for loop that runs for the length of line and stores values in pixel
		if pixel[0] != None and pixel[1] != None and pixel[2] != None:
			newPixel = decodePixel(pixel, numCol, count)
		# decode the pixel
			writeOutPixel(newPixel, newFile)
			pixel = [None, None, None]
			count += 1
		# call writeOutPixel
f.close()
newFile.close()