import unittest
from calculator import app

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = app()
        calc.display.set("5+2")
        calc.result(calc.display)
        self.assertEqual(calc.display.get(), "7")

    def test_subtraction(self):
        calc = app()
        calc.display.set("7-2")
        calc.result(calc.display)
        self.assertEqual(calc.display.get(), "5")

    def test_multiplication(self):
        calc = app()
        calc.display.set("2*6")
        calc.result(calc.display)
        self.assertEqual(calc.display.get(), "12")

    def test_division(self):
        calc = app()
        calc.display.set("9/3")
        calc.result(calc.display)
        self.assertEqual(calc.display.get(), "3.0")

    def test_round(self):
        calc = app()
        calc.display.set("4.23124322")
        calc.round(2)
        self.assertEqual(calc.display.get(), "4.23")

    def test_divide_by_zero(self):
        calc = app()
        calc.display.set("1/0")
        calc.result(calc.display)
        self.assertEqual(calc.display.get(), "UNDEFINED")

    def test_infinity(self):
        calc = app()
        calc.display.set("1e1000")
        calc.result(calc.display)
        self.assertEqual(calc.display.get(), "Inf")

if __name__ == '__main__':
    unittest.main()
