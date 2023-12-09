from contextlib import nullcontext
from dataclasses import dataclass


@dataclass
class Cancion:
    nombre = ""
    ruta = ""
    imagen = ""
    numero: int
    
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
        actual = self._inicio

        if (self._longitud == 1 and indice == 1):
            self._inicio = self._ultimo = nullcontext
            
        elif (self._longitud != 1 and indice == 1):
            print("Opción 2")
            self._inicio = self._inicio._nodoSiguiente
            self._inicio.guardarAnterior(nullcontext)
            
        elif (indice == self._longitud):
            print("Opción 3")
            self._ultimo = self._ultimo.obtenerAnterior()
            self._ultimo.guardarSiguiente(nullcontext)
            
        else:
            print("Opción 4")
            aEliminar: 'Nodo'
            rango = self._longitud / 2
                
            if (indice >= rango):
                indice_1 = self._longitud - indice
                print("NUmero: " + str(indice_1))
                aEliminar = self.encontrarPorIndiceFinalInicio(indice_1)
            else:
                aEliminar = self.encontrarPorIndiceInicioFinal(indice - 1)
                                
            print("N............" + aEliminar._cancion.nombre)
            anterior = aEliminar.obtenerAnterior()
            siguiente = aEliminar.obtenerSiguiente()
            anterior.guardarSiguiente(siguiente)
            siguiente.guardarAnterior(anterior)
            aEliminar.guardarSiguiente(nullcontext)
            aEliminar.guardarAnterior(nullcontext)         
        self._longitud -= 1    
        
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
        contenido: 'Nodo'
        
        rango = self._longitud / 2
        
        if (indice >= rango):
            indice_1 = self._longitud - indice
            contenido = self.encontrarPorIndiceFinalInicio(indice_1)
        else:
            contenido = self.encontrarPorIndiceInicioFinal(indice - 1)
                
        return contenido._cancion
        
class MenuPrincipal:
    
    lista = Lista()
    lista.agregarALaLista(Cancion("Navidad", "J", "C", 0))
    lista.agregarALaLista(Cancion("Año_Nuevo", "J", "C", 1))
    lista.agregarALaLista(Cancion("Felicidades", "J", "C", 2))
    opcion = int(input("Menu Principal \n    1. Agregar a la Lista \n    2. Listar \n    3. Listar Uno \n    4. Eliminar \n    5. Salir \n"))

    while opcion != 5:
            
        if (opcion == 1):
            lista.agregarALaLista(Cancion("Javier", "J", "C", 3))
        elif (opcion == 2):
            print("Longitud: " + str(lista._longitud))   
            for i in range(lista._longitud):
                contenido = lista.obtenerContenido(i + 1)
                print("Cancion: " + contenido.nombre)                  
        elif (opcion == 3):
            contenido = lista.obtenerContenido(int(input("Ingrese Indice_1: ")))
            print("- Cancion: " + contenido.nombre) 
        elif (opcion == 4):
            lista.eliminarDeLaLista(int(input("Ingrese Indice_2: ")))
            
        opcion = int(input("Menu Principal \n    1. Agregar a la Lista \n    2. Listar \n    3. Listar Uno \n    4. Eliminar \n    5. Salir \n"))
  