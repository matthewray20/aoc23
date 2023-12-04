
import unittest
from puzzle2 import min_possible_game

class TestPossibilities(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(min_possible_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), 48)
    
    def test_example2(self):
        self.assertEqual(min_possible_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"), 12)

    def test_example3(self):
        self.assertEqual(min_possible_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"), 1560)
    
    def test_example4(self):
        self.assertEqual(min_possible_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"), 630)
    
    def test_example5(self):
        self.assertEqual(min_possible_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"), 36)
    
    
if __name__ == '__main__':
    unittest.main()
