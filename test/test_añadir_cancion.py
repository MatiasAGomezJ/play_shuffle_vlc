from src.iniciar_playlist import iniciar_playlist   
import pytest

@pytest.mark.añadir_cancion
def test_funciona():
    numero = 1
    añadir_cancion = iniciar_playlist(numero)
    playlist = {}
    pl_copia = playlist.copy()
    nombre = "Sweden"
    añadir_cancion(nombre, playlist)
    pl_copia.update({numero+1:nombre})
    assert playlist == pl_copia