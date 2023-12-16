import os
import xml.etree.ElementTree as ET
from tkinter import filedialog
import tkinter as tk
from app.biblioteca.Cancion import Cancion
from app.lista.Lista import Lista

class Importar:
    def __init__(self):
        self.lista_retornar = Lista()

    def abrir_cuadro_dialogo():
        root = tk.Tk()
        root.withdraw() 

        # Abre el cuadro de diálogo para seleccionar un archivo
        archivo_seleccionado = filedialog.askopenfilename(title="Selecciona un archivo para la biblioteca de musica")

        # Verifica si se seleccionó un archivo
        if archivo_seleccionado:
            return archivo_seleccionado
        else:
            print("No se seleccionó ningún archivo.")


        #pruebas para importacion de datos
    #script_dir = os.path.dirname(os.path.realpath(__file__))
    #file_path = os.path.join(script_dir, 'plants.xml')

    #archivo = ET.parse(r'C:\Users\Usuario\Desktop\VAC IPC2 D2023\Proyecto1\IPC2_Vac_2023\app\manejo-datos\ejemplo.xml')


    def importar_biblioteca():
        tree = open(abrir_cuadro_dialogo())
        xml_data = ET.fromstring(tree.read())
        lst_canciones = xml_data.findall('cancion')


        for song in lst_canciones:
            nombre = song.attrib.get('nombre').strip('"')
            artista = song.find('artista').text.strip('"')
            album = song.find('album').text.strip('"')
            imagen = song.find('imagen').text.strip('"')
            ruta = song.find('ruta').text.strip('"')

            cancion = Cancion(nombre, artista, album, imagen, ruta)
            self.lista_retornar.agregarALaLista(cancion)




            #with open(ruta_relativa, 'r') as archivo:
            #    contenido = archivo.read()
            #    print(contenido)

            #rutasss = "C:/Users/Usuario/Desktop/VAC IPC2 D2023/Proyecto1/IPC2_Vac_2023/app/manejo-datos/segunda.txt"
            


            #archivo = open(ruta)
            #print(archivo)
        return self.lista_retornar



    
    

