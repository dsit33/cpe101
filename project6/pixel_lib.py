"""
Project _

Name: Boaty MacBoatface
Instructor: Mike Ryu
Section: __
"""

from math import sqrt

def encodePixel(pixel, col, count):
    """
    CONTRACT | encodePixel : str int int -> str
    PURPOSE  | take in the str pixel and multiplies the values by different factors of row and col
    EXAMPLES | "0 0 1" 2 0 -> "0 225 0"
    		 | "1 0 0" 6 20 -> "0 0 64000"
    		 | "0 1 0" 3 7 -> "28 0 0"
    """
    newPix = [0, 0, 0]
    newPix[0] = int(pixel[1]) * (count%col + 3) * (count//col + 5)
    # multiply the first value of str by (the index of column + 3) and (the index of row + 5)
    newPix[1] = int(pixel[2]) * ((count%col + 3) * (count//col + 5))**2
    # multiply the second value by the same factor squared
    newPix[2] = int(pixel[0]) * ((count%col + 3) * (count//col + 5))**3
    # multiply the third value by the same factor cubed
    return newPix
    # return that list


def decodePixel(pixel, col, count):
    """
    CONTRACT | decodePixel : str int int -> str
    PURPOSE  | take in the str pixel and divides the values by different factors of row and col
    EXAMPLES | "0 255 0" 2 0 -> "0 0 1"
    		 | "0 0 64000" 6 20 -> "1 0 0"
    		 | "28 0 0" 3 7 -> "0 1 0"
    """
    newPix = [0, 0, 0]
    newPix[0] = int(int(pixel[2]) / ((count%col + 3) * (count//col + 5))**3)
    # divide the first value of str by (the index of column + 3) and (the index of row + 5)
    newPix[1] = int(int(pixel[0]) / ((count%col + 3) * (count//col + 5)))
    # divide the second value by the same factor squared
    newPix[2] = int(int(pixel[1]) / ((count%col + 3) * (count//col + 5))**2)
    # divide the third value by the same factor cubed
    return newPix
    # return that list

