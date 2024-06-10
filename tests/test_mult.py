# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import mult

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_mult(self):
        assert mult(4,5) == 20
        assert mult(1,2) == 2
        assert mult(7,5) == 35
        assert mult(7,10) == 70