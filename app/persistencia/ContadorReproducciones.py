import xml.etree.ElementTree as ET

from app.reporte.Reporte import Reporte


class ContadorCanciones:
    def __init__(self):
        self.ruta = "./contador.xml"
        self.reporte = Reporte(self.ruta)

    def actualizar_contador(self, cancion):
        try:
            tree = ET.parse(self.ruta)
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("contador")
            tree = ET.ElementTree(root)

        cancion_existente = root.find(f"./cancion[@nombre='{cancion.obtenerNombre()}'][album='{cancion.obtenerAlbum()}']")
        if cancion_existente is not None:
            reproducciones_element = cancion_existente.find("reproducciones")
            reproducciones = int(reproducciones_element.text)
            reproducciones += 1
            reproducciones_element.text = str(reproducciones)
        else:
            cancion_element = ET.SubElement(root, "cancion", nombre=cancion.obtenerNombre())
            artista_element = ET.SubElement(cancion_element, "artista")
            artista_element.text = cancion.obtenerArtista()
            album_element = ET.SubElement(cancion_element, "album")
            album_element.text = cancion.obtenerAlbum()
            imagen_element = ET.SubElement(cancion_element, "imagen")
            imagen_element.text = cancion.obtenerImagen()
            reproducciones_element = ET.SubElement(cancion_element, "reproducciones")
            reproducciones_element.text = "1"

        tree.write(self.ruta)
        self.reporte.write_file()