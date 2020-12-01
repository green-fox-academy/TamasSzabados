import unittest

from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(11), 89)
        with self.assertRaises(TypeError):
            fibonacci(0.1)
            fibonacci("s")

if __name__ == '__main__':
    unittest.main()