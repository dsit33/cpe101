import unittest
from funcs import *


class TestCases(unittest.TestCase):

    def test_poundsToKG_1(self):
        self.assertAlmostEqual(poundsToKG(1.0), 0.453592)

    def test_poundsToKG_2(self):
        self.assertAlmostEqual(poundsToKG(140.0), 63.50288)

    def test_poundsToKG_3(self):
        self.assertAlmostEqual(poundsToKG(100.0), 45.3592)


    def test_getMassObject_1(self):
        self.assertEqual(getMassObject('t'), 0.1)

    def test_getMassObject_2(self):
        self.assertEqual(getMassObject('p'), 1.0)

    def test_getMassObject_3(self):
        self.assertEqual(getMassObject('r'), 3.0)

    def test_getMassObject_4(self):
        self.assertEqual(getMassObject('g'), 5.3)

    def test_getMassObject_5(self):
        self.assertEqual(getMassObject('l'), 9.07)

    def test_getMassObject_6(self):
        self.assertEqual(getMassObject('s'), 0.0)


    def test_getVelocityObject_1(self):
        self.assertAlmostEqual(getVelocityObject(1.0), 2.2135943621178655)

    def test_getVelocityObject_2(self):
        self.assertAlmostEqual(getVelocityObject(17.0), 9.126883367283709)

    def test_getVelocityObject_3(self):
        self.assertAlmostEqual(getVelocityObject(22.0), 10.38267788)


    def test_getVelocitySkater_1(self):
        self.assertAlmostEqual(getVelocitySkater(63.50288, 1.0, 2.2135943), 0.03485817)

    def test_getVelocitySkater_2(self):
        self.assertAlmostEqual(getVelocitySkater(45.3592, 5.3, 9.1268833), 1.0664315)


if __name__ == '__main__':
    unittest.main()
