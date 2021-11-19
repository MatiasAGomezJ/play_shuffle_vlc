from iniciar_playlist import iniciar_playlist
from seleccionar_cancion_random import seleccionar_cancion_random

def play_shuffle(libreria, playlist):
    
    # Comprobacion de variables
    assert isinstance(libreria, dict)
    assert isinstance(playlist, dict)


    iniciar_playlist()
    print(__name__)

