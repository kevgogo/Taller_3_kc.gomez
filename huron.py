from animal_exotico import Animal_Exotico

# Clase Huron que hereda de Animal_Exotico
class Huron(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._kilos_comidos = 0

    def hacer_sonido(self):
        return "¡Eek Eek!"

    def comer(self, kilos):
        self._kilos_comidos += kilos

    def obtener_kilos_comidos(self):
        return self._kilos_comidos
