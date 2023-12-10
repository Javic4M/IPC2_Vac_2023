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
        
    def agregarALaLista(self, dato):

        if self.estaVacia():
            self._inicio = Nodo(dato)
            self._ultimo = self._inicio
            self._longitud += 1
        else:
            
            #Buscar si el elemento ya se encuentra o no en la lista
            if self.buscarElemento(dato): 
                print("No se puede arear el elemento pues ya está contenido en la lista")
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
                return contenido.obtenerDato()
            else:
                print("\nIndice fuera de Rango\n")
    
    def estaVacia(self):
        return self._longitud == 0
    