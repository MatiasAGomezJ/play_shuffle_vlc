# Comprueba que no haya canciones repetidas ( mismo nombre )
def check_play_shuffle(playlist):

    # Comprobaciones
    assert isinstance(playlist, dict)

    lista_canciones = list(playlist.values()) # Crea una lista de los nombres de las canciones

    # Comprueba que por cada cancion solo aparezca una vez
    for cancion in playlist:
        if lista_canciones.count(cancion) > 1:
            return False
    
    return True