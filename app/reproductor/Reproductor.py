#REQUIERE LA INSTALACION DE PYGAME: pip install pygame
import pygame

def reproducir_audio(ruta_archivo):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_archivo)
    pygame.mixer.music.play()

    opcion = None
    while(opcion != "s"):
        opcion = input("Presiona enter para pausar... s para salir\n")
        pygame.mixer.music.pause()
        
        if(opcion == "s"):
            break
        
        opcion = input("Presiona enter para reanudar... s para salir")
        pygame.mixer.music.unpause()

ruta_archivo = "C:/Users/Jorge/OneDrive/Escritorio/Joji  Normal People ft rei brown.mp3"
reproducir_audio(ruta_archivo)