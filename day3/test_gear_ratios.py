
import unittest
from puzzle2 import gear_ratios

class TestPartNumbers(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(gear_ratios(
                ['467..114..',
                '...*......',
                '..35..633.',
                '......#...',
                '617*......',
                '.....+.58.',
                '..592.....',
                '......755.',
                '...$.*....',
                '.664.598..']
            ), 467835)

if __name__ == '__main__':
    unittest.main()
