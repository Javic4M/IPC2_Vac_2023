#Persiste listas de reproduccion
import xml.etree.ElementTree as ET
from app.biblioteca.Cancion import Cancion
from app.lista.Lista import Lista
 

class PersistirListas:
    def __init__(self):
        self.lista = None
        self.ruta = "./Listas de reproduccion.xml"

    def persistir(self, nombre_lista, lista):
        tree = None
        try:
            # Cargar el archivo XML existente
            tree = ET.parse(self.ruta)
            root = tree.getroot()
        except FileNotFoundError:
            # Si el archivo no existe, crear uno nuevo con el elemento raíz
            root = ET.Element("ListasReproduccion")
            tree = ET.ElementTree(root)
    
        # Verificar si la lista ya existe en el XML
        lista_existente = root.find(f"./Lista[@nombre='{nombre_lista}']")
        if lista_existente is not None:
            # Agregar elementos a la lista existente
            for i in range(1, lista.obtenerLongitud() + 1):
                cancion = lista.obtenerPorIndice(i)
                cancion_nombre = cancion.obtenerNombre()
                cancion_album = cancion.obtenerAlbum()
                cancion_existente = lista_existente.find(f"./cancion[@nombre='{cancion_nombre}'][album='{cancion_album}']")
                if cancion_existente is None:
                    # La canción no existe en la lista, agregarla
                    cancion_element = ET.SubElement(lista_existente, "cancion", nombre=cancion_nombre)
    
                    artista_element = ET.SubElement(cancion_element, "artista")
                    artista_element.text = cancion.obtenerArtista()
    
                    album_element = ET.SubElement(cancion_element, "album")
                    album_element.text = cancion_album
    
                    imagen_element = ET.SubElement(cancion_element, "imagen")
                    imagen_element.text = cancion.obtenerImagen()
    
                    ruta_element = ET.SubElement(cancion_element, "ruta")
                    ruta_element.text = cancion.obtenerRuta()
        else:
            # Crear un nuevo elemento Lista dentro del elemento raíz
            lista_element = ET.SubElement(root, "Lista", nombre=nombre_lista)
    
            # Recorrer la lista y agregar elementos canción
            for i in range(1, lista.obtenerLongitud() + 1):
                cancion = lista.obtenerPorIndice(i)
                cancion_nombre = cancion.obtenerNombre()
                cancion_album = cancion.obtenerAlbum()
                cancion_existente = lista_element.find(f"./cancion[@nombre='{cancion_nombre}'][album='{cancion_album}']")
                if cancion_existente is None:
                    # La canción no existe en la lista, agregarla
                    cancion_element = ET.SubElement(lista_element, "cancion", nombre=cancion_nombre)
    
                    artista_element = ET.SubElement(cancion_element, "artista")
                    artista_element.text = cancion.obtenerArtista()
    
                    album_element = ET.SubElement(cancion_element, "album")
                    album_element.text = cancion_album
    
                    imagen_element = ET.SubElement(cancion_element, "imagen")
                    imagen_element.text = cancion.obtenerImagen()
    
                    ruta_element = ET.SubElement(cancion_element, "ruta")
                    ruta_element.text = cancion.obtenerRuta()
    
        # Guardar el árbol XML actualizado en el archivo
        tree.write(self.ruta)
    