import tkinter as tk
from app.lista.Lista import Lista


from app.biblioteca.Biblioteca import Biblioteca
from app.reproductor.Reproductor import Reproductor

from app.manejo_datos.Importar import Importar
from app.manejo_datos.CargarListas import CargarListas

from app.ui.VentanaPrincipal import VentanaPrincipal


# Instanciar objetos de interes 
biblioteca = Biblioteca()
reproductor = Reproductor()
lista_canciones = Lista()

importar = Importar()
cargar_listas = CargarListas("./Listas de reproduccion.xml")


# Agregar las canciones desde el xml a la biblioteca
print("AGREGANDO CANCIONES DESDE XML")
contador = 1
lista_canciones = importar.importar_biblioteca()
while contador <= lista_canciones.obtenerLongitud():
    
    cancion = lista_canciones.obtenerPorIndice(contador)
    if cancion != None:
        biblioteca.agregarCancionPorObjeto(cancion)
        cancion.imprimirCancion()
    
    contador += 1


# Cargar listas de reprodccion desde el xml
listas_reproduccion = Lista()
listas_reproduccion = cargar_listas.cargarListas()
biblioteca.cargargarListasReproduccion(listas_reproduccion)

#reproductor.establecerListaAReproducir(biblioteca.obtenerTodasLasCanciones())

ventana_principal = VentanaPrincipal(biblioteca, reproductor)
ventana_principal.mainloop()

