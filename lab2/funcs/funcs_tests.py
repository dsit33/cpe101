import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
      # Add code here. REMOVE PASS
      self.assertEqual(funcs.f(1.0), 9.0)

      
   def test_f_2(self):
      # Add code here. REMOVE PASS
      self.assertEqual(funcs.f(3.0), 69.0)


   def test_g_1(self):
      # Add code here. REMOVE PASS
      self.assertAlmostEqual(funcs.g(1.0, 2.0), 1.66666666666)
      
   def test_g_2(self):
      # Add code here. REMOVE PASS
      self.assertAlmostEqual(funcs.g(1.0, 3.0), 3.33333333333)
   
   def test_hypotenuse_1(self):
      self.assertAlmostEqual(funcs.hypotenuse(3.0, 4.0), 5.0)

   def test_hypotenuse_2(self):
      self.assertAlmostEqual(funcs.hypotenuse(5.0, 12.0), 13.0)

   def test_is_positive_1(self):
      self.assertTrue(funcs.is_positive(1))   

   def test_is_positive_2(self):
      self.assertFalse(funcs.is_positive(-1))      
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

