
import unittest
from puzzle1 import possible_game

class TestPossibilities(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(possible_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", conditions), 1)
    
    def test_example2(self):
        self.assertEqual(possible_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", conditions), 2)

    def test_example3(self):
        self.assertEqual(possible_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", conditions), 0)
    
    def test_example4(self):
        self.assertEqual(possible_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", conditions), 0)
    
    def test_example5(self):
        self.assertEqual(possible_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", conditions), 5)
    
    
if __name__ == '__main__':
    conditions = {'red': 12, 'green': 13, 'blue': 14}
    unittest.main()
