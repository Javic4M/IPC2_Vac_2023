#Clase que almacena datos de manera persistente sobre la cantidad de reproducciones de las canciones
#Realiza la persistencia a traves de Json
import json

class Historial: 
    def __init__(self):
        self._ruta = "./contador.json"
        
        try:
            archivo = open(self._ruta, 'x')
            archivo.write("{\n}")
            archivo.close()
            print("Archivo creado exitosamente.")
        except FileExistsError:
            print("El archivo ya existe.")
    
    def actualizarContador(self, nombre_cancion):
        
        contador_cancion = 0
        
        with open(self._ruta) as file: 
            contador_json = json.loads(file.read())
        
        #Actualizar el valor de la cancion
        try:
            #Obtener el valor del contador de la cancion
            contador_cancion = contador_json[nombre_cancion]
            contador_cancion = int(contador_cancion)
            
        except KeyError:
            print("La clave no existe en el JSON.")
        
        #Actualizar el valor del contador de la cancion (se crea si no existe)
        contador_cancion += 1
        contador_json[nombre_cancion] = contador_cancion
        #Guardar el Json actualizado
        with open(self._ruta, 'w') as file:
            json.dump(contador_json, file)
        