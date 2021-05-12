import unittest
from functions_to_test import Calculator as calc


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(4, 8), 12)

    def test_subtract(self):
        self.assertEqual(calc.subtract(12, 8), 4)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 3), 9)

    def test_divide(self):
        self.assertEqual(calc.divide(9, 3), 3)
        self.assertRaises(ValueError, calc.divide(9, 0))


if __name__ == '__main__':
    unittest.main()
