import xml.etree.ElementTree as ET
from tkinter import filedialog
import tkinter as tk
from app.biblioteca.Cancion import Cancion
from app.lista.Lista import Lista

class Importar:
    def __init__(self):
        self.lista_retornar = Lista()

    def abrir_cuadro_dialogo(self):
        root = tk.Tk()
        root.withdraw() 

        archivo_seleccionado = filedialog.askopenfilename(title="Selecciona un archivo para la biblioteca de musica")
        
        if archivo_seleccionado:
            root.destroy()
            return archivo_seleccionado
        else:
            print("No se seleccionó ningún archivo")


    def importar_biblioteca(self):
        tree = open(self.abrir_cuadro_dialogo())
        xml_data = ET.fromstring(tree.read())
        lst_canciones = xml_data.findall('cancion')

        for song in lst_canciones:
            nombre = song.attrib.get('nombre').strip('"')
            artista = song.find('artista').text.strip('"')
            album = song.find('album').text.strip('"')
            imagen = song.find('imagen').text.strip('"').replace('\\', '/')
            ruta = song.find('ruta').text.strip('"').replace('\\', '/')

            cancion = Cancion(nombre, artista, album, imagen, ruta)
            self.lista_retornar.agregarALaLista(cancion)

        return self.lista_retornar