from src.calculator import Calculator
import unittest

class TestMyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_suma(self):
        self.assertEqual(self.calc.suma(3, 5), 8)
        self.assertEqual(self.calc.suma(-1, 1), 0)
        self.assertEqual(self.calc.suma(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(self.calc.resta(10, 5), 5)
        self.assertEqual(self.calc.resta(-1, 1), -2)
        self.assertEqual(self.calc.resta(-1, -1), 0)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicacion(3, 5), 15)
        self.assertEqual(self.calc.multiplicacion(-1, 1), -1)
        self.assertEqual(self.calc.multiplicacion(-1, -1), 1)

    def test_division(self):
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(-1, 1), -1)
        self.assertEqual(self.calc.division(-1, -1), 1)
        self.assertEqual(self.calc.division(5, 0), "Error: División por cero")

    def test_potencia(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(-1, 2), 1)
        self.assertEqual(self.calc.potencia(-1, 3), -1)

    def test_raiz_cuadrada(self):
        self.assertEqual(self.calc.raiz_cuadrada(4), 2)
        self.assertEqual(self.calc.raiz_cuadrada(9), 3)
        self.assertEqual(self.calc.raiz_cuadrada(-1), "Error: Raíz cuadrada de un número negativo")

    def test_logaritmo(self):
        self.assertEqual(self.calc.logaritmo(100), 2)
        self.assertEqual(self.calc.logaritmo(100, 10), 2)
        self.assertEqual(self.calc.logaritmo(8, 2), 3)
        self.assertEqual(self.calc.logaritmo(-1), "Error: Logaritmo de un número no positivo")

    def test_seno(self):
        self.assertAlmostEqual(self.calc.seno(0), 0)
        self.assertAlmostEqual(self.calc.seno(90), 1)
        self.assertAlmostEqual(self.calc.seno(180), 0)

    def test_coseno(self):
        self.assertAlmostEqual(self.calc.coseno(0), 1)
        self.assertAlmostEqual(self.calc.coseno(90), 0)
        self.assertAlmostEqual(self.calc.coseno(180), -1)

    def test_tangente(self):
        self.assertAlmostEqual(self.calc.tangente(0), 0)
        self.assertAlmostEqual(self.calc.tangente(45), 1)
        self.assertAlmostEqual(self.calc.tangente(135), -1)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(-1), 'Error: Factorial de numero negativo')
        self.assertEqual(self.calc.factorial(1.5), 'Error: El factorial solo acepta números enteros.')

