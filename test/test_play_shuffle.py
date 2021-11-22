from src.play_shuffle import play_shuffle
import pytest

@pytest.mark.play_shuffle
def test_libreria_vacia():
    a, b = {}, {}
    play_shuffle(a, b)  
    assert b == {}

    # a, b = {}, {'a': 1, 'b': 2}
    # play_shuffle(a, b)
    # assert b == {}