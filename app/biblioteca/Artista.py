from app.lista.Lista import Nodo
from app.lista.Lista import Lista

from app.biblioteca.Album import Album

class Artista: 
    
    def __init__(self, nombre):
        self._nombre = nombre
        self._lista_albumes = Lista()
        
    def agregarAlbum(self, nombre):
        album = Album(nombre, self._nombre)
        
        if self._lista_albumes.estaVacia():
            self._lista_albumes.agregarALaLista(album)
            print("Se ha agregado el album", nombre, "al artista", self._nombre)
        else:
            contador = 1
            longitud = self._lista_albumes.obtenerLongitud()
            album_actual = self._lista_albumes.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            
            while contador <= longitud :
                if album_actual.obtenerNombre()  == nombre:
                    print("Se encontro nuevamente el album", nombre, "del artista", self._nombre)
                    break
                else:
                    if contador == longitud:
                        #agregar el album 
                        self._lista_albumes.agregarALaLista(album)
                        print("Se ha agregado el album", nombre, "al artista", self._nombre)
                    
                contador += 1
                album_actual = self._lista_albumes.encontrarPorIndiceInicioFinal(contador).obtenerDato() 
    
    
    def obtenerListaAlbumes(self): 
        return self._lista_albumes
    
    def obtenerNombre(self): 
        return self._nombre