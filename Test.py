#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from add import addition

class TestSum(unittest.TestCase):
    def test_1(self):
        result = addition(2,3)
        self.assertEqual(result, 5)
    def test_2(self):
        result = addition(5,10)
        self.assertEqual(result, 15)
    def test_3(self):
        result = addition(10,35)
        self.assertEqual(result, 45)
    def test_4(self):
        result = addition(200,300)
        self.assertEqual(result, 500)
    def test_5(self):
        result = addition(11,32)
        self.assertEqual(result, 5111)

if __name__ == '__main__':
    unittest.main()
