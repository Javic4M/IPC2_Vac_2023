import xml.etree.ElementTree as ET
from app.biblioteca.Cancion import Cancion
from app.biblioteca.ListaDeReproduccion import ListaDeReproduccion

from app.lista.Circular import ListaCircular
from app.lista.Lista import Lista

class CargarListas:
    def __init__(self, ruta):
        self.ruta = ruta

    def cargarListas(self):
        try:
            tree = ET.parse(self.ruta)
            root = tree.getroot()
        except FileNotFoundError:
            print("El archivo XML no existe.")
            return None

        listas = Lista()

        for lista_element in root.findall("Lista"):
            nombre_lista = lista_element.get("nombre")
            lista_canciones = ListaCircular()

            for cancion_element in lista_element.findall("cancion"):
                nombre = cancion_element.get("nombre")
                artista = cancion_element.find("artista").text
                album = cancion_element.find("album").text
                imagen = cancion_element.find("imagen").text
                ruta = cancion_element.find("ruta").text

                cancion = Cancion(nombre, artista, album, imagen, ruta)
                lista_canciones.agregarALaLista(cancion)

            lista = ListaDeReproduccion(nombre_lista)
            lista.establecerListaCanciones(lista_canciones)
            listas.agregarALaLista(lista)

        return listas
