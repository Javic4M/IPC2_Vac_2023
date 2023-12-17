import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

from app.biblioteca.Biblioteca import Biblioteca
from app.biblioteca.Cancion import Cancion
from app.lista.Lista import Lista
from app.reporte.Reporte import Reporte
from app.reproductor.Reproductor import Reproductor
from app.manejoDatos.Importar import Importar

#Imports
biblioteca = Biblioteca()
importar = Importar()
#------------------------------


#Inicio Ventana
root = tk.Tk()
root.title("Reproductor de Música")
root.geometry("1024x720")
root.configure(bg="#333333")
root.resizable(False, False)
#-------------------------------

#Ejemplo Listas
lista_de_listas = [
    ("ruta/imagen1.png", "Lista 1"),
    ("ruta/imagen2.png", "Lista 2"),
]


# Obtener artistas únicos
#canciones_unicas = list(set(cancion[0] for cancion in lista_de_canciones))

# Obtener artistas únicos
#artistas_unicos = list(set(cancion[1] for cancion in lista_de_canciones))

# Obtener álbumes únicos
#albumes_unicos = list(set(cancion[2] for cancion in lista_de_canciones))

#-------------------------------

#Funciones
def menuEnter(boton):
    global boton_activo
    if boton_activo is not boton:
        boton.config(bg='gray')
    
def menuExit(boton):
    global boton_activo
    if boton_activo is not boton:
        boton.config(bg='#4F4F4F')
    
def change_color(boton):
    global boton_activo
    if boton_activo is not None:
        boton_activo.config(bg="#4F4F4F")
    boton.config(bg='purple')
    boton_activo = boton

def fill_canciones(self):
    for widget in lista_canciones.winfo_children():
        widget.destroy()

    #for cancion in listCanciones:
    #    label_cancion = tk.Label(lista_canciones, text=cancion, bg="#444444", fg="white")
    #    label_cancion.pack()
    listaCanciones = biblioteca.obtenerTodasLasCanciones()
    sizeLista = listaCanciones.obtenerLongitud() + 1
    
    for i in range(0, sizeLista):
        label_cancion = tk.Label(lista_canciones, text=f"{listaCanciones.obtenerPorIndice(i).get_nombre()}", bg="#444444", fg="white")
        label_cancion.pack()


#def fill_albumes(listAlbumes):
    #for widget in lista_albumes.winfo_children():
        #widget.destroy()

    #for album in listAlbumes:
        #label_album = tk.Label(lista_albumes, text=album, bg="#444444", fg="white")
        #label_album.pack()

#def fill_artistas(listArtistas):
    #for widget in lista_artistas.winfo_children():
        #widget.destroy()

    #for artista in listArtistas:
        #label_artista = tk.Label(lista_artistas, text=artista, bg="#444444", fg="white")
        #label_artista.pack()
        
def openCargarApp():
    cargarApp = MP3InfoApp()
    
#------------------------------------------

