class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Circle:
	def __init__(self, center = Point(0, 0), radius = 0):
		self.center = center
		self.radius = radius