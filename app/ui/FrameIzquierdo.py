import tkinter as tk
from PIL import Image, ImageTk

from app.reproductor.Reproductor import Reproductor
from app.biblioteca.Biblioteca import Biblioteca
from app.biblioteca.Cancion import Cancion

from app.reporte.Reporte import Reporte

class FrameIzquierdo(tk.Frame):
    """
    Clase perteneciente al panel (frame) izquierdo de la aplizacion
    En ella se contiene la vista del reproductor y el menu para navegar entre canciones
    
    Attributes:

    Methods:
    
    """
    
    def __init__(self, master, biblioteca, reproductor):
        """
        Constructor de la clase 
        
        Args:
            master: widget padre al que estará asociado
            biblioteca: obteto biblioteca ya inicializado 
            reproductor: obteto reproductor ya inicializado
        Rerurns: 
            None
        Ejemplo: 
        """
        
        self.biblioteca = biblioteca
        self.reproductor = reproductor
        self.directorio_assets = "./app/assets/"
        
        super().__init__(master, bg = "black")
        self.master = master # widget padre
        self.pack(fill = "y")
        
        # FRAME INTERCAMBIO VISTAS
        # Crear el frame
        self.frame_menu = tk.Frame(self, bg = "black")
        
        # Crear botones de navegacion
        
        #Espaciadores
        self.btn_espaciador1 = tk.Button(self.frame_menu, bg = "black", text = " ", relief= "flat")
        self.btn_espaciador1.grid(row = 2, column= 0, sticky="ns")
        self.btn_espaciador2 = tk.Button(self.frame_menu, bg = "black", text = " ", relief= "flat")
        self.btn_espaciador2.grid(row = 6, column= 0, sticky="ns")
        
        self.image_top = self.directorio_assets + "Top.png"
        self.img_top = Image.open(self.image_top)
        self.photo_top = ImageTk.PhotoImage(self.img_top)
        self.btn_top_10 = tk.Button(self.frame_menu, image = self.photo_top, bg = 'black', fg = "white", font = ("Arial" , 15), relief="flat", command = self.abrir_top_10, bd = 0, highlightthickness=0)
        self.btn_top_10.grid(row = 1, column=0, padx= 15, pady=10, sticky="ew") 
        
        self.image_artistas = self.directorio_assets + "Artistas.png"
        self.img_artistas = Image.open(self.image_artistas)
        self.photo_artistas = ImageTk.PhotoImage(self.img_artistas)
        self.btn_artistas = tk.Button(self.frame_menu,image = self.photo_artistas, bg="black", fg = "white", font = ("Arial" , 15), relief="flat", command = self.navegar_a_artistas, bd=0, highlightthickness=0)
        self.btn_artistas.grid(row = 3, column=0, padx= 15, pady=10)
        
        self.image_albumes = self.directorio_assets + "Albums.png"
        self.img_albumes = Image.open(self.image_albumes)
        self.photo_albumes = ImageTk.PhotoImage(self.img_albumes) 
        self.btn_albumes = tk.Button(self.frame_menu, image = self.photo_albumes, bg="black", fg = "white", font = ("Arial" , 15), relief="flat", command = self.navegar_a_albumes, bd=0, highlightthick = 0)
        self.btn_albumes.grid(row = 4, column=0, padx= 15, pady=10)
        
        self.image_listas_reproduccion = self.directorio_assets + "Playlists.png"
        self.img_listas_reproduccion = Image.open(self.image_listas_reproduccion)
        self.photo_listas_reproduccion = ImageTk.PhotoImage(self.img_listas_reproduccion)
        self.btn_listas_reproduccion = tk.Button(self.frame_menu, image = self.photo_listas_reproduccion, bg="black", fg = "white", font = ("Arial" , 15), relief="flat", command = self.navegar_a_listas_de_reproduccion, bd=0, highlightthickness=0)
        self.btn_listas_reproduccion.grid(row = 5, column=0, padx= 15, pady=10)
        
        
        
        self.frame_menu.pack()
        
        
        # FRAME REPRODUCTOR DE MUSICA 
        # Agregar los botones
        self.frame_reproductor = tk.Frame(self, bg="black")
        
        self.image_retroceder = self.directorio_assets + "Anterior.png"
        self.img_retroceder = Image.open(self.image_retroceder)
        self.photo_retroceder = ImageTk.PhotoImage(self.img_retroceder)
        self.btn_retroceder = tk.Button(self.frame_reproductor, image = self.photo_retroceder, command=self.retroceder, bg='black', fg='black', font=('Arial', 8), width=20, height=20, relief="flat",  bd=0, highlightthickness=0 )
        self.btn_retroceder.grid(row=0, column=0, padx=5, pady=5)

        self.image_reproducir = self.directorio_assets + "Play.png"
        self.img_reproducir = Image.open(self.image_reproducir)
        self.photo_reproducir = ImageTk.PhotoImage(self.img_reproducir)
        self.btn_reproducir = tk.Button(self.frame_reproductor, image = self.photo_reproducir, command=self.reproducir, bg='black', fg='black', font=('Arial', 8), width=20, height=20, relief="flat",  bd=0, highlightthickness=0)
        self.btn_reproducir.grid(row=0, column=1, padx=5, pady=5)

        self.image_pausar = self.directorio_assets + "Pausa.png"
        self.img_pausar = Image.open(self.image_pausar)
        self.photo_pausar = ImageTk.PhotoImage(self.img_pausar)
        self.btn_pausar = tk.Button(self.frame_reproductor, image = self.photo_pausar, command=self.pausar, bg='black', fg='black', font=('Arial', 8), width=20, height=20, relief="flat",  bd=0, highlightthickness=0)
        self.btn_pausar.grid(row=0, column=2, padx=5, pady=5)

        self.image_avanzar = self.directorio_assets + "Siguiente.png"
        self.img_avanzar = Image.open(self.image_avanzar)
        self.photo_avanzar = ImageTk.PhotoImage(self.img_avanzar)
        self.btn_avanzar = tk.Button(self.frame_reproductor, image = self.photo_avanzar, command=self.avanzar, bg='black', fg='black', font=('Arial', 8), width=20, height=20, relief="flat",  bd=0, highlightthickness=0)
        self.btn_avanzar.grid(row=0, column=3, padx=5, pady=5)

        self.image_aleatorio = self.directorio_assets + "Aleatorio.png"
        self.img_aleatorio = Image.open(self.image_aleatorio)
        self.photo_aleatorio = ImageTk.PhotoImage(self.img_aleatorio)
        self.btn_aleatorio = tk.Button(self.frame_reproductor,  image = self.photo_aleatorio, command=self.aleatorio, bg='black', fg='black', font=('Arial', 8), width=20, height=20, relief="flat",  bd=0, highlightthickness=0)
        self.btn_aleatorio.grid(row=0, column=4, padx=5, pady=5)

        self.image_path = self.directorio_assets + "comodin.jpg"
        self.imagen = Image.open(self.image_path)
        self.imagen = self.imagen.resize((150, 150))  # Ajustar el tamaño de la imagen
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(self.frame_reproductor, image=self.imagen)
        self.label_imagen.grid(row=1, column=0, columnspan=5, padx=10, pady=5)

        # Variables informacion cancion 
        self.nombre_cancion = tk.StringVar()
        self.nombre_artista = tk.StringVar()
        self.nombre_album = tk.StringVar()
        self.nombre_aleatorio = tk.StringVar()
        
        self.nombre_cancion.set("Cancion")
        self.nombre_artista.set("Artista")
        self.nombre_album.set("Album")
        self.nombre_aleatorio.set("No aleatorio")
        self.cancion_actual = None
        self.actualizarInformacion()
        
        self.label_cancion = tk.Label(self.frame_reproductor, textvariable=self.nombre_cancion, font=('Arial', 14), bg='black', fg='white')
        self.label_cancion.grid(row=2, column=0, columnspan=5, padx=10, pady=2)

        self.label_artista = tk.Label(self.frame_reproductor, textvariable=self.nombre_artista, font=('Arial', 12), bg='black', fg='white')
        self.label_artista.grid(row=3, column=0, columnspan=5, padx=10, pady=2)

        self.label_album = tk.Label(self.frame_reproductor, textvariable=self.nombre_album, font=('Arial', 10), bg='black', fg='white')
        self.label_album.grid(row=4, column=0, columnspan=5, padx=10, pady=2)
        
        self.label_aleatorio = tk.Label(self.frame_reproductor, textvariable=self.nombre_aleatorio, font=('Arial', 6), bg='black', fg='white')
        self.label_aleatorio.grid(row=5, column=0, columnspan=5, padx=10, pady=2)


        self.frame_reproductor.pack(side = "bottom")
        self.reporte = Reporte("./contador.xml")
    
    
    # METODOS    
    # 1. Navegacion   
    def abrir_top_10(self):
        print("Abro el navegador para ver el top 10 de canciones mas reproducidas")
        self.reporte.get_reporte()
    
    def navegar_a_artistas(self):
        print("Estoy navegando a artistas!")
        self.master.mostrar_artistas()
        
    def navegar_a_albumes(self):  
        print("Estoy navegando a albumes!")
        self.master.mostrar_albumes()
    
    def navegar_a_listas_de_reproduccion(self):
        print("Estoy navegando a listas de reproduccion!")
        self.master.mostrar_playlists()
        
        
        
    # 2. Reproductor
    def retroceder(self):
        print("Soy retroceder y estoy retrocediendo!")
        
        self.reproductor.retroceder()
        self.actualizarInformacion()

    def reproducir(self):
        print("Soy reproducir y estoy reproduciendo!")
        self.reproductor.reanudar()
        self.actualizarInformacion()

    def pausar(self):
        print("Soy pausar y estoy pausando!")
        self.reproductor.pausar()
        self.actualizarInformacion()

    def avanzar(self):
        print("Soy avanzar y estoy avanzando!")
        self.reproductor.avanzar()
        self.actualizarInformacion()

    def aleatorio(self):
        print("Soy aleatorio y estoy reproduciendo aleatoriamente!")
        aleatorio = self.reproductor.esAleatorio()
        if aleatorio:
            self.reproductor.reproduccionNoAleatoria()
        else:
            self.reproductor.reproduccionAleatoria()
        self.actualizarInformacion()
        
    def actualizarInformacion(self):
        self.cancion_actual = self.reproductor.obtenerCancionActual()
        if self.cancion_actual != None:
            
            nombre_cancion = self.cancion_actual.obtenerNombre()
            if nombre_cancion != None or nombre_cancion != "":
                self.nombre_cancion.set(nombre_cancion)
            else:
                self.nombre_cancion .set("Nombre desconocido")
                
            nombre_artista = self.cancion_actual.obtenerArtista()
            if nombre_artista != None or nombre_artista != "":
                self.nombre_artista.set(nombre_artista)
            else:
                self.nombre_artista .set("Artista desconocido")
            
            nombre_album = self.cancion_actual.obtenerAlbum()
            if nombre_album != None or nombre_album != "":
                self.nombre_album.set(nombre_album)
            else: 
                self.nombre_album.set("Album desconocido")         

            #Actalizar portada del album
            path = self.cancion_actual.obtenerImagen()
            if path != None or path != "":
                self.image_path = path
            else:
                self.image_path = self.directorio_assets + "comodin.jpg"
            
            try:
                self.imagen = Image.open(self.image_path)
                self.imagen = self.imagen.resize((150,150))
                self.imagen = ImageTk.PhotoImage(self.imagen)
                self.label_imagen.config(image = self.imagen)
                self.label_imagen.image = self.imagen
            except FileNotFoundError as e:
                self.image_path = self.directorio_assets + "comodin.jpg"
            
                self.imagen = Image.open(self.image_path)
                self.imagen = self.imagen.resize((150,150))
                self.imagen = ImageTk.PhotoImage(self.imagen)
                self.label_imagen.config(image = self.imagen)
                self.label_imagen.image = self.imagen
            
            if self.reproductor.esAleatorio():
                self.nombre_aleatorio.set("Aleatorio")
            else: 
                self.nombre_aleatorio.set("No aleatorio")
            
    # 2. Intercambio de vista lateral derecha
    
    
    
   