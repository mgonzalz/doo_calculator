import unittest
from lanzador import validate_menu

class TestMenu(unittest.TestCase):
    def test_opc_valida(self):
        for i in range(0,12):
            self.assertEqual(validate_menu(i), i)
    def test_opc_mayor(self):
        self.assertEqual(validate_menu(12), False)
    def test_opc_menor(self):
        self.assertEqual(validate_menu(-1), False)
    def test_opc_letra(self):
        self.assertEqual(validate_menu("aadasdas"), False)

