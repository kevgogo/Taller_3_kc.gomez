import unittest
from boa_constrictor import Boa_Constrictor
from huron import Huron

class TestBoaConstrictor(unittest.TestCase):

    def setUp(self):
        """Crea una instancia de Boa_Constrictor para ser utilizada en las pruebas."""
        self.boa = Boa_Constrictor("Boa", 15.0, 5, "Brasil", 10.0)

    def test_hacer_sonido(self):
        """Prueba que el sonido de la boa sea correcto."""
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        """Prueba que el cálculo de flete sea correcto."""
        esperado = self.boa._impuestos * self.boa._peso
        self.assertEqual(self.boa.calcular_flete(), esperado)

    def test_agregar_ratones(self):
        """Prueba que el método de agregar ratones funcione correctamente y lance error al llegar al límite."""
        for _ in range(10):
            self.boa.agregar_ratones()
        with self.assertRaises(ValueError):
            self.boa.agregar_ratones()

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
