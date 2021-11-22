import random
from src.seleccionar_cancion_random import seleccionar_cancion_random
import pytest

@pytest.mark.selec_cancion_random
def test_libreria_vacia():
    assert seleccionar_cancion_random({}) == ''
