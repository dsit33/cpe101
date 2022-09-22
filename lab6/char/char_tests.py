import unittest
from char import *

class TestChar(unittest.TestCase):
	def test_is_lower_101_1(self):
		self.assertTrue(is_lower_101("a"))
	def test_is_lower_101_2(self):
		self.assertFalse(is_lower_101("Y"))

	def test_char_rot_13_1(self):
		self.assertEqual(char_rot_13("a"), "n")
	def test_char_rot_13_2(self):
		self.assertEqual(char_rot_13("A"), "N")
	def test_char_rot_13_3(self):
		self.assertEqual(char_rot_13("4"), "4")
      


if __name__ == '__main__':
   unittest.main()

