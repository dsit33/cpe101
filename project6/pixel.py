"""
Project 6 - Pixel Magic, Part 2

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""


class Pixel:
    # You Do NOT Need to Unit Test the Methods of class Pixel.
    def __init__(self, r, g, b):
    	self.r = r
    	self.g = g
    	self.b = b

    def __repr__(self):
    	return "{} ".format(self.r) + "{} ".format(self.g) + "{}".format(self.b)

    def __eq__(self, other):
    	return self.r == other.r and self.g == other.g and self.b == other.b