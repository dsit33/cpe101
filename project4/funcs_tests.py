import unittest
from funcs import *


class TestCases(unittest.TestCase):

    def test_checkForward_1(self):
        self.assertEqual(checkForward('UNIX', [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]), (9, 3))

    def test_checkForward_2(self):
        self.assertEqual(checkForward('CODE', [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]), -1)

    def test_checkForward_3(self):
        self.assertEqual(checkForward('ZEBRA', [['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']]), (1, 0))

    def test_checkForward_4(self):
        self.assertEqual(checkForward('RACCOON', [['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'N', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']]), -1)

    def test_checkForward_5(self):
        self.assertEqual(checkForward('LLAR', [['L', 'L', 'A', 'R', 'S', 'H', 'A', 'H', 'L', 'C'], ['A', 'O', 'O', 'L', 'L', 'A', 'M', 'I', 'L', 'L'], ['O', 'I', 'D', 'N', 'A', 'L', 'H', 'G', 'I', 'H'], ['R', 'B', 'A', 'M', 'C', 'E', 'T', 'U', 'H', 'S'], ['S', 'M', 'O', 'S', 'K', 'A', 'G', 'E', 'T', 'R'], ['C', 'O', 'R', 'C', 'H', 'O', 'R', 'R', 'O', 'A'], ['I', 'D', 'B', 'S', 'L', 'S', 'A', 'A', 'O', 'M'], ['I', 'G', 'O', 'S', 'M', 'O', 'N', 'D', 'F', 'L'], ['H', 'H', 'N', 'G', 'M', 'S', 'D', 'C', 'M', 'A'], ['C', 'M', 'I', 'R', 'R', 'S', 'M', 'L', 'H', 'P']]), (0, 0))


    def test_checkBackward_1(self):
        self.assertEqual(checkBackward('HIGHLAND', [['L', 'L', 'A', 'R', 'S', 'H', 'A', 'H', 'L', 'C'], ['A', 'O', 'O', 'L', 'L', 'A', 'M', 'I', 'L', 'L'], ['O', 'I', 'D', 'N', 'A', 'L', 'H', 'G', 'I', 'H'], ['R', 'B', 'A', 'M', 'C', 'E', 'T', 'U', 'H', 'S'], ['S', 'M', 'O', 'S', 'K', 'A', 'G', 'E', 'T', 'R'], ['C', 'O', 'R', 'C', 'H', 'O', 'R', 'R', 'O', 'A'], ['I', 'D', 'B', 'S', 'L', 'S', 'A', 'A', 'O', 'M'], ['I', 'G', 'O', 'S', 'M', 'O', 'N', 'D', 'F', 'L'], ['H', 'H', 'N', 'G', 'M', 'S', 'D', 'C', 'M', 'A'], ['C', 'M', 'I', 'R', 'R', 'S', 'M', 'L', 'H', 'P']]), (2, 9))

    def test_checkBackward_2(self):
        self.assertEqual(checkBackward('CHORRO', [['L', 'L', 'A', 'R', 'S', 'H', 'A', 'H', 'L', 'C'], ['A', 'O', 'O', 'L', 'L', 'A', 'M', 'I', 'L', 'L'], ['O', 'I', 'D', 'N', 'A', 'L', 'H', 'G', 'I', 'H'], ['R', 'B', 'A', 'M', 'C', 'E', 'T', 'U', 'H', 'S'], ['S', 'M', 'O', 'S', 'K', 'A', 'G', 'E', 'T', 'R'], ['C', 'O', 'R', 'C', 'H', 'O', 'R', 'R', 'O', 'A'], ['I', 'D', 'B', 'S', 'L', 'S', 'A', 'A', 'O', 'M'], ['I', 'G', 'O', 'S', 'M', 'O', 'N', 'D', 'F', 'L'], ['H', 'H', 'N', 'G', 'M', 'S', 'D', 'C', 'M', 'A'], ['C', 'M', 'I', 'R', 'R', 'S', 'M', 'L', 'H', 'P']]), -1)

    def test_checkBackward_3(self):
        self.assertEqual(checkBackward('HARAMBE', [['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']]), -1)

    def test_checkBackward_4(self):
        self.assertEqual(checkBackward('AOLS', [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]), (7, 5))

    def test_checkBackward_5(self):
        self.assertEqual(checkBackward('PIPE', [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]), -1)


    def test_checkDown_1(self):
        self.assertEqual(checkDown('CALPOLY', [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]), (1, 0))

    def test_checkDown_2(self):
        self.assertEqual(checkDown('PCV', [['L', 'L', 'A', 'R', 'S', 'H', 'A', 'H', 'L', 'C'], ['A', 'O', 'O', 'L', 'L', 'A', 'M', 'I', 'L', 'L'], ['O', 'I', 'D', 'N', 'A', 'L', 'H', 'G', 'I', 'H'], ['R', 'B', 'A', 'M', 'C', 'E', 'T', 'U', 'H', 'S'], ['S', 'M', 'O', 'S', 'K', 'A', 'G', 'E', 'T', 'R'], ['C', 'O', 'R', 'C', 'H', 'O', 'R', 'R', 'O', 'A'], ['I', 'D', 'B', 'S', 'L', 'S', 'A', 'A', 'O', 'M'], ['I', 'G', 'O', 'S', 'M', 'O', 'N', 'D', 'F', 'L'], ['H', 'H', 'N', 'G', 'M', 'S', 'D', 'C', 'M', 'A'], ['C', 'M', 'I', 'R', 'R', 'S', 'M', 'L', 'H', 'P']]), -1)

    def test_checkDown_3(self):
        self.assertEqual(checkDown('RABBIT', [['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']]), (1, 3))

    def test_checkDown_4(self):
        self.assertEqual(checkDown('CHICKEN', [['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']]), -1)

    def test_checkDown_5(self):
        self.assertEqual(checkDown('RAMS', [['L', 'L', 'A', 'R', 'S', 'H', 'A', 'H', 'L', 'C'], ['A', 'O', 'O', 'L', 'L', 'A', 'M', 'I', 'L', 'L'], ['O', 'I', 'D', 'N', 'A', 'L', 'H', 'G', 'I', 'H'], ['R', 'B', 'A', 'M', 'C', 'E', 'T', 'U', 'H', 'S'], ['S', 'M', 'O', 'S', 'K', 'A', 'G', 'E', 'T', 'R'], ['C', 'O', 'R', 'C', 'H', 'O', 'R', 'R', 'O', 'A'], ['I', 'D', 'B', 'S', 'L', 'S', 'A', 'A', 'O', 'M'], ['I', 'G', 'O', 'S', 'M', 'O', 'N', 'D', 'F', 'L'], ['H', 'H', 'N', 'G', 'M', 'S', 'D', 'C', 'M', 'A'], ['C', 'M', 'I', 'R', 'R', 'S', 'M', 'L', 'H', 'P']]), -1)


    def test_checkUp_1(self):
        self.assertEqual(checkUp('MOUSE', [['L', 'L', 'A', 'R', 'S', 'H', 'A', 'H', 'L', 'C'], ['A', 'O', 'O', 'L', 'L', 'A', 'M', 'I', 'L', 'L'], ['O', 'I', 'D', 'N', 'A', 'L', 'H', 'G', 'I', 'H'], ['R', 'B', 'A', 'M', 'C', 'E', 'T', 'U', 'H', 'S'], ['S', 'M', 'O', 'S', 'K', 'A', 'G', 'E', 'T', 'R'], ['C', 'O', 'R', 'C', 'H', 'O', 'R', 'R', 'O', 'A'], ['I', 'D', 'B', 'S', 'L', 'S', 'A', 'A', 'O', 'M'], ['I', 'G', 'O', 'S', 'M', 'O', 'N', 'D', 'F', 'L'], ['H', 'H', 'N', 'G', 'M', 'S', 'D', 'C', 'M', 'A'], ['C', 'M', 'I', 'R', 'R', 'S', 'M', 'L', 'H', 'P']]), -1)

    def test_checkUp_2(self):
        self.assertEqual(checkUp('COMPILE', [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]), (6, 8))

    def test_checkUp_3(self):
        self.assertEqual(checkUp('SAGGY', [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]), -1)

    def test_checkUp_4(self):
        self.assertEqual(checkUp('BROAD', [['L', 'L', 'A', 'R', 'S', 'H', 'A', 'H', 'L', 'C'], ['A', 'O', 'O', 'L', 'L', 'A', 'M', 'I', 'L', 'L'], ['O', 'I', 'D', 'N', 'A', 'L', 'H', 'G', 'I', 'H'], ['R', 'B', 'A', 'M', 'C', 'E', 'T', 'U', 'H', 'S'], ['S', 'M', 'O', 'S', 'K', 'A', 'G', 'E', 'T', 'R'], ['C', 'O', 'R', 'C', 'H', 'O', 'R', 'R', 'O', 'A'], ['I', 'D', 'B', 'S', 'L', 'S', 'A', 'A', 'O', 'M'], ['I', 'G', 'O', 'S', 'M', 'O', 'N', 'D', 'F', 'L'], ['H', 'H', 'N', 'G', 'M', 'S', 'D', 'C', 'M', 'A'], ['C', 'M', 'I', 'R', 'R', 'S', 'M', 'L', 'H', 'P']]), (6, 2))

    def test_checkUp_5(self):
        self.assertEqual(checkUp('BAE', [['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']]), (8, 0))


    def test_checkDiag_1(self):
        self.assertEqual(checkDiag('MASON', [['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']]), -1)

    def test_checkDiag_2(self):
        self.assertEqual(checkDiag('CORE', [['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']]), (4, 0))

    def test_checkDiag_3(self):
        self.assertEqual(checkDiag('GCC', [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]), (6, 5))

    def test_checkDiag_4(self):
        self.assertEqual(checkDiag('DOGGY', [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'P', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'E', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']]), -1)

    def test_checkDiag_5(self):
        self.assertEqual(checkDiag('SOB', [['L', 'L', 'A', 'R', 'S', 'H', 'A', 'H', 'L', 'C'], ['A', 'O', 'O', 'L', 'L', 'A', 'M', 'I', 'L', 'L'], ['O', 'I', 'D', 'N', 'A', 'L', 'H', 'G', 'I', 'H'], ['R', 'B', 'A', 'M', 'C', 'E', 'T', 'U', 'H', 'S'], ['S', 'M', 'O', 'S', 'K', 'A', 'G', 'E', 'T', 'R'], ['C', 'O', 'R', 'C', 'H', 'O', 'R', 'R', 'O', 'A'], ['I', 'D', 'B', 'S', 'L', 'S', 'A', 'A', 'O', 'M'], ['I', 'G', 'O', 'S', 'M', 'O', 'N', 'D', 'F', 'L'], ['H', 'H', 'N', 'G', 'M', 'S', 'D', 'C', 'M', 'A'], ['C', 'M', 'I', 'R', 'R', 'S', 'M', 'L', 'H', 'P']]), (4, 0))


if __name__ == '__main__':
    unittest.main()
