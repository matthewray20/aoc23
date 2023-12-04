import unittest
from puzzle2 import find_real_calibration_value

class TestRealCalibration(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(find_real_calibration_value("two1nine"), 29)

    def test_example2(self):
        self.assertEqual(find_real_calibration_value("eightwothree"), 83)

    def test_example3(self):
        self.assertEqual(find_real_calibration_value("abcone2threexyz"), 13)

    def test_example4(self):
        self.assertEqual(find_real_calibration_value("xtwone3four"), 24)
    
    def test_example5(self):
        self.assertEqual(find_real_calibration_value("4nineeightseven2"), 42)

    def test_example6(self):
        self.assertEqual(find_real_calibration_value("zoneight234"), 14)
    
    def test_example7(self):
        self.assertEqual(find_real_calibration_value("7pqrstsixteen"), 76)
    
    def test_example8(self):
        self.assertEqual(find_real_calibration_value("eighthree"), 83)

    def test_example9(self):
        self.assertEqual(find_real_calibration_value("sevenine"), 79)

if __name__ == '__main__':
    unittest.main()
