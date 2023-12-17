#Objeto cancion con toda la informacion necesaria para representarla
class Cancion:
    def __init__(self, nombre, artista, album, imagen, ruta):
        self._nombre = nombre
        self._artista = artista
        self._album = album
        self._imagen = imagen
        self._ruta = ruta

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_artista(self):
        return self._artista

    def get_album(self):
        return self._album

    def get_imagen(self):
        return self._imagen

    def get_ruta(self):
        return self._ruta