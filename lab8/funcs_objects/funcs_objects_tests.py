import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
	def test_point(self):
		point = Point(3, 5)
		self.assertEqual(point.x, 3)
		self.assertEqual(point.y, 5)


	def test_circle(self):
		circle = Circle(Point(6, 9), 4)
		self.assertEqual(circle.center.x, 6)
		self.assertEqual(circle.center.y, 9)
		self.assertEqual(circle.radius, 4)

	def test_distance_1(self):
		point1 = Point(0, 3)
		point2 = Point(4, 0)
		self.assertAlmostEqual(distance(point1, point2), 5)

	def test_distance_2(self):
		point1 = Point(6, 9)
		point2 = Point(4, 20)
		self.assertAlmostEqual(distance(point1, point2), 11.1803399)

	def test_circles_overlap_1(self):
		circ1 = Circle(Point(0, 4), 3)
		circ2 = Circle(Point(3, 0), 4)
		self.assertTrue(circles_overlap(circ1, circ2))

	def test_circles_overlap_2(self):
		circ1 = Circle(Point(6, 9), 5)
		circ2 = Circle(Point(-1, -4), 2)
		self.assertFalse(circles_overlap(circ1, circ2))


   # Add other testing functions


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

