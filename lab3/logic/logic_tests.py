"""
Name: Derek Sit
Instructor: Mike Ryu
Section: 13

"""
import unittest
import logic

class TestCases(unittest.TestCase):
   def test_is_even(self):
      	self.assertTrue(logic.is_even(2))

   def test_is_even2(self):
   		self.assertFalse(logic.is_even(5))

   def test_is_an_interval(self):
   		self.assertTrue(logic.is_an_interval(2))

   def test_is_an_interval2(self):
   		self.assertTrue(logic.is_an_interval(50))

   def test_is_an_interval3(self):
   		self.assertTrue(logic.is_an_interval(19))		
      
   def test_is_an_interval4(self):
   		self.assertTrue(logic.is_an_interval(102))

   def test_is_an_interval5(self):
   		self.assertFalse(logic.is_an_interval(9))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

