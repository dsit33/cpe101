import unittest
from landerFuncs import *


class TestCases(unittest.TestCase):

    def test_updateAcceleration_1(self):
        self.assertAlmostEqual(updateAcceleration(1.62, 4), -0.324)

    def test_updateAcceleration_2(self):
        self.assertAlmostEqual(updateAcceleration(1.62, 7), 0.648)


    def test_updateAltitude_1(self):
        self.assertAlmostEqual(updateAltitude(500.0, 3.0, 0.6), 503.3)

    def test_updateAltitude_2(self):
        self.assertAlmostEqual(updateAltitude(6032.0, 20.0, 0.3), 6052.15)


    def test_updateVelocity_1(self):
        self.assertAlmostEqual(updateVelocity(20.4, 0.65), 21.05)

    def test_updateVelocity_2(self):
        self.assertAlmostEqual(updateVelocity(12.46, -0.71), 11.75)


    def test_updateFuel_1(self):
        self.assertEqual(updateFuel(50, 7), 43)

    def test_updateFuel_2(self):
        self.assertEqual(updateFuel(33, 8), 25)


if __name__ == '__main__':
    unittest.main()
