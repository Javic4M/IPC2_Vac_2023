from app.lista.Lista import Lista
from app.lista.Circular import ListaCircular

from app.biblioteca.Artista import Artista 
from app.biblioteca.Album import Album
from app.biblioteca.Cancion import Cancion
from app.biblioteca.ColeccionArtistas import ColeccionArtistas
from app.biblioteca.ListaDeReproduccion import ListaDeReproduccion

from app.persistencia.PersistirListas import PersistirListas

#Controla la totalidad de la biblioteca de música 
class Biblioteca: 
    def __init__(self): 
        self._coleccion_artistas = ColeccionArtistas()
        self._coleccion_listas_reproduccion = Lista()
        self._persistirListas = PersistirListas()
    
    #Retorna una lista doble enlazada con todos los artistas
    def obtenerListaArtistas(self):
        return self._coleccion_artistas.obtenerListaArtistas()
    
    #Retorna una lista con todos los albumes(recorre la lista de artistas para obtenerla)
    def obtenerListaAlbumes(self):
        lista_albumes = Lista()
        lista_artistas = self.obtenerListaArtistas()
        
        contador = 0
        longitud = lista_artistas.obtenerLongitud()
        artista_actual = None

        #Recorrer los artistas
        while contador < longitud:
            contador += 1
            artista_actual = lista_artistas.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            
            #Recorrer los albumes de los artistas
            lista_albumes_artista = artista_actual.obtenerListaAlbumes()
            longitud_albumes_artista = lista_albumes_artista.obtenerLongitud()
            contador_albumes_artista = 0
            
            while contador_albumes_artista < longitud_albumes_artista:
                contador_albumes_artista += 1
                album_actual = lista_albumes_artista.encontrarPorIndiceInicioFinal(contador_albumes_artista)
                lista_albumes.agregarALaLista(album_actual)

        return lista_albumes
    
    #Retorna todas las canciones (recorre la lista de todos los albumes)
    def obtenerTodasLasCanciones(self):
        lista_canciones = Lista()
        lista_albumes = Lista()
        lista_albumes = self.obtenerListaAlbumes()
        
        #Recorrer la lista de los albumes 
        longitud = lista_albumes.obtenerLongitud()
        contador_album = 0
        
        while contador_album <= longitud: 
            #Obtener el objeto Album
            contador_album += 1 
            album_actual = lista_albumes.encontrarPorIndiceFinalInicio(contador_album).obtenerDato().obtenerDato()
            lista_canciones_album = album_actual.obtenerListaCanciones()
            
            #Recorrer la lista de canciones del album y añadirla a la lista
            longitud_album = lista_canciones_album.obtenerLongitud()
            contador_cancion = 1
            while contador_cancion <= longitud_album: 
                #contador_cancion += 1
                cancion_actual = lista_canciones_album.encontrarPorIndiceInicioFinal(contador_cancion).obtenerDato()
                lista_canciones.agregarALaLista(cancion_actual)
                #cancion_actual.imprimirCancion()
                contador_cancion += 1
            
        return lista_canciones        
    
    #Agrega una cancion en base a su informacion
    def agregarCancionPorDatos(self, nombre, artista, album, imagen, ruta):
        cancion = Cancion(nombre, artista, album, imagen, ruta)
        self.agregarCancionPorObjeto(cancion)
    
    #Agrega una cancion en base a un objeto cancion            
    def agregarCancionPorObjeto(self, cancion):
        album = cancion.get_album()
        artista = cancion.get_artista()
        
        #1.1. Agregar al artista:
        self._coleccion_artistas.agregarArtista(artista)
        #1.2. Obtener al artista
        objeto_artista = self._coleccion_artistas.obtenerArtista(artista)
        
        #2.1 Agregar el album
        objeto_artista.agregarAlbum(album)
        #2.2 Obtener el album
        objeto_album = objeto_artista.obtenerAlbum(album)
        
        #3. Agregar la cancion
        nombre_cancion = cancion.get_nombre()
        artista_cacion = cancion.get_artista()
        album_cancion = cancion.get_album()
        imagen_cancion = cancion.get_imagen()
        ruta_cancion = cancion.get_ruta()
        objeto_album.agregarCancion(nombre_cancion, imagen_cancion, ruta_cancion)
    
    
    
    
    
    
    def obtenerListasReproduccion(self):
        return self._coleccion_listas_reproduccion
    
    def obtenerListaReproduccion(self, nombre):
        longitud = self._coleccion_listas_reproduccion.obtenerLongitud()
        contador = 1
        while contador <= longitud:
            lista_actual = self._coleccion_listas_reproduccion.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            if nombre == lista_actual.obtenerNombre():
                return lista_actual
            contador += 1
        return None
    
    
    #Crea una lista de reproduccion en base a un nombre     
    def agregarListaReproduccion(self, nombre):
        #1. verificar si hay una lista de reproduccion con ese nombre
        lista_a_agregar = self.obtenerListaReproduccion(nombre)
        if(lista_a_agregar == None):
            #2. Crear la lista y agregarla
            lista_a_agregar = ListaDeReproduccion(nombre)
            self._coleccion_listas_reproduccion.agregarALaLista(lista_a_agregar)
            print("Lista", nombre, "agregada correctamente!!!!!!")
        else:
            print("La lista de reproduccion", nombre, "ya existe por lo que no se agregara")
    
    # Establece una lista con listas de reproduccion
    def cargargarListasReproduccion(self, listas_reproduccion):
        if listas_reproduccion != None:
            self._coleccion_listas_reproduccion = listas_reproduccion
            print("Listas de reproduccion agregadas correctamente")
            
    #Agrega un objeto cancion a una lista de reproduccion en base a un nombre 
    def agregarCancionAListaReproduccion(self, cancion, nombre_lista):
        #Buscar la lista de reproduccion
        lista = self.obtenerListaReproduccion(nombre_lista)
        if lista == None: 
            self.agregarListaReproduccion(nombre_lista)
            lista = self.obtenerListaReproduccion(nombre_lista)
        
        if(lista != None):
            #Agregar la cancion
            lista.agregarCancion(cancion)
            
            lista_canciones = lista.obtenerListaCanciones()
            self._persistirListas.persistir(nombre_lista, lista_canciones)
            
            print ("La cancion: ", cancion.obtenerNombre(), "ha sido agregada correctamente a la lista de reproduccion", nombre_lista, "!!!!!")
        
    #Implementar logica para: 
    # agegar una cancion
    # agregar un album 
    #
    # agregar una cancion a una lista de reproduccion
    # #