from abc import ABC, abstractmethod

# Interfaz iAnimal
class IAnimal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def obtener_kilos_comidos(self):
        pass