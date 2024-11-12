from i_animal import IAnimal
from abc import abstractmethod

# Clase base Animal que implementa la interfaz IAnimal
class Animal(IAnimal):
    def __init__(self, nombre: str, peso: float, edad: int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad

    def obtener_nombre(self):
        return self._nombre

    def obtener_peso(self):
        return self._peso

    def obtener_edad(self):
        return self._edad

    @abstractmethod
    def hacer_sonido(self):
        pass