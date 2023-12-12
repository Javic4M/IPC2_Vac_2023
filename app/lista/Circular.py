#Lista Circular Doblemente Enlazada
from app.lista.Nodo import Nodo


class ListaCircular:
    
    _inicio : 'Nodo'
    _ultimo: 'Nodo'
    _longitud : 'int'
    
    def __init__(self): 
        self._inicio =  None
        self._ultimo =  None 
        self._longitud = 0  
        
        self._actual = self._inicio #Nodo para agilizar avanzar y retroceder en la lista -> Mantiene el estado de la lista
        self._posicion_actual = 0   #Contador de posicion actual 
    
    def agregarALaLista(self, dato):

        if self.estaVacia():
            self._inicio = Nodo(dato)
            self._ultimo = self._inicio
            self._longitud += 1
            self._inicio.guardarSiguiente(self._inicio)
            
            self._posicion_actual = 1 #Contador de posicion actual
            self._actual = self._inicio
            
        else:
            
            #Buscar si el elemento ya se encuentra o no en la lista
            if self.buscarElemento(dato): 
                print("No se puede agrear el elemento pues ya está contenido en la lista")
            else: 
                actual = self._ultimo
                self._ultimo = Nodo(dato)
                actual.guardarSiguiente(self._ultimo)
                self._ultimo.guardarAnterior(actual)
                self._inicio.guardarAnterior(self._ultimo)
                self._ultimo.guardarSiguiente(self._inicio)
                self._longitud += 1
                
    def buscarElemento(self, dato):
        actual = self._inicio
        
        for i in range(self._longitud):
            if actual.obtenerDato() == dato:
                return True
            actual = actual.obtenerSiguiente()
        return False  
    
    def eliminar(self, indice: int):
        
        if (self.estaVacia()):
            print("\nLa Lista esta Vacia\n")
        else:
            if (indice >= 1 and indice <= self._longitud):
                actual = self._inicio

                if (self._longitud == 1):
                    self._inicio = self._ultimo = None
                    
                elif (self._longitud != 1 and indice == 1):
                    self._inicio = self._inicio.obtenerSiguiente()
                    self._inicio.guardarAnterior(self._ultimo)
                    self._ultimo.guardarSiguiente(self._inicio)   
                   
                elif (indice == self._longitud):
                    self._ultimo = self._ultimo.obtenerAnterior()
                    self._inicio.guardarAnterior(self._ultimo)
                    self._ultimo.guardarSiguiente(self._inicio)   
                     
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
        if self._longitud == 0:
            return None
        elif self._longitud == 1:
            return self._inicio
        else: 
            contador = self._longitud
            actual = self._ultimo
            while contador > indice: #cambiar self.longitud por indice
                contador -= 1
                actual = actual.obtenerAnterior()   
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
                return contenido.obtenerDato()
            else:
                print("\nIndice fuera de Rango\n")
    
    def estaVacia(self):
        return self._longitud == 0
    
    def obtenerLongitud(self):
        return self._longitud
    
    
    
    #Codigo para agilizar la busqueda ascendete - descendente (mantiene el estado de la lista)
    #Retorna el contenido de la posicion actual (Contenido, no nodo)
    def obtenerContenidoActual(self):
        
        if self.estaVacia():
            print("No hay elementos en la lista")
        else: 
            return self._actual.obtenerDato()
    
    
    def avanzar(self):
        if not self.estaVacia():
            pivote = self._actual.obtenerSiguiente()
            if pivote != None:
                self._actual = pivote
                self._posicion_actual +=1
                if self._posicion_actual > self._longitud:
                    #Regreso al inicio (giro por la derecha)
                    self._posicion_actual = 1
        
        
    def retroceder(self):
        if not self.estaVacia():
            pivote = self._actual.obtenerAnterior()
            if pivote != None:
                self._actual = pivote
                self._posicion_actual -=1
                if self._posicion_actual == 0:
                    #Regreso al final (giro por la izquierda)
                    self._posicion_actual = self._longitud    
    
    def obtenerIndicePosicionActual(self):
        return self._posicion_actual