from app.lista.Lista import Lista

from app.biblioteca.Biblioteca import Biblioteca
from app.biblioteca.Cancion import Cancion

cancion1 = Cancion("Malice", "Osiah", "Kairos", "Imgggen", "Escritorio: Malice.mp3")
cancion2 = Cancion("Disillusion", "Osiah", "Kairos", "Imagggen", "Escritorio: Disillusion.mp3")

cancion3 = Cancion("Nina", "Mon", "1940 Carmen", "1940 Carmen.jpg", "Escritorio: Nina.mp3")
cancion4 = Cancion("Zombie", "Mon", "1940 Carmen", "1940 Carmen.jpg", "Escritorio: Zombie.mp3")

cancion5 = Cancion("Mew", "Mon", "Auto", "Auto.jpg", "Mew.mp3")
cancion6 = Cancion("Mew", "Mon", "Auto", "Auto.jpg", "Mew.mp3")


biblioteca = Biblioteca()

biblioteca.agregarCancionPorObjeto(cancion1)
biblioteca.agregarCancionPorObjeto(cancion2)
biblioteca.agregarCancionPorObjeto(cancion3)
biblioteca.agregarCancionPorObjeto(cancion4)
biblioteca.agregarCancionPorObjeto(cancion5)
biblioteca.agregarCancionPorObjeto(cancion6)


print("\nBiblioteca de canciones agregada correctamente!\n")
print("Obtener canciones:")

lista_canciones = Lista()
lista_canciones = biblioteca.obtenerTodasLasCanciones()
contador = 0
while contador < lista_canciones.obtenerLongitud():
    contador += 1
    cancion_actual = lista_canciones.encontrarPorIndiceInicioFinal(contador).obtenerDato()
    cancion_actual.imprimirCancion()

print("\n\n\n\n\n\n\n\n")
print("agregando listas de reproduccion\n")
biblioteca.agregarListaReproduccion("Lista de reproduccion numero uno")
biblioteca.agregarListaReproduccion("Lista de reproduccion numero dos")
biblioteca.agregarListaReproduccion("Lista de reproduccion numero uno")
biblioteca.agregarListaReproduccion("Lista de reproduccion numero tres")
