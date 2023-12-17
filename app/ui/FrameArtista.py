import tkinter as tk

from PIL import Image, ImageTk

from app.biblioteca.Artista import Artista
from app.lista.Lista import Lista
from app.ui.FrameAlbum import FrameAlbum

class FrameArtista(tk.Frame):
    
    def __init__(self, master, artista, reproductor, biblioteca, *args, **kwargs):
        """
            params: 
                master: ventana principal
                artista: objeto artista con los albumes a mostrar
        """
        super().__init__(master, *args, **kwargs, bg = "black")
        
        self.master = master
        self.artista = artista
        self.reproductor = reproductor
        self.biblioteca = biblioteca
        self.lista_frames_album = Lista()
        
        # Crear el label en la parte superior con el nombre del artista
        self.nombre_artista =  self.artista.obtenerNombre()
        label_artistas = tk.Label(self, text=self.nombre_artista, font=("Arial", 35, "bold"), bg="black", fg="white")
        label_artistas.grid(row=0, column=0, sticky="w", pady = 20, padx=15) 


        # Area de albumes ----------------------------------------------------------------
        # Crear un canvas escroleable
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.grid(row=1, column=0, sticky="nsew")

        # Crear un frame para contener los botones
        self.contenedor_botones = tk.Frame(self.canvas, bg="black")
        self.canvas.create_window((0, 0), window=self.contenedor_botones, anchor="nw")

        # Configurar el peso de la fila y la columna para que el frame se expanda
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Agregar un scrollbar al canvas
        scrollbar = tk.Scrollbar(self, command=self.canvas.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Configurar el canvas para que sea escroleable
        self.contenedor_botones.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Permitir desplazamiento con la rueda del mouse
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        # Creacion de botones para los albumes del artista ----------------------------------------------------------------
        self.contador_columnas = 0
        self.contador_filas = 0
        
        self.agregar_albums()


    def mostrar_frame(self):
        self.master.cambiar_vista(self)
        
    def agregar_nuevo(self, album):
        
        # Añadir una instancia de un botón al contenedor de botones con la imagen del album ----------------------------------------------------------------
        # Obtener la imagen del album 
        canciones = album.obtenerListaCanciones()
        cancion = canciones.obtenerPorIndice(1)
        ruta = cancion.obtenerImagen()
        if ruta == None or ruta == "":
            ruta = "./app/assets/comodin.jpg"
        
        imagen = None
        try:
            imagen = Image.open(ruta)
            imagen = imagen.resize((100,100))
            imagen = ImageTk.PhotoImage(imagen)
        except Exception as e:
            ruta = "./app/assets/comodin.jpg"
            imagen = Image.open(ruta)
            imagen = imagen.resize((100,100))
            imagen = ImageTk.PhotoImage(imagen)
            
            
            
        nombre = album.obtenerNombre()
        if nombre == None or nombre == "":
            nombre = "Album desconocido"


        frame_album = FrameAlbum(self.master, album, self.reproductor, self.biblioteca)
        nuevo_boton = tk.Button(self.contenedor_botones, image=imagen, compound="top", bg="#181818", fg="white", font=("Arial", 15, "bold"), highlightthickness=0, relief="flat", text=nombre, command=frame_album.mostrar_frame, width=140, height=140)
        #Mantener la referencia en la lista
        self.lista_frames_album.agregarALaLista(frame_album)
                
        # Mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        nuevo_boton.image = imagen

        if(self.contador_columnas == 6):
            self.contador_columnas = 0
            self.contador_filas += 1
        
        
        nuevo_boton.grid(row=self.contador_filas, column=self.contador_columnas, sticky="ew", pady = 20, padx= 20)
        self.contador_columnas += 1

    
    def agregar_albums(self):
        lista_albums = self.artista.obtenerListaAlbumes()
        
        longitud = lista_albums.obtenerLongitud()
        contador = 1
        while contador <= longitud: 
            album = lista_albums.obtenerPorIndice(contador)
            if album != None:
                self.agregar_nuevo(album)
            contador += 1