from app.lista.Lista import Lista 
from app.biblioteca.Artista import Artista

#Lista de artistas
class ColeccionArtistas: 
    
    def __init__(self):
        self._lista_artistas = Lista()
        
    def agregarArtista(self, nombre):
        artista = Artista(nombre)
        
        if self._lista_artistas.estaVacia():
            self._lista_artistas.agregarALaLista(artista)
            print("Artista", nombre, "agregado correctamente a la biblioteca")
            
        else: 
            contador = 0
            longitud = self._lista_artistas.obtenerLongitud()
            artista_actual = None
            
            while contador <= longitud:
                contador += 1  
                artista_actual = self._lista_artistas.encontrarPorIndiceInicioFinal(contador).obtenerDato()
                if artista_actual.obtenerNombre() == nombre:
                    print("Se encontro nuevamente el artista", nombre)
                    break

                else:
                    if contador == longitud:
                        #agregar el artista 
                        self._lista_artistas.agregarALaLista(artista)    

    def obtenerListaArtistas(self):
        return self._lista_artistas
    
    #Devuelve un artista en base a su nombre
    def obtenerArtista(self, nombre):
        longitud = self._lista_artistas.obtenerLongitud()
        contador = 1
        
        while contador <= longitud:
            artista_actual = self._lista_artistas.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            if artista_actual.obtenerNombre() == nombre:
                return artista_actual
            contador += 1
        
        return None
