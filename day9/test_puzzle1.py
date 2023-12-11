





import unittest
from puzzle1 import predict_next




class TestPredictNext(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(predict_next([0, 3, 6, 9, 12, 15], 'forwards'), 18)
    
    def test_example2(self):
        self.assertEqual(predict_next([1, 3, 6, 10, 15, 21], 'forwards'), 28)
    
    def test_example3(self):
        self.assertEqual(predict_next([10, 13, 16, 21, 30, 45], 'forwards'), 68)
    




if __name__ == "__main__":
    unittest.main()
    
    