import unittest

from sharpie import Sharpie

class TestSharpie(unittest.TestCase):
    def test_sharpie(self):
        sharpie = Sharpie("black", 0.1)
        self.assertEqual(sharpie.use(), 99)
        self.assertEqual(sharpie.get_ink(), 99)
        self.assertEqual(sharpie.get_width(), 0.1)
        self.assertEqual(sharpie.get_color(), "black")
        with self.assertRaises(TypeError):
            sharpie.set_width("s")
            sharpie.set_color(10)
        

if __name__ == '__main__':
    unittest.main()