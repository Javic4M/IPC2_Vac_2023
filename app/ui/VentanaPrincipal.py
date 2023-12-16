import tkinter as tk

from app.biblioteca.Biblioteca import Biblioteca
from app.reproductor.Reproductor import Reproductor

from app.ui.FrameIzquierdo import FrameIzquierdo

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
        self.frame_izquierdo.pack(side =  "left", fill="y", expand = True)
        
        