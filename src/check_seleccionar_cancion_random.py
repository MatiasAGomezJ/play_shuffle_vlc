def check_seleccionar_cancion_random(cancion, libreria):

    # Comprobaciones
    assert isinstance(cancion, str), 'la cancion no es un string'
    assert isinstance(libreria, dict), 'la libreria no es un diccionario'

    if cancion not in libreria:
        return False
    else:
        return True