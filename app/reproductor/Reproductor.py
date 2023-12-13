#REQUIERE LA INSTALACION DE PYGAME: pip install pygame
import pygame
import random 

from app.lista.Lista import Lista
from app.lista.Circular import ListaCircular

from app.biblioteca.Cancion import Cancion

from app.persistencia.Historial import Historial

class Reproductor: 
    
    def __init__(self):
        self._reproduccion_aleatoria = False
        self._lista_a_reproducir = Lista()
        self._cancion = None
        
        self._aleatorio = False
        self._pila = []
        
        self._cancion_actual = None
        
        self._historial = Historial()
        
        pygame.mixer.init()
        
    #Obtiene como parametro una lista de canciones para reproducir    
    def establecerListaAReproducir(self, lista_a_reproducir):
        self._lista_a_reproducir = lista_a_reproducir
    
    def reproducir(self):
        mensaje = ""
        if self._aleatorio == False: 
            self._cancion_actual = self._lista_a_reproducir.obtenerContenidoActual()
            mensaje = "en modo normal"
        else:
            if self._cancion_actual == None:
                self.avanzar()
            mensaje = "en modo aleatorio"
            
        ruta = self._cancion_actual.obtenerRuta()
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()
        
        nombre_cancion = self._cancion_actual.obtenerNombre()
        self._historial.actualizarContador(nombre_cancion)
        
        print("Reproduciendo: ", ruta, mensaje," \n")
    
    def obtenerCancionAleatoria(self):
        indice = random.randint(1, self._lista_a_reproducir.obtenerLongitud())
        cancion = self._lista_a_reproducir.obtenerPorIndice(indice)
        return cancion
        
    
    def retroceder(self):
        if self._aleatorio == False:
            self._lista_a_reproducir.retroceder()
        else: 
            if len(self._pila) == 0:
                self.avanzar()
            else:
                self._cancion_actual = self._pila.pop()
                print("Elementos actuales en la pila")
                for elemento in self._pila:
                    print(elemento.imprimirCancion())
                    
        self.reproducir()
    
    def avanzar(self):
        if self._aleatorio == False:
            self._lista_a_reproducir.avanzar()
        else: 
            cancion = self.obtenerCancionAleatoria()
            while self._cancion_actual == cancion:
                cancion = self.obtenerCancionAleatoria()
                 
            self._cancion_actual = cancion
            self._pila.append(self._cancion_actual)
        self.reproducir()
    
    def pausar(self):
        pygame.mixer.music.pause()   
    
    def reanudar(self):
        pygame.mixer.music.unpause()  
    
    def reproduccionAleatoria(self):
        self._aleatorio = True
        self._pila = []
        print("Modo de reproduccion configurado en Aleatorio!")
        self.reproducir()
        
    def reproduccionNoAleatoria(self):
        self._aleatorio = False
        print("Modo de reproduccion configurado en no Aleatorio!")
        self.reproducir()



#def reproducir_audio(ruta_archivo):
#    pygame.mixer.init()
#    pygame.mixer.music.load(ruta_archivo)
#    pygame.mixer.music.play()
#
#    opcion = None
#    while(opcion != "s"):
#        opcion = input("Presiona enter para pausar... s para salir\n")
#        pygame.mixer.music.pause()
#        
#        if(opcion == "s"):
#            break
#        
#        opcion = input("Presiona enter para reanudar... s para salir")
#        pygame.mixer.music.unpause()
#
#ruta_archivo = "C:/Users/Jorge/OneDrive/Escritorio/Joji  Normal People ft rei brown.mp3"
#reproducir_audio(ruta_archivo)