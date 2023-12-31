import tkinter as tk

from app.biblioteca.Biblioteca import Biblioteca
from app.reproductor.Reproductor import Reproductor

from app.ui.FrameIzquierdo import FrameIzquierdo
from app.ui.FrameArtistas import FrameArtistas
from app.ui.FrameAlbumes import FrameAlbumes
from app.ui.FramePlaylists import FramePlaylists

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
        self.configure(bg="black")
        self.geometry("900x600")
        
        #lanzara un mensaje en dado caso no se muestre el icono en sistemas linux.
        try:
            self.iconbitmap("./app/assets/ipc2.ico")
        except:
            print("No es posible cargar los iconos")
            
        # Atributos de la ventana ----------------------------------------------------------------
                
        # Backend
        self.biblioteca = biblioteca
        self.reproductor = reproductor
        
        # Frames frontend
        self.frame_izquierdo = FrameIzquierdo(self, biblioteca, reproductor)
        #self.frame_izquierdo.grid(row = 0, column = 0, sticky = "ns")
        self.frame_izquierdo.pack(side =  "left", padx=20, pady = 25)
        
        lista_artistas = self.biblioteca.obtenerListaArtistas()
        self.frame_artistas = FrameArtistas(self, lista_artistas, reproductor, biblioteca)
        self.frame_artistas.pack(side = "right", fill="both", expand = True, padx=1)
        
        
        self.frame_albumes = FrameAlbumes(self, reproductor, biblioteca)
        
        self.frame_playlists = FramePlaylists(self, reproductor, biblioteca)
        
        self.vista_actual = None #Vista actual es el frame actual cargado en la parte derecha del reproductor
        self.vista_actual = self.frame_artistas
        
        
        
    def cambiar_vista(self, vista_nueva):
        self.vista_actual.pack_forget()
        self.vista_actual = vista_nueva
        self.vista_actual.pack(side = "right", fill="both", expand = True, padx=1)
    
    def mostrar_artistas(self):
        self.cambiar_vista(self.frame_artistas)
    
    def mostrar_albumes(self):
        self.frame_albumes.mostrar_frame()
    
    def mostrar_playlists(self):
        self.refresh_playlists_frame()
        self.frame_playlists.mostrar_frame()
    
    def actualizar_informacion_reproductor(self):
        self.frame_izquierdo.actualizarInformacion()
        
    def refresh_playlists_frame(self):
        self.frame_playlists.destroy()
        self.frame_playlists = FramePlaylists(self, self.reproductor, self.biblioteca)
