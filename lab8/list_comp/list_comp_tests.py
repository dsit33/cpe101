import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
	def assertListAlmostEqual(self, l1, l2):
		self.assertEqual(len(l1), len(l2))
		for el1, el2 in zip(l1, l2):
			self.assertAlmostEqual(el1, el2)
	def test_1(self):
		lst = [Point(0, 3), Point(4, 0), Point(3, 4)]
		self.assertListAlmostEqual(distance_all(lst), [3, 4, 5])
	def test_2(self):
		lst = [Point(5, 12), Point(6, 8)]
		self.assertListAlmostEqual(distance_all(lst), [13, 10])

	def test_3(self):
		lst = [Point(4, 5), Point(-6, 9), Point(4, -20), Point(1, 1)]
		self.assertListAlmostEqual(are_in_first_quadrant(lst), [Point(4, 5), Point(1, 1)])
	def test_4(self):
		lst = [Point(-3, -8)]
		self.assertListAlmostEqual(are_in_first_quadrant(lst), [])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

