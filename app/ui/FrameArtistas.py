import tkinter as tk

from app.biblioteca.Artista import Artista
from app.lista.Lista import Lista

from app.ui.FrameArtista import FrameArtista

class FrameArtistas(tk.Frame):
    
    
    def __init__(self, master, lista_artistas, reproductor, biblioteca,*args, **kwargs):
        
        """
            params: 
                master: ventana principal
                lista_artistas: lista enlazada con los artistas disponibles
             
        """
        super().__init__(master, *args, **kwargs, bg="black")


        self.lista_artistas = lista_artistas
        self.master = master
        self.reproductor = reproductor
        self.biblioteca = biblioteca
        
        # Crear el label en la parte superior
        label_artistas = tk.Label(self, text="Artistas", font=("Arial", 35, "bold"), bg="black", fg="white")
        label_artistas.grid(row=0, column=0, sticky="w", pady = 20, padx=15)

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

        # Crear el botón "Agregar Nuevo" en el contenedor de botones
        #btn_agregar_nuevo = tk.Button(self.contenedor_botones, text="Agregar Nuevo", command=self.agregar_nuevo, font=("Arial", 12))
        #btn_agregar_nuevo.grid(row=0, column=0, sticky="ew")
        
        # Lista enlazada para manetener referencias de los frames artista
        self.lista_frames_artista = Lista()

        self.contador_columnas = 0
        self.contador_filas = 0
        
        self.agregar_artistas()

    def agregar_nuevo(self, artista):
        
        # Añadir una instancia de un botón al contenedor de botones
        imagen = tk.PhotoImage(file="./app/assets/Artista_icon.png")
        #imagen = imagen.subsample(3, 3)  # Redimensionar la imagen (ajusta los valores según sea necesario)
        
        nombre = artista.obtenerNombre()
        if nombre == None or nombre == "":
            nombre = "Artista desconocido"


        frame_artista = FrameArtista(self.master, artista, self.reproductor, self.biblioteca)
        nuevo_boton = tk.Button(self.contenedor_botones, image=imagen, compound="top", bg="#181818", fg="white", font=("Arial", 15, "bold"), highlightthickness=0, relief="flat", text=nombre, command=frame_artista.mostrar_frame, width=140, height=140)
        #Mantener la referencia en la lista
        self.lista_frames_artista.agregarALaLista(frame_artista)
                
        # Mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        nuevo_boton.image = imagen

        if(self.contador_columnas == 6):
            self.contador_columnas = 0
            self.contador_filas += 1
        
        nuevo_boton.grid(row=self.contador_filas, column=self.contador_columnas, sticky="ew", pady = 20, padx= 20)

        self.contador_columnas += 1

    def agregar_artistas(self):
        longitud = self.lista_artistas.obtenerLongitud()
        contador = 1
        while contador <= longitud:
            artista = self.lista_artistas.obtenerPorIndice(contador)
            if artista != None:
                self.agregar_nuevo(artista)
                
            contador += 1
            
    def cambiar_frame_derecho(self):
        print ("in cambiar frame derecho desde artistas")