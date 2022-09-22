import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_max_101(self):
   		self.assertEqual(conditional.max_101(50, 1), 50)

   def test_max_101_2(self):
   		self.assertEqual(conditional.max_101(33, 33), 33)

   def test_max_of_three(self):
   		self.assertEqual(conditional.max_of_three(10, 43, 9), 43)

   def test_max_of_three2(self):
   		self.assertEqual(conditional.max_of_three(33, 4, 5), 33)

   def test_rental_late_fee(self):
   		self.assertEqual(conditional.rental_late_fee(0), 0)

   def test_rental_late_fee2(self):
   		self.assertEqual(conditional.rental_late_fee(7), 5)

   def test_rental_late_fee3(self):
   		self.assertEqual(conditional.rental_late_fee(11), 7)

   def test_rental_late_fee4(self):
   		self.assertEqual(conditional.rental_late_fee(24), 19)

   def test_rental_late_fee5(self):
   		self.assertEqual(conditional.rental_late_fee(69), 100)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

