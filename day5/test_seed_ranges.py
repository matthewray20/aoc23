

import unittest
from puzzle2 import get_seeds


class TestSeedRanges(unittest.TestCase):
    def test_example1(elf):
        self.assertEqual(parse_seed_ranges('seeds: 79 14 55 13'), [(79, 93, 14), (55, 68, 13)])
    def test_example1(self):
        self.assertTrue(
            (get_seeds([(79, 93, 14), (55, 68, 13)], 2) == 
            [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]).all())
    
    """def test_example2(self):
        self.assertEqual(
            (get_seeds([(79, 93, 14), (55, 68, 13)], 2) ==  
            []).all())"""



if __name__ == "__main__":
    unittest.main()