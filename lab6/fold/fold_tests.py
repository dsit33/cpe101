import unittest
from fold import *

class TestCases(unittest.TestCase):
	def test_sum_1(self):
		self.assertEqual(sum([1, 2, 3, 4, 5]), 15)
	def test_sum_2(self):
		self.assertEqual(sum([0, 4, 6, 2]), 12)

	def test_index_of_smallest_1(self):
		self.assertEqual(index_of_smallest([9, 13, 7, 394, 0, -4]), 5)
	def test_index_of_smallest_2(self):
		self.assertEqual(index_of_smallest([100, 6, 1, 18]), 2)
	def test_index_of_smallest_3(self):
		self.assertEqual(index_of_smallest([]), -1)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

