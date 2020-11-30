import unittest

from anagram import anagram

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(anagram('abcd', 'bdca'), True)
        self.assertFalse(anagram('abcd', 'caad'), False)
        with self.assertRaises(TypeError):
            anagram(1234, 4321)
            anagram("adcd", 2345)
            anagram(1234, "haja")

if __name__ == '__main__':
    unittest.main()