from src.iniciar_playlist import iniciar_playlist
from src.seleccionar_cancion_random import seleccionar_cancion_random
from src.check_play_shuffle import check_play_shuffle

def play_shuffle(libreria, playlist):
    
    # Comprobaciones
    assert isinstance(libreria, dict), 'libreria no es un diccionario'
    assert isinstance(playlist, dict), 'playlist no es un diccionario'

    if libreria == {}:
        playlist = {}
        return

    indice_cancion = 0

    añadir_cancion = iniciar_playlist(indice_cancion)

    continuar = True

    while continuar:

        cancion = seleccionar_cancion_random(libreria)

        if cancion not in list(playlist.values()):
            indice_cancion = añadir_cancion(cancion, playlist)
            print(str(playlist[indice_cancion]), " se ha añadido correctamente")
        else:
            pass

        if len(libreria) == len(playlist):
            continuar = False
            print("Todas las canciones han sido añadidas")

    assert check_play_shuffle(playlist), "cancion repetida"


