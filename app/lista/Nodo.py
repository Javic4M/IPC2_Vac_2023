class Nodo: 
    def __init__(self, dato):
        self._dato = dato
        self._nodoSiguiente = None
        self._nodoAnterior = None
        
    def obtenerDato(self):
        return self._dato
        
    def guardarSiguiente(self, nodoSiguiente):
        self._nodoSiguiente = nodoSiguiente
    
    def guardarAnterior(self, nodoAnterior):
        self._nodoAnterior = nodoAnterior
    
    #def obtenerSiguiente(self, nodSiguiente):
    #    return self._nodoSiguiente
    #
    #def obtenerAnterior(self, nodoAnterior):
    #    return self._nodoAnterior
    
    def obtenerSiguiente(self):
        return self._nodoSiguiente
    
    def obtenerAnterior(self):
        return self._nodoAnterior