import tkinter as tk

from PIL import Image, ImageTk

from app.lista.Lista import Lista
from app.ui.FramePlaylist import FramePlaylist


class FramePlaylists(tk.Frame):
    
    def __init__(self, master, reproductor, biblioteca, *args, **kwargs):
        """
            params: 
                master: ventana principal
                artista: objeto artista con los albumes a mostrar
        """
        super().__init__(master, *args, **kwargs, bg = "black")
        
        self.master = master
        self.reproductor = reproductor
        self.biblioteca = biblioteca
        self.lista_playlists = biblioteca.obtenerListasReproduccion()
        self.lista_frames_playlist = Lista()
        
        
        
        # Crear el label en la parte superior con el nombre del Frame
        label_titulo = tk.Label(self, text="Playlists", font=("Arial", 35, "bold"), bg="black", fg="white")
        label_titulo.grid(row=0, column=0, sticky="w", pady = 20, padx=15) 


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
        
        self.agregar_playlists()


    def mostrar_frame(self):
        self.master.cambiar_vista(self)
        
    def agregar_nuevo(self, playlist):
        
        # Añadir una instancia de un botón al contenedor de botones con la imagen de la playlist ----------------------------------------------------------------
        # Obtener la imagen de la playlist

        ruta = "./app/assets/Playlist_icon.png"
        imagen = Image.open(ruta)
        imagen = imagen.resize((80,80))
        imagen = ImageTk.PhotoImage(imagen)
            
            
            
        nombre = playlist.obtenerNombre()
        if nombre == None or nombre == "":
            nombre = "Playlist Desconocida"


        frame_playlist = FramePlaylist(self.master, playlist, self.reproductor, self.biblioteca)
        nuevo_boton = tk.Button(self.contenedor_botones, image=imagen, compound="top", bg="#181818", fg="white", font=("Arial", 15, "bold"), highlightthickness=0, relief="flat", text=nombre, command=frame_playlist.mostrar_frame, width=140, height=140)
        #Mantener la referencia en la lista
        self.lista_frames_playlist.agregarALaLista(frame_playlist)
                
        # Mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        nuevo_boton.image = imagen

        if(self.contador_columnas == 6):
            self.contador_columnas = 0
            self.contador_filas += 1
        
        nuevo_boton.grid(row=self.contador_filas, column=self.contador_columnas, sticky="ew", pady = 20, padx= 20)
        self.contador_columnas += 1

    
    def agregar_playlists(self):
        lista_playlists = self.lista_playlists
        
        longitud = lista_playlists.obtenerLongitud()
        contador = 1
        while contador <= longitud: 
            playlist = lista_playlists.obtenerPorIndice(contador)
            if playlist != None:
                self.agregar_nuevo(playlist)
            contador += 1