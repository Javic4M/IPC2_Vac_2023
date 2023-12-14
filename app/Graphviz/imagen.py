from graphviz import Digraph
from graphviz import nohtml
from app.lista.Lista import Lista
from app.biblioteca.Cancion import Cancion
from app.biblioteca.Biblioteca import Biblioteca

class Graphviz:
    
    def graficarTodasLasCanciones(listaDeCanciones: Lista):
        longitud = listaDeCanciones.obtenerLongitud()    
        
        dot = Digraph('imagenGraphviz', format='png', node_attr={'width': '.2', 'height': '.5'})

        contador = 0
        dot.node('1','Lista de Reproducción')
        while contador < longitud:
            contador += 1
            cancion: Cancion
            cancion = listaDeCanciones.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            dot.node(str(contador + 1), nohtml(cancion.get_nombre() + ' | { Album:  ' +  cancion.get_album() + ' | Artista:  ' + cancion.get_artista() + '}'), style='filled', shape='record')
            dot.edges([str(contador) + str(contador + 1)])

        print(dot.source)  
        dot.render(view=True)
       
    # Pendiente de Imprementar Logica
    def graficarAlbum(listaDeAlbumnes: Lista):
        longitud = listaDeAlbumnes.obtenerLongitud() 
        
        dot = Digraph('imagenGraphviz', format='png', node_attr={'width': '.2', 'height': '.5'})

        contador = 0
        dot.node('1','Lista de Reproducción')
        while contador < longitud:
            contador += 1
            cancion: Cancion
            cancion = listaDeAlbumnes.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            dot.node(str(contador + 1), nohtml(cancion.get_nombre() + ' | { Album:  ' +  cancion.get_album() + ' | Artista:  ' + cancion.get_artista() + '}'), style='filled', shape='record')
            dot.edges([str(contador) + str(contador + 1)])

        print(dot.source)  
        dot.render(view=True) 
      
        
c = Graphviz

biblio = Biblioteca()
biblio.agregarCancionPorDatos("Merry Chirstman", "Javier", "Navidad", "imagen_1.png", "ruta_1.mp3")
biblio.agregarCancionPorDatos("Navidad", "Carlos", "Navidad_2", "imagen_2.png", "ruta_2.mp3")
biblio.agregarCancionPorDatos("Peces en el Rio", "Luis", "Reflexion", "imagen_3.png", "ruta_3.mp3")
biblio.agregarCancionPorDatos("Belen", "Luis", "Reflexion", "imagen_3.png", "ruta_3.mp3")

c.graficarTodasLasCanciones(biblio.obtenerTodasLasCanciones())