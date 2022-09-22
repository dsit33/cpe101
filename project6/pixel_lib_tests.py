import unittest
from pixel_lib import *


class TestCases(unittest.TestCase):

    def test_encodePixel_1(self):
        self.assertEqual(encodePixel([0, 0, 1], 2, 0), [0, 225, 0])

    def test_encodePixel_2(self):
        self.assertEqual(encodePixel([1, 0, 0], 6, 20), [0, 0, 64000])

    def test_encodePixel_3(self):
        self.assertEqual(encodePixel([0, 1, 0], 3, 7), [28, 0, 0])
    def test_encodePixel_4(self):
        self.assertEqual(encodePixel([255, 0, 0], 3, 0), [0, 0, 860625])


    def test_decodePixel_1(self):
        self.assertEqual(decodePixel([0, 255, 0], 2, 0), [0, 0, 1])

    def test_decodePixel_2(self):
        self.assertEqual(decodePixel([0, 0, 64000], 6, 20), [1, 0, 0])

    def test_decodePixel_3(self):
        self.assertEqual(decodePixel([28, 0, 0], 3, 7), [0, 1, 0])


if __name__ == '__main__':
    unittest.main()
