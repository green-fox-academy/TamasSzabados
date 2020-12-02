import unittest

from animal import Animal

class TestAnimal(unittest.TestCase):
    def test_animals(self):
        animal = Animal(50,50)
        self.assertEqual(animal.eat(),49)
        self.assertEqual(animal.drink(),49)
        self.assertEqual(animal.play(),(50,50))
        self.assertEqual(animal.get_hunger(),50)
        self.assertEqual(animal.get_thirst(),50)
       



if __name__ == "__main__":
    unittest.main()