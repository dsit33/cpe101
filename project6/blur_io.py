"""
Project 5 - Pixel Magic, Part 2

Name:
Instructor: Mike Ryu
Section: 13
"""
from blur_lib import *

# You Do NOT Need to Unit Test Any of The Following Functions

def read_lines_from_image(file_path):
	f = open("{}".format(file_path), "r")
	return f.readlines()


def open_output_file(file_path):
	f = open("{}".format(file_path), "w")
	return f


def write_header_to_output_file(output_file, header_lines):
    output_file.write(header_lines[0])
    output_file.write(header_lines[1])
    output_file.write(header_lines[2])


def write_pixel_to_output_file(output_file, pixel):
    output_file.write("{} ".format(pixel.r) + "{} ".format(pixel.g) + "{}".format(pixel.b))


def print_usage_info():
   	print("Usage: python blur.py <image.ppm> <row> <col> <radius> <reach>") 


def print_file_io_error(file_path):
    print("Unable to open {}".format(file_path))


def print_file_format_error(line_num, file_path):
    print("Invalid formatting at line {} in {}".format(line_num, file_path))
