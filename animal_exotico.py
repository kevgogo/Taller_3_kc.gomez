from animal import Animal;

# Clase Animal_Exotico que hereda de Animal
class Animal_Exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def calcular_flete(self):
        return self._impuestos * self._peso