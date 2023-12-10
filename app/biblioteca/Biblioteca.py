from app.lista.Lista import Lista
from app.biblioteca.Artista import Artista 
from app.biblioteca.Album import Album
from app.biblioteca.ColeccionArtistas import ColeccionArtistas

#Controla la totalidad de la biblioteca de música 
class Biblioteca: 
    def __init__(self): 
        self._coleccion_artistas = ColeccionArtistas()
    
    #Retorna una lista doble enlazada con todos los artistas
    def obtenerListaArtistas(self):
        return self._coleccion_artistas.obtenerListaArtistas()
    
    #Retorna una lista con todos los albumes(recorre la lista de artistas para obtenerla)
    def obtenerListaAlbumes(self):
        lista_albumes = Lista()
        lista_artistas = self.obtenerListaArtistas()
        
        contador = 1
        longitud = lista_artistas.obtenerLongitud()
        artista_actual = lista_artistas.encontrarPorIndiceInicioFinal(contador).obtenerDato()
        while contador <= longitud:
            lista_albumes_artista = Lista()
            lista_albumes_artista = artista_actual.obtenerListaAlbumes()
            lista_albumes.agregarALaLista(lista_albumes_artista)
        return lista_albumes
    
    #Retorna todas las canciones (recorre la lista de todos los albumes)
    def obtenerTodasLasCanciones(self):
        lista_canciones = Lista()
        lista_albumes = Lista()
        lista_albumes = self.obtenerListaAlbumes()
        
        #Recorrer la lista de los albumes 
        longitud = lista_albumes.obtenerLongitud()
        contador_album = 1
        
        while contador_album <= longitud: 
            album_actual = lista_albumes.encontrarPorIndiceFinalInicio(contador_album).obtenerDato()
            lista_canciones_album = album_actual.obtenerLiataCanciones()
            
            #Recorrer la lista de canciones del album y añadirla a la lista
            longitud_album = album_actual.obtenerLongitud()
            contador_cancion = 1
            while contador_cancion <= longitud_album: 
                cancion_actual = lista_canciones_album.encontrarPorIndiceInicioFinal(contador_cancion)
                lista_canciones.agregarALaLista(cancion_actual)
                contador_cancion += 1
        
        return lista_canciones        
            
            
    #Implementar logica para: 
    # agegar una cancion
    # agregar un album 
    #
    # agregar una cancion a una lista de reproduccion
    # #