import unittest

from sum import sum1

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum1([1,2,3]), 6)
        self.assertEqual(sum1([2]), 2)
        with self.assertRaises(ValueError):
            sum1(None)
            sum1([])
        


if __name__ == '__main__':
    unittest.main()