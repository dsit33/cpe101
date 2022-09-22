import unittest
import poly

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   # Add tests here
   def test_poly_add2(self):
   		self.assertListAlmostEqual(poly.poly_add2([2, 3.1, 2.7], [3, -4.2, 1]), [5, -1.1, 3.7])

   def test_poly_add2_2(self):
   		self.assertListAlmostEqual(poly.poly_add2([2.3, 4.7, 1.0], [1.2, 2.1, -3.2]), [3.5, 6.8, -2.2])

   def test_poly_mult2(self):
   		self.assertListAlmostEqual(poly.poly_mult2([1, 1, 1], [1, 1, 1]), [1, 2, 3, 2, 1])

   def test_poly_mult2_2(self):
   		self.assertListAlmostEqual(poly.poly_mult2([-4, 0, 1], [-4, 0, 1]), [16, 0, -8, 0, 1])


if __name__ == '__main__':
   unittest.main()
