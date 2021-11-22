from src.iniciar_playlist import iniciar_playlist
import pytest

@pytest.mark.iniciar_playlist
def test_devuelve_funcion():
    assert callable(iniciar_playlist(0))