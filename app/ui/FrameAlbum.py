import tkinter as tk

from app.biblioteca.Album import Album

class FrameAlbum(tk.Frame):
    
    def __init__(self, master, album, *args, **kwargs):
        
        """
            params: 
                master: objeto ventana principal
                album: objeto album con la lista de canciones a mostrar
        """
        
        super().__init__(master, *args, **kwargs, bg = "black")
        
        self.master = master
        self.album = album
        
    def mostrar_frame(self):
        self.master.cambiar_vista(self)