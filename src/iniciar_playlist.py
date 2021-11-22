<<<<<<< HEAD
def iniciar_playlist():
=======
def iniciar_playlist(indice_cancion):

    clave_cancion = indice_cancion

    def añadir_cancion(cancion, playlist):

        # Comprobaciones
        assert isinstance(cancion, str), "cancion no es un diccionario"
        assert isinstance(playlist, dict), "playlist no es un diccionario"

        lista_canciones = list(playlist.values())   # Crea una lista de las canciones dentro de la playlist
        assert cancion not in lista_canciones   

        nonlocal clave_cancion
        clave_cancion += 1
        playlist[clave_cancion] = str(cancion)
        return clave_cancion

    return añadir_cancion
>>>>>>> 3d237d5ce58999d5e0bdea5fe9b59b1d2964dc4c