#Clase para el contenedor de listas
class ContenedorListas(tk.Frame):
    def __init__(self, parent, image_path, list_name, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.config(borderwidth=4, highlightbackground="#6A0DAD", highlightthickness=4, bg=parent['bg'])

        self.image_label = tk.Label(self, bg=parent['bg'])
        self.image_label.pack(side=tk.LEFT)

        self.name_label = tk.Label(self, text=list_name, bg=parent['bg'], fg="white")
        self.name_label.pack(side=tk.LEFT, padx=10)

        self.options_button = tk.Button(self, text="...", command=self.show_options, bg=parent['bg'], bd=0)
        self.options_button.pack(side=tk.RIGHT)


    def load_image(self, path):
        image = tk.PhotoImage(file=path)
        image = image.subsample(2)
        self.image_label.config(image=image)
        self.image_label.image = image

    def show_options(self):
        pass

#------------------------------------------

#Clase para cargar archivos
class MP3InfoApp:
    def __init__(self):
        self.open_mp3_info()

    def open_mp3_info(self):
        mp3_info_window = MP3InfoGUI()

class MP3InfoGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('MP3 Info')
        self.root.geometry('300x150')

        self.open_button = ttk.Button(self.root, text='Open a File', command=self.select_file)
        self.open_button.pack(expand=True)

        self.xml_button = ttk.Button(self.root, text="Open XML", command=self.select_xml)
        self.xml_button.pack(expand=True)
    
    def select_xml(self):
        lista = Lista()
        lista = importar.importar_biblioteca()
        valor = lista.obtenerLongitud()
        print(valor)
        for i in range(0, valor):
            cancion = lista.obtenerPorIndice(i)
            print(cancion.get_nombre())
            biblioteca.agregarCancionPorObjeto(cancion)
        self.root.destroy()

    def select_file(self):
        filetypes = (
            ('MP3 files', '*.mp3'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        if filename:
            self.show_info_window(filename)

    def manual_entry(self, filename):
        info_window = tk.Toplevel(root)
        info_window.title('Manual Entry')
        info_window.geometry('300x200')

        def submit_info():
            title_value = title_entry.get()
            artist_value = artist_entry.get()
            album_value = album_entry.get()

            showinfo(
                title='Manual Entry Info',
                message=f'File: {filename}\nTitle: {title_value}\nArtist: {artist_value}\nAlbum: {album_value}'
            )
            biblioteca.agregarCancionPorDatos(title_value, artist_value, album_value, "", filename)
            info_window.destroy()
            self.root.destroy()


        title_label = ttk.Label(info_window, text='Title:')
        title_label.pack()

        title_entry = ttk.Entry(info_window)
        title_entry.pack()

        artist_label = ttk.Label(info_window, text='Artist:')
        artist_label.pack()

        artist_entry = ttk.Entry(info_window)
        artist_entry.pack()

        album_label = ttk.Label(info_window, text='Album:')
        album_label.pack()

        album_entry = ttk.Entry(info_window)
        album_entry.pack()

        submit_button = ttk.Button(info_window, text='Submit', command=submit_info)
        submit_button.pack()

    def show_info_window(self, filename):
        info_window = tk.Toplevel(self.root)
        info_window.title('MP3 File Information')
        info_window.geometry('300x200')

        def auto_info():
            audio = MP3(filename, ID3=ID3)
            tags = audio.tags

            if tags:
                title = tags.get('TIT2') if 'TIT2' in tags else "Unknown Title"
                artist = tags.get('TPE1') if 'TPE1' in tags else "Unknown Artist"
                album = tags.get('TALB') if 'TALB' in tags else "Unknown Album"
                
                for tag in audio.tags.values():
                    if isinstance(tag, APIC):
                        image_data = tag.data
                        with open('album_art.jpg', 'wb') as img_file:
                            img_file.write(image_data)

                showinfo(
                    title='MP3 File Information',
                    message=f'File: {filename}\nTitle: {title}\nArtist: {artist}\nAlbum: {album}\nAlbum art saved as album_art.jpg'
                )
            else:
                showinfo(
                    title='MP3 File Information',
                    message=f'File: {filename}\nNo tags found in this MP3 file'
                )
            biblioteca.agregarCancionPorDatos(title, artist, album, "", filename)
            info_window.destroy()
            self.root.destroy()

        auto_button = ttk.Button(info_window, text='Auto Fill Info', command=auto_info)
        auto_button.pack()

        manual_button = ttk.Button(info_window, text='Manual Entry', command=lambda:self.manual_entry(filename))
        manual_button.pack()
#------------------------------------------

#Frames
menu_frame = tk.Frame(root, width=266, height=600, bg="#4F4F4F")
menu_frame.pack(side=tk.LEFT, anchor="n", padx=16, pady=16)
menu_frame.propagate(False)

reproductor_frame = tk.Frame(root, width=1024, height=130, bg="#4F4F4F")
reproductor_frame.place(rely=0.8972)
reproductor_frame.propagate(False)

framesOpciones = {
    'listas_frame': tk.Frame(root, bg="#4F4F4F", width=700, height=600),
    'biblioteca_frame': tk.Frame(root, bg="#4F4F4F", width=700, height=600),
}

def mostrar_frame(frame_mostrar):
    for frame in framesOpciones.values():
        frame.pack_forget()
    
    framesOpciones[frame_mostrar].pack(side=tk.TOP, pady=100, fill = tk.BOTH, expand = True)
    framesOpciones[frame_mostrar].propagate(False)
    
def mostrar_listas():
    mostrar_frame('listas_frame')

def mostrar_biblioteca():
    mostrar_frame('biblioteca_frame')

#------------------------------------------

#Botones Menu
name = "cargar_button"
cargar_button = tk.Button(menu_frame, text="Cargar", bg="#4F4F4F", bd=0, height=3, fg="white", command=openCargarApp)
cargar_button.pack(fill=tk.X)

name = "listas_button"
listas_button = tk.Button(menu_frame, text="Listas", width=20, bg="#4F4F4F", bd=0, height=3, fg="white", command=mostrar_listas)
listas_button.pack(fill=tk.X)

name = "biblioteca_button"
biblioteca_button = tk.Button(menu_frame, text="Biblioteca", width=20, bg="#4F4F4F", bd=0, height=3, fg="white", command=mostrar_biblioteca)
biblioteca_button.pack(fill=tk.X)

name = "top_button"
top_button = tk.Button(menu_frame, text="Top", width=20, bg="#4F4F4F", bd=0, height=3, fg="white")
top_button.pack(fill=tk.X)

buttons = [cargar_button, listas_button, biblioteca_button, top_button]

for button in buttons:
    button.bind('<Button-1>', lambda event, b=button: change_color(b))
    button.bind('<Enter>', lambda event, b=button: menuEnter(b))
    button.bind('<Leave>', lambda event, b=button: menuExit(b))
    
boton_activo = None
#------------------------------------------


#Elementos Espacio Listas
titulo_listas = tk.Label(framesOpciones['listas_frame'], text="Listas Creadas", font=("Arial", 40), bg="#444444", fg="white")
titulo_listas.pack()

crear_lista_button = tk.Button(framesOpciones['listas_frame'], text="Crear Lista", bg="#555555", fg="white")
crear_lista_button.pack()

eliminar_lista_button = tk.Button(framesOpciones['listas_frame'], text="Eliminar Lista", bg="#555555", fg="white")
eliminar_lista_button.pack()

scrollbar = tk.Scrollbar(framesOpciones['listas_frame'])
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_canvas = tk.Canvas(framesOpciones['listas_frame'], yscrollcommand=scrollbar.set, bg="#444444")
lista_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=lista_canvas.yview)

for info_lista in lista_de_listas:
    image_path, list_name = info_lista
    container = ContenedorListas(lista_canvas, image_path, list_name)
    container.pack(padx=10, pady=10, fill=tk.X)
#---------------------------------------------


#Elementos Reproductor
back_button = tk.Button(reproductor_frame, text="Atras", bg="#333333", fg="white")
back_button.pack(side=tk.LEFT)

play_button = tk.Button(reproductor_frame, text="Play", bg="#333333", fg="white")
play_button.pack(side=tk.LEFT)

stop_button = tk.Button(reproductor_frame, text="Stop", bg="#333333", fg="white")
stop_button.pack(side=tk.LEFT)

forward_button = tk.Button(reproductor_frame, text="Adelante", bg="#333333", fg="white")
forward_button.pack(side=tk.LEFT)
#---------------------------------------------


#Elementos Biblioteca
def showCanvas(canvas_mostrar, canvas_ocultar):
    if isinstance(canvas_ocultar, list):
        for canvas in canvas_ocultar:
            canvas.pack_forget()
    else:
        canvas_ocultar.pack_forget()
    canvas_mostrar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    
    
scrollbar_biblioteca = tk.Scrollbar(framesOpciones['biblioteca_frame'])
scrollbar_biblioteca.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar_biblioteca.config(command=lista_canvas.yview)

lista_canciones = tk.Canvas(framesOpciones['biblioteca_frame'], yscrollcommand=scrollbar_biblioteca.set, bg="#444444")
label1 = tk.Label(lista_canciones, text="Aqui van canciones")
label1.pack()



lista_albumes = tk.Canvas(framesOpciones['biblioteca_frame'], yscrollcommand=scrollbar_biblioteca.set, bg="#444444")
label2 = tk.Label(lista_albumes, text="Aqui van albumes")
label2.pack()

lista_artistas = tk.Canvas(framesOpciones['biblioteca_frame'], yscrollcommand=scrollbar_biblioteca.set, bg="#444444")
label3 = tk.Label(lista_artistas, text="Aqui van artistas")
label3.pack()

titulo = tk.Label(framesOpciones['biblioteca_frame'], text="Biblioteca", font=("Arial", 40), bg="#444444", fg="white")
titulo.pack()

canciones_button = tk.Button(framesOpciones["biblioteca_frame"], text="canciones", command=lambda: showCanvas(lista_canciones, [lista_artistas, lista_albumes]))
canciones_button.pack(side=tk.TOP, anchor="w")

albumes_button = tk.Button(framesOpciones["biblioteca_frame"], text="albumes", command=lambda: showCanvas(lista_albumes, [lista_canciones, lista_artistas]))
albumes_button.pack(side=tk.TOP, anchor="e")

artistas_button = tk.Button(framesOpciones["biblioteca_frame"], text="artistas", command=lambda: showCanvas(lista_artistas, [lista_canciones, lista_albumes]))
artistas_button.pack(side=tk.TOP, anchor="n")

canciones_button.bind('<Button-1>', fill_canciones)
#albumes_button.bind('<Button-1>', fill_albumes)
#artistas_button.bind('<Button-1>', lfill_artistas)

#-----------------------------------------------------

root.mainloop()
