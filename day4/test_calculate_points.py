import unittest
from puzzle1 import calculate_points


class TestCalcPoints(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(calculate_points(
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'),
            8
        )
    
    def test_example2(self):
        self.assertEqual(calculate_points(
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'),
            2
        )
    
    def test_example3(self):
        self.assertEqual(calculate_points(
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'),
            2
        )
    
    def test_example4(self):
        self.assertEqual(calculate_points(
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'),
            1
        )
    
    def test_example5(self):
        self.assertEqual(calculate_points(
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'), 
            0
        )
    
    def test_example6(self):
        self.assertEqual(calculate_points(
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'),
            0
        )


if __name__ == '__main__':
    unittest.main()
