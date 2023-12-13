from app.lista.Lista import Lista

from app.biblioteca.Biblioteca import Biblioteca
from app.biblioteca.Cancion import Cancion

from app.reproductor.Reproductor import Reproductor

cancion1 = Cancion("Normal People", "Joji", "Nectar", "Imgggen", "C:/Users/Jorge/OneDrive/Escritorio/Joji  Normal People ft rei brown.mp3")
cancion2 = Cancion("NITRUS",        "Joji", "Nectar", "Imagggen", "C:/Users/Jorge/OneDrive/Escritorio/Joji NITROUS.mp3")
cancion3 = Cancion("Afterthought",  "Joji", "Nectar", "1940 Carmen.jpg", "C:/Users/Jorge/OneDrive/Escritorio/Joji Afterthought.mp3")
cancion4 = Cancion("777",           "Joji", "Nectar", "1940 Carmen.jpg", "C:/Users/Jorge/OneDrive/Escritorio/Joji 777.mp3")

#cancion5 = Cancion("Mew", "Mon", "Auto", "Auto.jpg", "Mew.mp3")
#cancion6 = Cancion("Mew", "Mon", "Auto", "Auto.jpg", "Mew.mp3")


biblioteca = Biblioteca()

biblioteca.agregarCancionPorObjeto(cancion1)
biblioteca.agregarCancionPorObjeto(cancion2)
biblioteca.agregarCancionPorObjeto(cancion3)
biblioteca.agregarCancionPorObjeto(cancion4)
#biblioteca.agregarCancionPorObjeto(cancion5)
#biblioteca.agregarCancionPorObjeto(cancion6)


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


reproductor = Reproductor()
reproductor.establecerListaAReproducir(lista_canciones)
reproductor.reproduccionAleatoria()

reproductor.reproducir()

opcion = None
print("\n\n\n\n\n\n\n Reproductor\n")
while opcion != "s":
    print("s: salir")
    print("p: pausar")
    print("r: reanudar")
    print("a: avanzar")
    print("t: atras")
    
    print("i: aleatoio")
    print("n: no aleatorio")
    opcion = input()
    
    if opcion == "s": 
        break
    elif opcion == "p":
        reproductor.pausar()
    elif opcion == "r":
        reproductor.reanudar()
    elif opcion == "a":
        reproductor.avanzar()
    elif opcion == "t":
        reproductor.retroceder()
    
    elif opcion == "i":
        reproductor.reproduccionAleatoria()
    elif opcion == "n":
        reproductor.reproduccionNoAleatoria()