from app.lista.Lista import Lista

from app.biblioteca.Biblioteca import Biblioteca
from app.biblioteca.Cancion import Cancion
from app.reporte.Reporte import Reporte

from app.reproductor.Reproductor import Reproductor

from app.persistencia.PersistirListas import PersistirListas

from app.biblioteca.ListaDeReproduccion import ListaDeReproduccion

cancion1 = Cancion("Recover", "CHVRCHES", "Nectar", "Imgggen", "/home/giovanic/Música/2013 - The Bones of What You Believe (EU Limited Edition) FLAC/07 - Recover.flac")
cancion2 = Cancion("The Mother We Share",        "CHVRCHES", "Nectar", "Imagggen", "/home/giovanic/Música/2013 - The Bones of What You Believe (EU Limited Edition) FLAC/01 - The Mother We Share.flac")
cancion3 = Cancion("Gun",  "Joji", "CHVRCHES", "1940 Carmen.jpg", "/home/giovanic/Música/2013 - The Bones of What You Believe (EU Limited Edition) FLAC/03 - Gun.flac")
cancion4 = Cancion("Tether",           "CHVRCHES", "Nectar", "1940 Carmen.jpg", "/home/giovanic/Música/2013 - The Bones of What You Believe (EU Limited Edition) FLAC/04 - Tether.flac")

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
        
        
# lista = Lista()
# c1 = Cancion("Cancion 1", "Artista 1", "Album 1", "imagen1.jpg", "ruta1.mp3")
# c2 = Cancion("Cancion 2", "Artista 2", "Album 2", "imagen2.jpg", "ruta2.mp3")
# c3 = Cancion("Cancion 3", "Artista 3", "Album 3", "imagen3.jpg", "ruta3.mp3")

# biblioteca.agregarListaReproduccion("Lista de reproduccion con canciones ficticias")
# biblioteca.agregarCancionAListaReproduccion(c1, "Lista de reproduccion con canciones ficticias")
# biblioteca.agregarCancionAListaReproduccion(c2, "Lista de reproduccion con canciones ficticias")
# biblioteca.agregarCancionAListaReproduccion(c3, "Lista de reproduccion con canciones ficticias")


#persistir_listas = PersistirListas()
#
#persistir_listas.persistir("Lista de reproduccion 1", lista)
#persistir_listas.persistir("Todas las canciones", lista_canciones)