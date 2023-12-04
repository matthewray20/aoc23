import unittest
from main import find_calibration_value 

class TestCalibration(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(find_calibration_value("1abc2"), 12)

    def test_example2(self):
        self.assertEqual(find_calibration_value("pqr3stu8vwx"), 38)

    def test_example3(self):
        self.assertEqual(find_calibration_value("a1b2c3d4e5f"), 15)

    def test_example4(self):
        self.assertEqual(find_calibration_value("treb7uchet"), 77)

if __name__ == '__main__':
    unittest.main()
