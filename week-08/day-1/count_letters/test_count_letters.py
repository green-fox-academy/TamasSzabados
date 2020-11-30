import unittest

from count_letters import count_letters

class Testcount(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count_letters("hello world"), {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
        with self.assertRaises(TypeError):
            count_letters(1234)
            count_letters(True)
            count_letters(0.1112)


if __name__ == "__main__":
    unittest.main()