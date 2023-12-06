
import unittest
from puzzle1 import parse_races, ways_to_win_races

# test parsing of the races into list of [time, distance] for each race
class TestParseRaces(unittest.TestCase):
    def test_example1(self):
        self.assertTrue((parse_races([
            'Time:      7  15   30', 
            'Distance:  9  40  200'
        ]) == [
            [7, 9],
            [15, 40],
            [30, 200]
        ]).all())

# test calculation for number of ways to win a race
class TestWaysToWinRaces(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(ways_to_win_races([7, 9]), 4)
    
    def test_example2(self):
        self.assertEqual(ways_to_win_races([15, 40]), 8)
    
    def test_example3(self):
        self.assertEqual(ways_to_win_races([30, 200]), 9)



if __name__ == "__main__":
    unittest.main()