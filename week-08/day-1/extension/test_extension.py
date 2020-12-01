import unittest
from extension import add, max_of_three, median, is_vovel, translate

class TestExtend(unittest.TestCase):
    def test_add_2_and_3_is_5(self):
        self.assertEqual(add(7, 3), 10)

    def test_add_1_and_4_is_5(self):
        self.assertEqual(add(18, 4), 22)

    def test_max_of_three_first(self):
        self.assertEqual(max_of_three(6, 4, 10), 10)

    def test_max_of_three_third(self):
        self.assertEqual(max_of_three(5, 10, 5), 10)

    def test_median_four(self):
        self.assertEqual(median([7, 5, 3, 5, 1, 9]), 5)

    def test_median_five(self):
        self.assertEqual(median([1, 2, 3, 3, 4, 5, 6]), 3)

    def test_is_vovel_a(self):
        self.assertTrue(is_vovel('e'))

    def test_is_vovel_u(self):
        self.assertFalse(is_vovel('b'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(translate('bemutatkozik ő'), 'bevemuvutavatkovozivik ővő')

    def test_translate_kolbice(self):
        self.assertEqual(translate('lagopus'), 'lavagovopuvus')

if __name__ == '__main__':
    unittest.main()