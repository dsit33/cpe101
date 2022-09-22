import unittest
from objects import *

class TestCases(unittest.TestCase):
	def test_equality(self):
		pt1 = Point(3, 0)
		pt2 = Point(3, 0)
		self.assertEqual(pt1, pt2)


	def test_equality_2(self):
		pt1 = Point(4, 6)
		pt2 = Point(2, 7)
		self.assertNotEqual(pt1, pt2)

	def test_equality_3(self):
		circ1 = Circle(Point(3, 0), 4)
		circ2 = Circle(Point(3, 0), 4)
		self.assertEqual(circ1, circ2)

	def test_equality_4(self):
		circ1 = Circle(Point(6, 9), 4)
		circ2 = Circle(Point(4, 0), 4)
		self.assertNotEqual(circ1, circ2)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

