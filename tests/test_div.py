# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import div

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_div(self):
        assert div(4,4) == 1
        assert div(1,1) == 1
        assert div(0,1) == 0
        assert div(10,5) == 2