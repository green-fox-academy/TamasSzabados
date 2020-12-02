import unittest

from cow_n_bulls import Cow_n_bulls


class TestCowNBulls(unittest.TestCase):
    def test_guess(self):
        player = Cow_n_bulls()
        self.assertTrue(player.random_numbers())
        self.assertEqual(player.guess(5), 1)
        self.assertEqual(player.get_status(), "playing")
        self.assertEqual(player.reset(), 0)
        player.numbers = [1, 2, 3, 4]
        player.guesses = [1, 2, 4, 3]
        player.state = "finished"
        self.assertEqual(player.guess_results(), "You have: 2 Cows and 2 Bulls")
        player.counter = 4
        with self.assertRaises(ValueError):
            player.guess(5)

        



if __name__ == '__main__':
    unittest.main()