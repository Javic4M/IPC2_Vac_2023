import tkinter as tk

from PIL import Image, ImageTk

from app.biblioteca.Album import Album

class FrameAlbum(tk.Frame):
    
    def __init__(self, master, album, reproductor, biblioteca, *args, **kwargs):
        
        """
            params: 
                master: objeto ventana principal
                album: objeto album con la lista de canciones a mostrar
        """
        
        super().__init__(master, *args, **kwargs, bg = "black")
        
        self.master = master
        self.album = album
        self.reproductor = reproductor
        self.biblioteca = biblioteca
        
        # Titulo del album --------------------------------
        self.frame_titulo = tk.Frame(bg = "black")
        # Crear imagen del album
        self.portada = self.obtener_imagen_album()
        self.label_portada = tk.Label(self, image = self.portada)
        self.label_portada.grid(row = 1, column = 0, padx = 10, pady = 20)
        
        # Crear label con el nombre del album
        self.nombre_album = tk.StringVar()
        self.obtener_nombre_album()
        self.label_nombre_album = tk.Label(self, textvariable=self.nombre_album, font = ("Arial", 35, "bold"), bg = "black", fg="white")
        self.label_nombre_album.grid(row = 1, column = 1, padx=10, pady = 30)
        
        #Crear boton para reproducir el album
        self.imagen_play = self.obtener_imagen_play()
        self.boton_reproducir = tk.Button(self, image = self.imagen_play, command = self.reproducir, bg = "black", relief="flat", bd = 0, highlightthickness=0)
        self.boton_reproducir.grid(row = 1, column = 2, padx=15, pady=30, sticky="e")
        
    def mostrar_frame(self):
        self.master.cambiar_vista(self)
        
    def obtener_imagen_album(self):
        canciones = self.album.obtenerListaCanciones()
        cancion = canciones.obtenerPorIndice(1)
        ruta = cancion.obtenerImagen()
        if ruta == None or ruta == "":
            ruta = "./app/assets/comodin.jpg"
        
        imagen = None
        try:
            imagen = Image.open(ruta)
            imagen = imagen.resize((80,80))
            imagen = ImageTk.PhotoImage(imagen)
            return imagen
        except Exception as e:
            ruta = "./app/assets/comodin.jpg"
            imagen = Image.open(ruta)
            imagen = imagen.resize((80,80))
            imagen = ImageTk.PhotoImage(imagen)
            return imagen

    def obtener_nombre_album(self):
            
        nombre = self.album.obtenerNombre()
        if nombre == None or nombre == "":
            nombre = "Album desconocido"
        self.nombre_album.set(nombre)
        
    def obtener_imagen_play(self):
        ruta = "./app/assets/Play_icon.png"
        imagen = Image.open(ruta)
        imagen = ImageTk.PhotoImage(imagen)
        return imagen

    def reproducir(self):
        lista_canciones = self.album.obtenerListaCanciones()
        self.reproductor.establecerListaAReproducir(lista_canciones)
        self.reproductor.reproducir()
        self.master.actualizar_informacion_reproductor()
        
    def agregar_canciones(self):
        