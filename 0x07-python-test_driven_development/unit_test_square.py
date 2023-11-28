import unittest
from doc_test import square_area

class TestSquareArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(square_area(2), 4)
        self.assertAlmostEqual(square_area(0), 0)
    def test_values(self):
        self.assertRaises(ValueError, square_area, -2)
    def test_types(self):
        self.assertRaises(TypeError, square_area, "h")
        self.assertRaises(TypeError, square_area, 2+2j)
        self.assertRaises(TypeError, square_area, True)