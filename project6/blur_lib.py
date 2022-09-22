"""
Project 6 - Pixel Magic, Part 2

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

from pixel import *
from math import sqrt
from blur_io import *

################################################################################
############ ALL Functions in This File MUST be 100% Unit Tested! ##############
################################################################################

# Required Functions with Provided Unit Tests (5 total)

def process_command_line_args(args):
    for i, item in enumerate(args):
    	if i == 0 and item.find(".ppm") == -1:
    		return None
    	if i == 1:
    		nums = args[i:]
    		for num in nums:
    			if not num.replace("-", "1").isdigit():
    				return None
    if len(args) == 5:
    	return {'file': str(args[0]), 
    	'row': int(args[1]), 
    	'col': int(args[2]), 
    	'radius': int(args[3]), 
    	'reach': int(args[4])}
    elif len(args) == 4:
    	return {'file': str(args[0]), 'row': int(args[1]), 'col': int(args[2]), 'radius': int(args[3]), 'reach': 4}
    else:
    	return None


def build_output_file_path(input_file_path):
    if input_file_path.find(".ppm") == -1:
    	return None
    else:
    	return "{}_blurred.ppm".format(input_file_path[0:-4])


def cast_all_to_ints(lst):
    newLst = []
    for item in lst:
    	try:
    		newLst.append(int(item))
    	except:
    		return None
    return newLst


def get_pixels_from_groups_of_3(groups):
    pixelList = []
    leftovers = []
    for i, group in enumerate((groups)):
    	if len(group) == 3:
    		newPix = Pixel(group[0], group[1], group[2])
    		pixelList.append(newPix)
    	if len(group) < 3 and i == len(groups) - 1:
    		leftovers = group
    return pixelList, leftovers


def get_image_dimensions_from_header_lines(header_lines):
    dims = header_lines[1].split()
    try:
    	height = int(dims[0])
    	width = int(dims[1])
    except:
    	return None
    return (height, width)


# Required Functions You Must Write Unit Tests For (3 total)

def groups_of_3(list_of_ints):
    final = []
    group = []
    for i, num in enumerate(list_of_ints):
    	group.append(num)
    	if len(group) == 3:
    		final.append(group)
    		group = []
    	elif i == len(list_of_ints) - 1:
    		final.append(group)
    return final


def get_reach_for_pixel_location(blur_params, pixel_row, pixel_col):
    #if distance(blur_params['row'], blur_params['col'], pixel_row, pixel_col) > int(blur_params['radius']) * 2:
    	#return None
    if distance(blur_params['row'], blur_params['col'], pixel_row, pixel_col) <= int(blur_params['radius']):
    	return int(blur_params['reach'])
    elif distance(blur_params['row'], blur_params['col'], pixel_row, pixel_col) > int(blur_params['radius']) and distance(blur_params['row'], blur_params['col'], pixel_row, pixel_col) <= int(blur_params['radius'])*2:
    	return int((1 - ((distance(blur_params['row'], blur_params['col'], pixel_row, pixel_col)) - int(blur_params['radius'])) / int(blur_params['radius'])) * int(blur_params['reach']))


def get_blurred_pixel(orig_image_pixels, row, col, reach):
    count = 0
    averageColor = [0, 0, 0]
    for y in range(row - reach, row + reach + 1):
    	if y >= 0 and y < len(orig_image_pixels):
    		for x in range(col - reach, col + reach + 1):
    			if x >= 0 and x < len(orig_image_pixels[0]):
    				averageColor[0] += orig_image_pixels[y][x].r
    				averageColor[1] += orig_image_pixels[y][x].g
    				averageColor[2] += orig_image_pixels[y][x].b
    				count += 1
    return Pixel(averageColor[0]//count, averageColor[1]//count, averageColor[2]//count)

def distance(row1, col1, row2, col2):
	return sqrt((int(row1) - int(row2))**2 + (int(col1) - int(col2))**2)



