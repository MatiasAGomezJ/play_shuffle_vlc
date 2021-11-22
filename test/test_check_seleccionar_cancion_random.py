from src.check_seleccionar_cancion_random import check_seleccionar_cancion_random
import pytest

@pytest.mark.check_selec_cancion_random
def test_funciona():
    assert check_seleccionar_cancion_random('a', {'a': 1, 'b': 2}) == True
    assert check_seleccionar_cancion_random('c', {'a': 1, 'b': 2}) == False
