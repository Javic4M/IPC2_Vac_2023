from contextlib import nullcontext
from dataclasses import dataclass


@dataclass
class Cancion:
    
    def __init__(self, nombre, ruta, imagen, numero):
        self.nombre = nombre
        self.ruta = ruta
        self.imagen = imagen
        self.numero = numero
        
        
class Nodo:
    
    _cancion: 'Cancion'
    _nodoSiguiente: 'Nodo'
    _nodoAnterior: 'Nodo'
        
    def __init__(self, cancion):
        self._cancion = cancion
        self._nodoSiguiente = nullcontext    
    
    def guardarSiguiente(self, nodoSiguiente):
        self._nodoSiguiente = nodoSiguiente   
    
    def guardarAnterior(self, nodoAnterior):
        self._nodoAnterior = nodoAnterior   
    
    def obtenerSiguiente(self):
        return self._nodoSiguiente

    def obtenerAnterior(self):
        return self._nodoAnterior
    
    
class Lista:  
    _inicio: 'Nodo'
    _ultimo: 'Nodo'
    _longitud: int
    
    def __init__(self):
        self._inicio = Nodo
        self._ultimo = Nodo
        self._longitud = 0 
      
    def agregarALaLista(self, cancion):

        if self._longitud == 0:
            self._inicio = Nodo(cancion)
            self._ultimo = self._inicio
        else:
            nuevo = Nodo(cancion)
            self._ultimo.guardarSiguiente(nuevo)
            nuevo.guardarAnterior(self._ultimo)
            self._ultimo = nuevo
        self._longitud += 1
           
    def eliminarDeLaLista(self, indice: int):
        
        if (self.estaVacia()):
            print("\nLa Lista esta Vacia\n")
        else:
            if (indice >= 1 and indice <= self._longitud):
                actual = self._inicio

                if (self._longitud == 1 and indice == 1):
                    self._inicio = self._ultimo = nullcontext
                    
                elif (self._longitud != 1 and indice == 1):
                    self._inicio = self._inicio._nodoSiguiente
                    self._inicio.guardarAnterior(nullcontext)
                    
                elif (indice == self._longitud):
                    self._ultimo = self._ultimo.obtenerAnterior()
                    self._ultimo.guardarSiguiente(nullcontext)
                    
                else:
                    aEliminar: 'Nodo'
                    rango = self._longitud / 2
                        
                    if (indice >= rango):
                        indice_1 = self._longitud - indice
                        aEliminar = self.encontrarPorIndiceFinalInicio(indice_1)
                    else:
                        aEliminar = self.encontrarPorIndiceInicioFinal(indice - 1)
                                        
                    anterior = aEliminar.obtenerAnterior()
                    siguiente = aEliminar.obtenerSiguiente()
                    anterior.guardarSiguiente(siguiente)
                    siguiente.guardarAnterior(anterior)
                    aEliminar.guardarSiguiente(nullcontext)
                    aEliminar.guardarAnterior(nullcontext)         
                self._longitud -= 1    
            else:
                print("\nIndice Fuera de Rango\n")
            
    def encontrarPorIndiceInicioFinal(self, indice): 
        actual = self._inicio
        
        for i in range(indice):
            siguiente = actual.obtenerSiguiente()
            actual = siguiente     
        return actual
       
    def encontrarPorIndiceFinalInicio(self, indice): 
        actual = self._ultimo
        
        for i in range(indice):
            anterior = actual.obtenerAnterior()
            actual = anterior
        return actual
    
    def obtenerContenido(self, indice):
        
        if (self.estaVacia()):
            print("\nLa Lista esta Vacia\n")
        else:
            if (indice >= 1 and indice <= self._longitud):
                contenido: 'Nodo'       
                rango = self._longitud / 2
                
                if (indice >= rango):
                    indice_1 = self._longitud - indice
                    contenido = self.encontrarPorIndiceFinalInicio(indice_1)
                else:
                    contenido = self.encontrarPorIndiceInicioFinal(indice - 1)    
                return contenido._cancion
            else:
                print("\nIndice fuera de Rango\n")
    
    def estaVacia(self):
        return self._longitud == 0
        
        
class MenuPrincipal:
    
    lista = Lista()
    #lista.agregarALaLista(Cancion("Noche de Paz", "ruta_1", "noche.png", 1))
    #lista.agregarALaLista(Cancion("Feliz Navidad", "ruta_2", "felizNavidad.png", 2))
    lista.agregarALaLista(Cancion("Rodolfo el Reno", "ruta_3", "reno.png", 3))
    
    opcion = int(input("Menu Principal \n    1. Agregar a la Lista \n    2. Listar \n    3. Listar Uno \n    4. Eliminar \n    5. Salir \n"))

    while opcion != 5:
            
        if (opcion == 1):
            lista.agregarALaLista(Cancion(input("Ingrese el Nombre de la Canción: "), "ruta_" + str(lista._longitud + 1), "img.png", lista._longitud + 1))
            print("\n-----------------------------")
            print("Canción Ingresada Correctamente")
            print("-----------------------------\n") 
        elif (opcion == 2):
            print("\n-------------------------")
            for i in range(lista._longitud):
                contenido = lista.obtenerContenido(i + 1) 
                print("Canción: " + contenido.nombre)    
            print("-------------------------\n")                 
        elif (opcion == 3):
            try:
                contenido = lista.obtenerContenido(int(input("Ingrese el Número de la Canción que desea Reproducir: ")))
                if (contenido != None):
                    print("\n---------------------\nCanción \n  Nombre: " + contenido.nombre + "\n  Ruta: " + contenido.ruta + "\n  Numero: " + str(contenido.numero) + "\n---------------------\n")                             
            except ValueError:
                print("\n---------------------\nDebe Ingresar un Número\n---------------------\n") 
        elif (opcion == 4):
            try:
                lista.eliminarDeLaLista(int(input("Ingrese la Canción que desea Eliminar: ")))
            except ValueError:
                print("\n---------------------\nDebe Ingresar un Número\n---------------------\n") 
            
        opcion = int(input("Menu Principal \n    1. Agregar a la Lista \n    2. Listar \n    3. Listar Uno \n    4. Eliminar \n    5. Salir \n"))
  