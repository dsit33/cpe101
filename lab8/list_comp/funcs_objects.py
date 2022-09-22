from math import sqrt

def distance(pt1, pt2):
	return sqrt((pt2.x - pt1.x)**2 + (pt2.y - pt1.y)**2)

def circles_overlap(circ1, circ2):
	return distance(circ1.center, circ2.center) < circ1.radius + circ2.radius