"""
Project 6 - Pixel Magic

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

from math import sqrt

def printUsage(file):
    """
    CONTRACT | printUsage : str -> none
    PURPOSE  | read in file and print out a statement depending on whether or not a file was provided
    EXAMPLES | n/a
    """
    if file.find(".ppm") == -1:
        print("Usage: python encode.py <image.ppm>")
        exit()
    try:
        f = open(file)
    except:
        print("Unable to open <{}>".format(file))
        exit()
    f.close()

    # if no file was passed through

        # print out the "Usage: python encode.py <image.ppm>"

        # exit code

    # try to open the file

    # use an except that will occur if the file name doesn't exist

        # print out "Unable to open <image.ppm>"

        # exit code


def writeOutPixel(pixel, f):
    """
    CONTRACT | writeOutPixel : str str -> none
    PURPOSE  | take in a str pixel and str file write out the information to a ppm file
    EXAMPLES | n/a
    """
    f.write("{}".format(pixel[0])+" {}".format(pixel[1])+" {}".format(pixel[2])+"\n")


    # create a new file with the name_of_the_picture_encoded.ppm

    # write out the pixel to the file

    # close the file


