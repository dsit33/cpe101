import unittest
import map

class TestCases(unittest.TestCase):
	def assertListAlmostEqual(self, l1, l2):
		self.assertEqual(len(l1), len(l2))
		for el1, el2 in zip(l1, l2):
			self.assertAlmostEqual(el1, el2)

	def test_square_all_1(self):
      # Add code here
		self.assertListAlmostEqual(map.square_all([1, 2, 3]), [1, 4, 9])
	def test_square_all_2(self):
		self.assertListAlmostEqual(map.square_all([4, 5, 6]), [16, 25, 36])

	def test_add_n_all_1(self):
		self.assertListAlmostEqual(map.add_n_all([1, 2, 3], 5), [6, 7, 8])
	def test_add_n_all_2(self):
		self.assertListAlmostEqual(map.add_n_all([4.2, 9.1, 0.5], 6.3), [10.5, 15.4, 6.8])

	def test_even_or_odd_all_1(self):
		self.assertListAlmostEqual(map.even_or_odd_all([1, 6, 7, 5, 10]), [False, True, False, False, True])
	def test_even_or_odd_all_2(self):
		self.assertListAlmostEqual(map.even_or_odd_all([4, 8, 2, 5, 100]), [True, True, True, False, True])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

