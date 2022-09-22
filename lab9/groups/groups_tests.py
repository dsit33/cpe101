import unittest
from groups import *

class TestCases(unittest.TestCase):
	def test_groups_of_3(self):
		vals = [1,2,3,4,5,6,7]
		final = [[1,2,3],[4,5,6],[7]]
		self.assertEqual(groups_of_3(vals), final)

	def test_groups_of_3_2(self):
		vals = [6,9,4,2,0]
		final = [[6,9,4],[2,0]]
		self.assertEqual(groups_of_3(vals), final)

	def test_groups_of_3_3(self):
		vals = [0,0,0,0,0,0,0,0,0]
		final = [[1,2,3],[4,5,6]]
		self.assertNotEqual(groups_of_3(vals), final)

if __name__ == '__main__':
	unittest.main()