#!/usr/bin/python3
import unittest
class mathsTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(4 + 4, 8)
    def test_substraction(self):
        self.assertEqual(4 - 2, 2)
class stringTest(unittest.TestCase):
    def test_concatinate(self):
        self.assertEqual("hel" + "-" + "lo", "hel-lo")
    def test_upper(self):
        self.assertEqual("he".upper(), "HE")
math_suite = unittest.TestLoader().loadTestsFromTestCase(mathsTest)
string_suite = unittest.TestLoader().loadTestsFromTestCase(stringTest)
all_test_suite = unittest.TestSuite([math_suite, string_suite])
if __name__ == "__main__":
    unittest.TextTestRunner().run(all_test_suite)
    