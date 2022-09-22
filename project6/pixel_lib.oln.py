"""
Project 6 - Pixel Magic

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

"""
CONTRACT | encodePixel : str int int -> str
--------:|:--------------------------------------------------------------------
PURPOSE  | take in the str `pixel` and multiplies the values by different factors of `row` and `col`
EFFECTS  | none/none
EXAMPLES | "0 0 1" 1 2 -> "0 0 21952"
		 | "1 0 0" 4 6 -> "77 0 0"
		 | "0 1 0" 3 3 -> "0 2304 0"
"""
# multiply the first value of str by (the index of column + 3) and (the index of row + 5)
 
# multiply the second value by the same factor squared
 
# multiply the third value by the same factor cubed

# create a new string consisting of the new values

# return that string

"""
CONTRACT | decodePixel : str int int -> str
--------:|:--------------------------------------------------------------------
PURPOSE  | take in the str `pixel` and divides the values by different factors of `row` and `col`
EFFECTS  | none/none
EXAMPLES | "0 0 21952" 1 2 -> "0 0 1"
		 | "77 0 0" 4 6 -> "1 0 0"
		 | "0 2304 0" 3 3 -> "0 1 0"
"""
# divide the first value of str by (the index of column + 3) and (the index of row + 5)
 
# divide the second value by the same factor squared
 
# divide the third value by the same factor cubed

# create a new string consisting of the new values

# return that string

 