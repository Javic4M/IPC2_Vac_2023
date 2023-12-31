import tkinter as tk

from tkinter import simpledialog
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
        self.frame_titulo = tk.Frame(self, bg="black")
        self.frame_titulo.grid(row=0, column=0, sticky="ew")
        self.frame_titulo.grid_propagate(False)  # Evitar que el marco se ajuste al tamaño de su contenido
        self.frame_titulo.config(width=900, height=100)

        # Crear imagen del álbum
        self.portada = self.obtener_imagen_album()
        self.label_portada = tk.Label(self.frame_titulo, image=self.portada, bg="black")
        self.label_portada.grid(row=0, column=0, padx=10, pady=5)

        # Crear label con el nombre del álbum
        self.nombre_album = tk.StringVar()
        self.obtener_nombre_album()
        self.label_nombre_album = tk.Label(self.frame_titulo, textvariable=self.nombre_album, font=("Arial", 35, "bold"), bg="black", fg="white")
        self.label_nombre_album.grid(row=0, column=1, padx=10, pady=5)

        # Crear botón para reproducir el álbum
        self.imagen_play = self.obtener_imagen_play()
        self.boton_reproducir = tk.Button(self.frame_titulo, image=self.imagen_play, command=self.reproducir, bg="black", relief="flat", bd=0, highlightthickness=0)
        self.boton_reproducir.grid(row=0, column=2, padx=15, pady=5, sticky="e")

        # Lista de canciones ----------------------------------------------------------------
        # Crear un canvas scrollable para la lista de canciones
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)  # Configurar el peso de la fila para que se expanda
        self.grid_columnconfigure(0, weight=1)  # Configurar el peso de la columna para que se expanda
        
        # Agregar un scrollbar para el canvas
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Crear un frame para contener la lista de canciones dentro del canvas
        self.frame_canciones = tk.Frame(self.canvas, bg="black")
        self.canvas.create_window((0, 0), window=self.frame_canciones, anchor="nw")
        
        # Configurar el canvas para que se expanda con el frame de canciones
        self.frame_canciones.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        # Permitir desplazamiento con la rueda del mouse
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        
        self.agregar_canciones()


        
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
        lista_canciones = self.album.obtenerListaCanciones()
        longitud = lista_canciones.obtenerLongitud()
        contador = 1
        while contador <= longitud:
            cancion = lista_canciones.obtenerPorIndice(contador)
            if cancion != None: 
                nombre = cancion.obtenerNombre()
                if nombre == None or nombre == "":
                    nombre = "Cancion desconocida"
                    print (nombre)
                print(nombre)
                
                imagen = tk.PhotoImage(file="./app/assets/Mas.png")
                    
                boton = tk.Button(self.frame_canciones, text=nombre + "         ", font = ("Arial", 20), bg = "black", fg = "white", border= 0, highlightthickness= 0, relief = "flat", bd = 0, command = lambda cancion = cancion: self.agregar_a_lista(cancion), image = imagen, compound="right", width=800, height=60)
                boton.pack(side = "top", padx = 10, pady = 10, fill = "x", expand=True)
                print("boton de cacion: " + nombre + " agregado correctamente")
                boton.image = imagen
                            
            contador += 1
    
    
    def agregar_a_lista(self, cancion):
        lista = simpledialog.askstring("Lista de reproduccion", "Por favor, ingrese la lista a la que añadir "+ cancion.obtenerNombre())
        if isinstance(lista, str):
            if lista != None or lista != "":
                self.biblioteca.agregarCancionAListaReproduccion( cancion, lista)