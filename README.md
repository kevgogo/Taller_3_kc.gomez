# Taller 3 - Pruebas y Versiones

Este repositorio contiene la implementación del **Taller 3** del curso **COLSUBSIDIO BACKEND CON PYTHON GRUPO 2 - Universidad de los Andes**. Este taller abarca la práctica de conceptos de programación orientada a objetos en Python y el uso de pruebas unitarias para validar el correcto funcionamiento del código. Además, se implementa el manejo básico de control de versiones con Git y GitHub.

## Estructura del Proyecto

- **`animal.py`**: Clase base `Animal` que implementa la interfaz `IAnimal`.
- **`animal_exotico.py`**: Clase `Animal_Exotico` que hereda de `Animal`.
- **`boa_constrictor.py`**: Clase `Boa_Constrictor`, derivada de `Animal_Exotico`, que incluye métodos específicos para las boas.
- **`huron.py`**: Clase `Huron`, también derivada de `Animal_Exotico`.
- **`guarderia.py`**: Clase `Guarderia`, que contiene instancias de `Boa_Constrictor` y `Huron` y proporciona métodos de alimentación con manejo de errores.
- **Pruebas Unitarias**:
  - **`test_animales.py`**: Pruebas unitarias para las clases `Boa_Constrictor` y `Huron`.
  - **`test_guarderia.py`**: Pruebas unitarias para la clase `Guarderia`.
  - **`test_huron.py`**: Pruebas unitarias adicionales para la clase `Huron`.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone [Taller_3_kc.gomez](https://github.com/kevgogo/Taller_3_kc.gomez.git)
   cd Taller_3_kc.gomez
