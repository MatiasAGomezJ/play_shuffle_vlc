from src.check_seleccionar_cancion_random import check_seleccionar_cancion_random
import random
# Escoge un item del diccionario especificado
def seleccionar_cancion_random(libreria):
    
    # Comprobaciones
    assert isinstance(libreria, dict), 'la libreria no es un dict'

    if libreria == {}: return ''

    lista_canciones = list(libreria.keys()) # Crea una lista de los nombres de las canciones

    cancion = random.choice(lista_canciones) # Escoge al azar uno de la lista especificada

    assert check_seleccionar_cancion_random(cancion, libreria)

    return cancion