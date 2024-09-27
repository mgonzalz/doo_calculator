from src.calculator import Calculator
import unittest

class TestMyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    def test_suma_method(self):
        self.calc.suma(1, 3)
        self.assertEqual(4, self.calc.value)
    
    def test_rest_value(self):
        self.calc.resta(1, 3)
        self.assertEqual(-2, self.calc.value)
