# Importa las clases Boa_Constrictor y Huron
from boa_constrictor import Boa_Constrictor
from huron import Huron

class Guarderia:
    def __init__(self):
        # Inicializa dos boas y dos hurones
        self.boas = [
            Boa_Constrictor("Boa1", 20.0, 5, "Brasil", 12.0),
            Boa_Constrictor("Boa2", 18.0, 4, "Perú", 10.0)
        ]
        self.hurones = [
            Huron("Huron1", 1.5, 2, "Argentina", 5.0),
            Huron("Huron2", 1.8, 3, "Chile", 4.5)
        ]

    def alimentar_boa(self, boa):
        """Intenta alimentar a la boa y maneja posibles errores."""
        if boa is None:
            return "Esta Boa no existe!"
        
        try:
            boa.agregar_ratones()
            return "Éxito"
        except ValueError:
            return "La boa está llena"
