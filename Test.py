#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from add import addition

class TestSum(unittest.TestCase):
    def test_list_int(self):
        result = addition(2,3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
