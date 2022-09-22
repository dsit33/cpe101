"""
Project 1

Name: Boaty Derek Sit
Instructor: Mike Ryu
Section: 13
"""

from math import sqrt

def poundsToKG(pounds):
    """
    CONTRACT | poundsToKG : float -> float
    PURPOSE  | take in the users input 'pounds' and converts it to 'kg'
    EXAMPLES | 1 -> .453592
    		 | 140 -> 63.50288
    		 | 100 -> 45.3592
    """
    return pounds * .453592

    # first-outline


def getMassObject(object):
    """
    CONTRACT | getMassObject : str -> float
    PURPOSE  | reads 'object' the user picked up and determines the mass of the object in kg
    EXAMPLES | t -> .1
    		 | p -> 1.0
    		 | r -> 3.0
    		 | g -> 5.3
    		 | l -> 9.07
    		 | s -> 0.0
    """
    if object == 't':
        return .1
    elif object == 'p':
        return 1.0
    elif object == 'r':
        return 3.0
    elif object == 'g':
        return 5.3
    elif object == 'l': 
        return 9.07
    else:
        return 0.0

    # second-outline


def getVelocityObject(distance):
    """
    CONTRACT | getVelocityObject : float -> float
    PURPOSE  | take in parameter 'distance' and calculate the velocity of the object in m/s
    EXAMPLES | 1 -> 2.2135943
    		 | 17 -> 9.1268833
    		 | 22 -> 10.3826778
    """
    return sqrt(9.8 * distance / 2)

    # third-outline


def getVelocitySkater(massSkater, massObject, velObject):
    """
    CONTRACT | getVelocitySkater : float float float -> float
    PURPOSE  | take in parameters 'massSkater', 'massObject', and 'velObject' and calculate the velocity of the skater after the throw
    EXAMPLES | 63.50288 1.0 2.2135943 -> .03485817
    		 | 45.3592 5.3 9.1268833 -> 1.0664315
    """
    return massObject * velObject / massSkater


