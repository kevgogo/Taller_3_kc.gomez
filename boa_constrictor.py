from animal_exotico import Animal_Exotico

# Clase Boa_Constrictor que hereda de Animal_Exotico
class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0
        self._kilos_comidos = 0

    def agregar_ratones(self):
        if self._ratones_comidos >= 10:  # Si ya ha comido 10 ratones, lanzamos el error
            raise ValueError("Demasiados Ratones!")
        self._ratones_comidos += 1
        self._kilos_comidos += 0.5

    def obtener_ratones_comidos(self):
        return self._ratones_comidos

    def hacer_sonido(self):
        return "¡Tsss!"

    def comer(self, kilos):
        self._kilos_comidos += kilos

    def obtener_kilos_comidos(self):
        return self._kilos_comidos
