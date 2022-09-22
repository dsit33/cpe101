from objects import *
from funcs_objects import *

def distance_all(lst):
	return [distance(n, Point(0, 0)) for n in lst]

def are_in_first_quadrant(lst):
	return [n for n in lst if n.x > 0 and n.y > 0]