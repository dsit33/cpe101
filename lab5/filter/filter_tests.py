import unittest
import filter

class TestCases(unittest.TestCase):
	def assertListAlmostEqual(self, l1, l2):
		self.assertEqual(len(l1), len(l2))
		for el1, el2 in zip(l1, l2):
			self.assertAlmostEqual(el1, el2)

	def test_are_positive_1(self):
      # Add code here
		self.assertListAlmostEqual(filter.are_positive([1, 2, 3]), [1, 2,3])
	def test_are_positive_2(self):
		self.assertListAlmostEqual(filter.are_positive([1, -2, 3]), [1, 3])

	def test_are_greater_than_n_1(self):
		self.assertListAlmostEqual(filter.are_greater_than_n([1, 2, 3], 5), [])
	def test_are_greater_than_n_2(self):
		self.assertListAlmostEqual(filter.are_greater_than_n([40.2, 9.1, 0.5], 6.3), [40.2, 9.1])

	def test_are_divisible_by_n_1(self):
		self.assertListAlmostEqual(filter.are_divisible_by_n([3, 6, 7, 9, 10], 3), [3, 6, 9])
	def test_are_divisible_by_n_2(self):
		self.assertListAlmostEqual(filter.are_divisible_by_n([4, 8, 2, 5, 100], 4), [4, 8, 100])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

