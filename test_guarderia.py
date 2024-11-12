import unittest
from guarderia import Guarderia
from boa_constrictor import Boa_Constrictor

class TestGuarderia(unittest.TestCase):

    def setUp(self):
        """Configura una instancia de Guarderia para usar en las pruebas."""
        self.guarderia = Guarderia()
        self.boa = self.guarderia.boas[0]  # Selecciona una de las boas para pruebas

    def test_alimentar_boa_exito(self):
        """Prueba que alimentar a una boa inicialmente retorne 'Éxito'."""
        resultado = self.guarderia.alimentar_boa(self.boa)
        self.assertEqual(resultado, "Éxito")

    def test_alimentar_boa_llena(self):
        """Prueba que al alcanzar el límite de ratones se retorne 'La boa está llena'."""
        # Alimenta a la boa 10 veces para alcanzar el límite
        for _ in range(10):
            self.guarderia.alimentar_boa(self.boa)
        # Intento adicional de alimentar debe lanzar el mensaje de que está llena
        resultado = self.guarderia.alimentar_boa(self.boa)
        self.assertEqual(resultado, "La boa está llena")

    def test_alimentar_boa_no_existe(self):
        """Prueba que alimentar una boa que no existe retorne 'Esta Boa no existe!'."""
        resultado = self.guarderia.alimentar_boa(None)
        self.assertEqual(resultado, "Esta Boa no existe!")
