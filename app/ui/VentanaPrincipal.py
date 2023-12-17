import tkinter as tk

from app.biblioteca.Biblioteca import Biblioteca
from app.reproductor.Reproductor import Reproductor

from app.ui.FrameIzquierdo import FrameIzquierdo
from app.ui.FrameArtistas import FrameArtistas

class VentanaPrincipal(tk.Tk):
    

    
    def __init__(self, biblioteca, reproductor): 
        """
        Attributes:
            biblioteca: Objeto biblioteca ya inicializado
            reproductor: Objeto reproductor ya inicializado
        """
        # Configuracion de la ventana
        super().__init__()
        self.title("IPC2 Music")
        self.iconbitmap("./app/assets/ipc2.ico")
        self.configure(bg="black")
        self.geometry("900x600")
        
        # Atributos de la ventana ----------------------------------------------------------------
                
        # Backend
        self.biblioteca = biblioteca
        self.reproductor = reproductor
        
        # Frames frontend
        self.frame_izquierdo = FrameIzquierdo(self, biblioteca, reproductor)
        #self.frame_izquierdo.grid(row = 0, column = 0, sticky = "ns")
        self.frame_izquierdo.pack(side =  "left", padx=20, pady = 25)
        
        lista_artistas = self.biblioteca.obtenerListaArtistas()
        self.frame_artistas = FrameArtistas(self, lista_artistas)
        self.frame_artistas.pack(side = "right", fill="both", expand = True, padx=1)
        
        self.vista_actual = None #Vista actual es el frame actual cargado en la parte derecha del reproductor
        self.vista_actual = self.frame_artistas
        
        
        
    def cambiar_vista(self, vista_nueva):
        self.vista_actual.pack_forget()
        self.vista_actual = vista_nueva
        self.vista_actual.pack(side = "right", fill="both", expand = True, padx=1)
    
    def mostrar_artistas(self):
        self.cambiar_vista(self.frame_artistas)