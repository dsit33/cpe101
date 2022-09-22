import utility

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y, other.y)

class Circle:
	def __init__(self, center = Point(0, 0), radius = 0):
		self.center = center
		self.radius = radius