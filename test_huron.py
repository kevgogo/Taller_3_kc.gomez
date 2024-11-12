import unittest
from huron import Huron

class TestHuron(unittest.TestCase):

    def setUp(self):
        """Crea una instancia de Huron para ser utilizada en las pruebas."""
        self.huron = Huron("Huron", 1.5, 2, "Argentina", 5.0)

    def test_hacer_sonido(self):
        """Prueba que el sonido del hurón sea correcto."""
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        """Prueba que el cálculo de flete sea correcto."""
        esperado = self.huron._impuestos * self.huron._peso
        self.assertEqual(self.huron.calcular_flete(), esperado)