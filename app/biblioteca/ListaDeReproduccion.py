from app.biblioteca.Cancion import Cancion

from app.lista.Circular import ListaCircular


#Lista de reproduccion (basada en lista circular)
class ListaDeReproduccion: 
    
    def __init__(self, nombre):
        self._nombre = nombre
        self._lista_canciones = ListaCircular()
        
    #Recibe un objeto cancion    
    def agregarCancion(self, cancion):
        nombre = cancion.obtenerNombre
        
        if self._lista_canciones.estaVacia():
            self._lista_canciones.agregarALaLista(cancion)
            print ("Se ha agregado la cancion:", nombre, "a la lista de reproduccion:", self._nombre)
        else:
            contador = 1
            longitud = self._lista_canciones.obtenerLongitud()
            cancion_actual = self._lista_canciones.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            
            while contador <= longitud: 
                if cancion_actual.obtenerNombre() == nombre: 
                    print("Se encontro nuevamente la cancion", nombre, "al intentar agregarla a la lista de reproduccion", self._nombre)
                    break; 
                else: 
                    if contador == longitud: 
                        #agregar la cancion
                        self._lista_canciones.agregarALaLista(cancion)
                        print("Se ha agregado la cancion", nombre, "a la lista de reproduccion", self._nombre)
                contador += 1
                cancion_actual = self._lista_canciones.encontrarPorIndiceInicioFinal(contador).obtenerDato()

    def obtenerListaCanciones(self):
        return self._lista_canciones
    
    
    def obtenerNombre(self):
        return self._nombre