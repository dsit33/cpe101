import unittest
from string_101 import *

class TestString(unittest.TestCase):
	def test_str_rot_13_1(self):
		self.assertEqual(str_rot_13("aaa"), "nnn")
	def test_str_rot_13_2(self):
		self.assertEqual(str_rot_13("A4AA"), "N4NN")

	def test_str_translate_101_1(self):
		self.assertEqual(str_translate_101("abcdcba", "a", "x"), "xbcdcbx")
	def test_str_translate_101_2(self):
		self.assertEqual(str_translate_101("suh dude", "u", "r"), "srh drde")

if __name__ == '__main__':
   unittest.main()

