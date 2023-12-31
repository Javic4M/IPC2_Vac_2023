from app.lista.Lista import Lista
import tkinter as tk


from app.biblioteca.Biblioteca import Biblioteca
from app.biblioteca.Cancion import Cancion
from app.reporte.Reporte import Reporte

from app.reproductor.Reproductor import Reproductor

from app.persistencia.PersistirListas import PersistirListas

from app.biblioteca.ListaDeReproduccion import ListaDeReproduccion

from app.ui.VentanaPrincipal import VentanaPrincipal

ruta_escritorio = "C:/Users/Jorge/OneDrive/Escritorio/"

nectar = ruta_escritorio + "nectar.png"
cancion1 = Cancion("Normal People", "Joji", "Nectar", nectar, "C:/Users/Jorge/OneDrive/Escritorio/Joji  Normal People ft rei brown.mp3")
cancion2 = Cancion("NITRUS",        "Joji", "Nectar", nectar, "C:/Users/Jorge/OneDrive/Escritorio/Joji NITROUS.mp3")
cancion3 = Cancion("Afterthought",  "Joji", "Nectar", nectar, "C:/Users/Jorge/OneDrive/Escritorio/Joji Afterthought.mp3")
cancion4 = Cancion("777",           "Joji", "Nectar", nectar, "C:/Users/Jorge/OneDrive/Escritorio/Joji 777.mp3")

c1 = cancion1


#cancion5 = Cancion("Mew", "Mon", "Auto", "Auto.jpg", "Mew.mp3")
#cancion6 = Cancion("Mew", "Mon", "Auto", "Auto.jpg", "Mew.mp3")


biblioteca = Biblioteca()

biblioteca.agregarCancionPorObjeto(cancion1)
biblioteca.agregarCancionPorObjeto(cancion2)
biblioteca.agregarCancionPorObjeto(cancion3)
biblioteca.agregarCancionPorObjeto(cancion4)

smithereens = ruta_escritorio +"smithereens.jpg"
cancion1 = Cancion("Dissolve", "Joji", "Smithereens", smithereens, "C:/Users/Jorge/OneDrive/Escritorio/Joji - Dissolve.mp3")
cancion2 = Cancion("YUKON",        "Joji", "Smithereens", smithereens, "C:/Users/Jorge/OneDrive/Escritorio/Joji - YUKON.mp3")
cancion3 = Cancion("BLAHBLAHBLAH DEMO",  "Joji", "Smithereens", smithereens, "C:/Users/Jorge/OneDrive/Escritorio/Joji - DEMO.mp3")
biblioteca.agregarCancionPorObjeto(cancion1)
biblioteca.agregarCancionPorObjeto(cancion2)
biblioteca.agregarCancionPorObjeto(cancion3)
c2 = cancion1

autopoietica = ruta_escritorio +"Autopoietica.jpg"
cancion1 = Cancion("Prendele fuego",    "Mon Laferte", "Autopoietica", autopoietica, "C:/Users/Jorge/OneDrive/Escritorio/Mon - Prendele Fuego.mp3")
cancion2 = Cancion("Pornocracia",       "Mon Laferte", "Autopoietica", autopoietica, "C:/Users/Jorge/OneDrive/Escritorio/Mon - Pornocracia.mp3")
cancion3 = Cancion("Amantes suicidas",  "Mon Laferte", "Autopoietica", autopoietica, "C:/Users/Jorge/OneDrive/Escritorio/Mon - Amantes Suicidas.mp3")
biblioteca.agregarCancionPorObjeto(cancion1)
biblioteca.agregarCancionPorObjeto(cancion2)
biblioteca.agregarCancionPorObjeto(cancion3)
c3 = cancion1

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
#biblioteca.agregarListaReproduccion("Lista de reproduccion numero uno")
#biblioteca.agregarListaReproduccion("Lista de reproduccion numero dos")
#biblioteca.agregarListaReproduccion("Lista de reproduccion numero uno")
#biblioteca.agregarListaReproduccion("Lista de reproduccion numero tres")


reproductor = Reproductor()
reproductor.establecerListaAReproducir(lista_canciones)
reproductor.reproduccionAleatoria()

reproductor.reproducir()

opcion = None
print("\n\n\n\n\n\n\n Reproductor\n")
#while opcion != "s":
#    print("s: salir")
#    print("p: pausar")
#    print("r: reanudar")
#    print("a: avanzar")
#    print("t: atras")
#    
#    print("i: aleatoio")
#    print("n: no aleatorio")
#    opcion = input()
#    
#    if opcion == "s": 
#        break
#    elif opcion == "p":
#        reproductor.pausar()
#    elif opcion == "r":
#        reproductor.reanudar()
#    elif opcion == "a":
#        reproductor.avanzar()
#    elif opcion == "t":
#        reproductor.retroceder()
#    
#    elif opcion == "i":
#        reproductor.reproduccionAleatoria()
#    elif opcion == "n":
#        reproductor.reproduccionNoAleatoria()
#        
#        
#lista = Lista()
#c1 = Cancion("Cancion 1", "Artista 1", "Album 1", "imagen1.jpg", "ruta1.mp3")
#c2 = Cancion("Cancion 2", "Artista 2", "Album 2", "imagen2.jpg", "ruta2.mp3")
#c3 = Cancion("Cancion 3", "Artista 3", "Album 3", "imagen3.jpg", "ruta3.mp3")
#
biblioteca.agregarListaReproduccion("Lista de prueba")
biblioteca.agregarCancionAListaReproduccion(c1, "Lista de prueba")
biblioteca.agregarCancionAListaReproduccion(c2, "Lista de prueba")
biblioteca.agregarCancionAListaReproduccion(c3, "Lista de prueba")



#persistir_listas = PersistirListas()
#
#persistir_listas.persistir("Lista de reproduccion 1", lista)
#persistir_listas.persistir("Todas las canciones", lista_canciones)

ventana = VentanaPrincipal(biblioteca, reproductor)
ventana.mainloop()