import unittest
import BinaryGap as test

class TestBinaryGap(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(2, test.solution(9))

    def test_example2(self):
        self.assertEqual(4, test.solution(529))
    
    def test_example3(self):
        self.assertEqual(1, test.solution(20))

    def test_example4(self):
        self.assertEqual(0, test.solution(15))

    def test_example5(self):
        self.assertEqual(0, test.solution(32))

    def test_example6(self):
        self.assertEqual(5, test.solution(1041))

    def test_example7(self):
        self.assertEqual(0, test.solution(2147483647))
