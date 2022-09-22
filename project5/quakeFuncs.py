"""
Project 5 - Earthquakes

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""
from urllib.request import *
from json import *
from datetime import *
from operator import *
from utility import *


### GIVEN FUNCTIONS ############################################################
# Use the below two as-is and DO NOT change them ###############################
################################################################################

def get_json(url):
    """
    CONTRACT | get_json : str -> dict
    PURPOSE  | Given a `url` of a website, returns a JSON dictionary.
    EFFECTS  | Website/None
    EXAMPLES | n/a
    """
    with urlopen(url) as response:
        html = response.read()
    html_str = html.decode("utf-8")
    return loads(html_str)


def time_to_str(time):
    """
    CONTRACT | time_to_str : int -> str
    PURPOSE  | Given an epoch-based UNIX `time`, formats it to a string.
    EFFECTS  | None/None
    EXAMPLES | 0 -> '1969-12-31 16:00:00' # ONLY VALID in UTC-8 (PST) timezone!
             | 1519793864 -> '2018-02-27 20:57:44'    # Again, in PST timezone!
    """
    return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')


################################################################################
# Use the above two as-is and DO NOT change them ###############################
######################################################################## END ###


# Fill in the class definition here.
class Earthquake():
    """
    A class to represent an occurrence of an earthquake.
    Attributes:
        place - string, where it occurred
        mag - float, magnitude of it
        longitude - float, longitude of the origin
        latitude - float, latitude of the origin
        time - int, UNIX posix time in seconds of when it occurred
    """
    def __init__(self, place, mag, longitude, latitude, time):
        self.place = place
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time

    def __eq__(self, other):
        return self.place == other.place and epsilon_equal(self.mag, other.mag) and epsilon_equal(self.longitude, other.longitude) and epsilon_equal(self.latitude, other.latitude) and epsilon_equal(self.time, other.time)

    def __str__(self):
        return "({:.2f})".format(self.mag) + " {:>40} at".format(self.place) + " {}".format(time_to_str(self.time)) + " ({:8.3f},".format(self.longitude) + " {:6.3f})".format(self.latitude)

# Required function - implement me!
def read_quakes_from_file(filename):
    """
    CONTRACT | read_quakes_from_file : str -> list
    PURPOSE  | Reads quakes from given `filename` and returns a list of Earthquakes.
    EFFECTS  | file/None
    """
    lst = []
    file = open(filename)
    for line in file:
        inp = line.split()
        lst.append(Earthquake(' '.join(inp[4:len(inp)]), float(inp[0]), float(inp[1]), float(inp[2]), int(inp[3])))
    file.close()
    return lst


# Required function - implement me!
def filter_by_mag(quakes, low, high):
    """
    CONTRACT | filter_by_mag : list float float -> list
    PURPOSE  | Given a list of `quakes`, `low`, and `high` magnitudes, returns 
             |     only the quakes that had magnitudes between the given 
             |     low and high values (inclusive).
    EFFECTS  | None/None
    """
    final = []
    for quake in quakes:
        if quake.mag >= float(low) and quake.mag <= float(high):
            final.append(quake)
    return final


# Required function - implement me!
def filter_by_place(quakes, word):
    """
    CONTRACT | filter_by_place : list str -> list
    PURPOSE  | Given a list of `quakes` and `word` to search within the place
             |     attribute of the quakes, returns only the quakes that have
             |     the given word inside of the place attribute.
    EFFECTS  | None/None
    """
    final = []
    for quake in quakes:
        string = quake.place.lower()
        if string.find(word.lower()) != -1:
            final.append(quake)
    return final


# Required function for final part - implement me too!
def quake_from_feature(feature):
    """
    CONTRACT | quake_from_feature : dict -> Earthquake
    PURPOSE  | Given a `feature` dictionary from the USGS website, constructs
             |     and returns a corresponding Earthquake object.
    EFFECTS  | None/None
    """
    return Earthquake(feature["properties"]["place"], float(feature["properties"]["mag"]), float(feature["geometry"]["coordinates"][0]), float(feature["geometry"]["coordinates"][1]), int(feature["properties"]["time"]/1000))



