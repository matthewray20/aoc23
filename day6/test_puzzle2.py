

import unittest
from puzzle2 import find_nums


# test the function to get the single number from the multiple numbers in the string
class TestFindNums(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(find_num("Time:      7  15   30"), 71530)

    def test_example2(self):
        self.assertEqual(find_num("Distance:  9  40  200"), 940200)



if __name__ == "__main__":
    unittest.main()