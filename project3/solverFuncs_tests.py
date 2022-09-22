import unittest
import solverFuncs


class TestCases(unittest.TestCase):

    def test_check_valid_1(self):
        self.assertTrue(solverFuncs.check_valid([[1, 5, 4, 2, 3], [3, 1, 2, 4, 5], [4, 2, 5, 3, 1], [5, 4, 3, 1, 2], [2, 3, 1, 5, 4]], [[5, 3, 0, 5, 6], [9, 2, 1, 2], [14, 4, 3, 4, 8, 9], [8, 3, 6, 11, 12], [9, 2, 10, 15], [4, 2, 13, 14], [12, 4, 16, 17, 20, 21], [7, 3, 18, 22, 23], [6, 2, 19, 24]]))

    def test_check_valid_2(self):
        self.assertFalse(solverFuncs.check_valid([[2, 4, 5, 3, 1], [3, 5, 4, 2, 1], [5, 1, 3, 2, 4], [4, 5, 2, 3, 4], [1, 5, 2, 4, 3]], [[5, 3, 0, 5, 6], [9, 2, 1, 2], [14, 4, 3, 4, 8, 9], [8, 3, 6, 11, 12], [9, 2, 10, 15], [4, 2, 13, 14], [12, 4, 16, 17, 20, 21], [7, 3, 18, 22, 23], [6, 2, 19, 24]]))

    def test_check_valid_3(self):
        self.assertFalse(solverFuncs.check_valid([[2, 4, 3, 1, 5], [5, 1, 4, 2, 3], [3, 2, 1, 5, 4], [4, 5, 2, 3, 1], [1, 3, 5, 4, 2]], [[11, 4, 0, 5, 6, 10], [11, 3, 1, 2, 7], [16, 5, 3, 4, 8, 9, 13], [10, 4, 11, 12, 16, 17], [7, 3, 14, 19, 24], [12, 4, 15, 20, 21, 22], [7, 2, 18, 23]]))

    def test_check_valid_4(self):
        self.assertFalse(solverFuncs.check_valid([[5, 4, 3, 1, 5], [2, 3, 4, 2, 3], [1, 2, 1, 5, 4], [4, 5, 2, 3, 1], [1, 3, 5, 4, 2]], [[11, 4, 0, 5, 6, 10], [11, 3, 1, 2, 7], [16, 5, 3, 4, 8, 9, 13], [10, 4, 11, 12, 16, 17], [7, 3, 14, 19, 24], [12, 4, 15, 20, 21, 22], [7, 2, 18, 23]]))

    def test_check_valid_5(self):
        self.assertTrue(solverFuncs.check_valid([[1, 5, 4, 2, 3], [3, 1, 2, 4, 5], [4, 2, 5, 3, 1], [5, 4, 3, 1, 0], [0, 0, 0, 0, 0]], [[5, 3, 0, 5, 6], [9, 2, 1, 2], [14, 4, 3, 4, 8, 9], [8, 3, 6, 11, 12], [9, 2, 10, 15], [4, 2, 13, 14], [12, 4, 16, 17, 20, 21], [7, 3, 18, 22, 23], [6, 2, 19, 24]]))


    def test_check_cages_valid_1(self):
        self.assertTrue(solverFuncs.check_cages_valid([[1, 5, 4, 2, 3], [3, 1, 2, 4, 5], [4, 2, 5, 3, 1], [5, 4, 3, 1, 2], [2, 3, 1, 5, 4]], [[5, 3, 0, 5, 6], [9, 2, 1, 2], [14, 4, 3, 4, 8, 9], [8, 3, 6, 11, 12], [9, 2, 10, 15], [4, 2, 13, 14], [12, 4, 16, 17, 20, 21], [7, 3, 18, 22, 23], [6, 2, 19, 24]]))

    def test_check_cages_valid_2(self):
        self.assertFalse(solverFuncs.check_cages_valid([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], [[5, 3, 0, 5, 6], [9, 2, 1, 2], [14, 4, 3, 4, 8, 9], [9, 3, 6, 11, 12], [9, 2, 10, 15], [4, 2, 13, 14], [12, 4, 16, 17, 20, 21], [7, 3, 18, 22, 23], [6, 2, 19, 24]]))

    def test_check_cages_valid_3(self):
        self.assertFalse(solverFuncs.check_cages_valid([[2, 4, 3, 1, 5], [5, 1, 4, 2, 3], [3, 2, 1, 5, 4], [4, 5, 2, 3, 1], [1, 3, 5, 4, 2]], [[11, 4, 0, 5, 6, 10], [11, 3, 1, 2, 7], [16, 5, 3, 4, 8, 9, 13], [10, 4, 11, 12, 16, 17], [7, 3, 14, 19, 24], [12, 4, 15, 20, 21, 22], [7, 2, 18, 23]]))

    def test_check_cages_valid_4(self):
        self.assertFalse(solverFuncs.check_cages_valid([[5, 4, 3, 1, 5], [2, 3, 4, 2, 3], [1, 2, 1, 5, 4], [4, 5, 2, 3, 1], [1, 3, 5, 4, 2]], [[11, 4, 0, 5, 6, 10], [11, 3, 1, 2, 7], [16, 5, 3, 4, 8, 9, 13], [10, 4, 11, 12, 16, 17], [7, 3, 14, 19, 24], [12, 4, 15, 20, 21, 22], [7, 2, 18, 23]]))


    def test_check_columns_valid_1(self):
        self.assertFalse(solverFuncs.check_columns_valid([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))

    def test_check_columns_valid_2(self):
        self.assertTrue(solverFuncs.check_columns_valid([[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]))

    def test_check_columns_valid_3(self):
        self.assertTrue(solverFuncs.check_columns_valid([[2, 4, 5, 3, 1], [3, 5, 4, 1, 2], [5, 1, 3, 2, 4], [4, 3, 2, 5, 5], [1, 2, 1, 4, 3]]))

    def test_check_columns_valid_4(self):
        self.assertFalse(solverFuncs.check_columns_valid([[2, 4, 5, 3, 1], [3, 5, 4, 2, 1], [5, 1, 3, 2, 4], [4, 5, 2, 3, 4], [1, 5, 2, 4, 3]]))


    def test_check_rows_valid_1(self):
        self.assertTrue(solverFuncs.check_rows_valid([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))

    def test_check_rows_valid_2(self):
        self.assertFalse(solverFuncs.check_rows_valid([[1, 2, 3, 4, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))

    def test_check_rows_valid_3(self):
        self.assertTrue(solverFuncs.check_rows_valid([[2, 4, 5, 3, 1], [3, 5, 4, 2, 1], [5, 1, 3, 2, 4], [4, 5, 2, 3, 1], [1, 5, 2, 4, 3]]))

    def test_check_rows_valid_4(self):
        self.assertFalse(solverFuncs.check_rows_valid([[2, 4, 5, 3, 1], [3, 5, 4, 2, 1], [5, 1, 3, 2, 4], [4, 5, 2, 3, 4], [1, 5, 2, 4, 3]]))

    def test_check_rows_valid_5(self):
        self.assertTrue(solverFuncs.check_rows_valid([[2, 4, 5, 3, 1], [3, 5, 4, 2, 1], [5, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))    


if __name__ == '__main__':
    unittest.main()
