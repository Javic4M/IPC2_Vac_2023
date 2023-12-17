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
            contador = 1
            longitud = self._lista_artistas.obtenerLongitud()
            artista_actual = self._lista_artistas.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            
            while contador <= longitud:
                if artista_actual.otenerNombre() == nombre:
                    print("Se encontro nuevamente el artista", nombre)
                    break

                else:
                    if contador == longitud:
                        #agregar el artista 
                        self._lista_artistas.agregarALaLista(artista)

    def obtenerListaArtistas(self):
        return self._lista_artistas
