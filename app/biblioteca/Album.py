from app.lista.Nodo import Nodo
from app.lista.Lista import Lista
from app.biblioteca.Cancion import Cancion

#Contiene albumes y singles (albumes con una sola cancion)
class Album: 
    def __init__(self, nombre, artista):
        self._nombre = nombre
        self._artista = artista
        self._lista_canciones = Lista()
        
    def agregarCancion(self ,nombre, imagen, ruta):
        cancion = Cancion(nombre, self._artista, self._nombre, imagen, ruta)
        #self._lista_canciones.agregarALaLista(cancion)

        if self._lista_canciones.estaVacia():
            self._lista_canciones.agregarALaLista(cancion)
            print ("Se ha agregado la cancion:", nombre, "al album:", self._nombre)
        else:
            contador = 1
            longitud = self._lista_canciones.obtenerLongitud()
            cancion_actual = self._lista_canciones.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            
            while contador <= longitud: 
                if cancion_actual.obtenerNombre() == nombre: 
                    print("Se encontro nuevamente la cancion", nombre, "del album", self._nombre)
                    break; 
                else: 
                    if contador == longitud: 
                        #agregar la cancion
                        self._lista_canciones.agregarALaLista(cancion)
                        print("Se ha agregado la cancion", nombre, "al album", self._nombre)
                contador += 1
                cancion_actual = cancion_actual = self._lista_canciones.encontrarPorIndiceInicioFinal(contador).obtenerDato()
    
    def obtenerListaCanciones(self):
        return self._lista_canciones
    
    
    def obtenerNombre(self):
        return self._nombre