import unittest
from apples import Apples


class TestApples(unittest.TestCase):
    def test_apple(self):
        apples = Apples("inared")
        self.assertEqual(apples.get_apples(), "apples")



if __name__ == '__main__':
    unittest.main()