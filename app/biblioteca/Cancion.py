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
    
    def obtenerNombre(self):
        return self._nombre
    def obtenerArtista(self):
        return self._artista
    def obtenerAlbum(self):
        return self._album
    def obtenerImagen(self):
        return self._imagen
    def obtenerRuta(self):
        return self._ruta
    
    def imprimirCancion(self):
        print("Cancion:", self._nombre)
        print("Artista:", self._artista)
        print("Album:", self._album)
        print("Imagen:", self._imagen)
        print("Ruta:", self._ruta)
        print("\n")