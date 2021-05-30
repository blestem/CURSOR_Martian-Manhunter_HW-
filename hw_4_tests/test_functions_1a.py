import unittest
from functions_to_test import Calculator as calc


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(4, 8), 12)
        self.assertEqual(calc.add(15, 10), 25)
        self.assertEqual(calc.add(0.0, 0.1), 0.1)
        self.assertEqual(calc.add("2", "9"), "29")
        self.assertEqual(calc.add(-15, -4), -19)
        self.assertNotEqual(calc.add(10, 10), 22)

    def test_add_negative(self):
        with self.assertRaises(TypeError):
            calc.add(6, None)
            calc.add([], 48)
            calc.add("15", 7)

    def test_subtract(self):
        self.assertEqual(calc.subtract(12, 8), 4)
        self.assertEqual(calc.subtract(5, 14), -9)
        self.assertEqual(calc.subtract(-15, -10), -5)
        self.assertEqual(calc.subtract(5.75, 1.75), 4.00)
        self.assertNotEqual(calc.subtract(4, 2), 3)

    def test_subtract_negative(self):
        with self.assertRaises(TypeError):
            calc.subtract(6, "2")
            calc.subtract("7", "15")
            calc.subtract(6, None)
            calc.subtract([], 48)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 3), 9)
        self.assertEqual(calc.multiply(-9, 2), -18)
        self.assertEqual(calc.multiply(0.15, 0), 0)
        self.assertEqual(calc.multiply("6", 3), "666")
        self.assertEqual(calc.multiply(0.7, 0.5), 0.35)
        self.assertNotEqual(calc.multiply(5, 5), 52)

    def test_multiply_negative(self):
        with self.assertRaises(TypeError):
            calc.multiply(None, 15)
            calc.multiply([15], [2])

    def test_divide(self):
        self.assertEqual(calc.divide(9, 3), 3)
        self.assertEqual(calc.divide(-12, -2), 6)
        self.assertEqual(calc.divide(-15, 3), -5)
        self.assertEqual(calc.divide(0.35, 0.7), 0.5)
        self.assertNotEqual(calc.divide(9, 3), 4)

    def test_divide_negative(self):
        with self.assertRaises(ValueError):
            calc.divide(15, 0)
            calc.divide(-15, 0)
            calc.divide(0.15, 0)
            calc.divide(15, 0.0)

        with self.assertRaises(TypeError):
            calc.divide(15, None)
            calc.divide("15", "3")
            calc.divide(15, "3")
            calc.divide(15, "z")


if __name__ == '__main__':
    unittest.main()
