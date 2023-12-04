
import unittest
from puzzle1 import part_numbers

class TestPartNumbers(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(part_numbers(
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
            ), 4361)

if __name__ == '__main__':
    unittest.main()
