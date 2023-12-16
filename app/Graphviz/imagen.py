from graphviz import Digraph
from graphviz import nohtml
from app.lista.Lista import Lista
from app.biblioteca.Cancion import Cancion
from app.biblioteca.Album import Album
from app.biblioteca.Biblioteca import Biblioteca

class Graphviz:
    
    def graficarTodasLasCanciones(listaDeReproduccion: Lista):
        longitud = listaDeReproduccion.obtenerLongitud()    
        
        dot = Digraph(filename="GraphvizCanciones", format="jpg", node_attr={'width': '.2', 'height': '.5'})

        contador = 0
        dot.node('1','Lista de Reproducción')
        while contador < longitud:
            contador += 1
            cancion: Cancion
            cancion = listaDeReproduccion.encontrarPorIndiceInicioFinal(contador).obtenerDato()
            dot.node(str(contador + 1), nohtml(cancion.get_nombre() + ' | { Album:  ' +  cancion.get_album() + ' | Artista:  ' + cancion.get_artista() + '}'), style='filled', shape='record')
            dot.edges([str(contador) + str(contador + 1)])

        print(dot.source)  
        dot.render(view=True)
       
    # Recibe como parametros una lista de Albumnes para que los pueda mostrar
    def graficarAlbum(listaDeAlbumnes: Lista):
        longitudAlbumnes = listaDeAlbumnes.obtenerLongitud() 
        
        dot = Digraph(filename='GraphvizAlbum', format="jpg", node_attr={'width': '.2', 'height': '.5'})

        contardorAlbumnes = 0
        contadorCanciones = 0
        contador = 0
        album: Album
        
        # Este ciclo sirve para que no muestre solo un albúm sino todos los que estan en la Lista
        while contardorAlbumnes < longitudAlbumnes:
            contardorAlbumnes += 1
            album = listaDeAlbumnes.encontrarPorIndiceInicioFinal(contardorAlbumnes).obtenerDato().obtenerDato()
            
            listaCanciones = album.obtenerListaCanciones()
            longitudCanciones = listaCanciones.obtenerLongitud()

            with dot.subgraph(name='cluster_' + str(contardorAlbumnes)) as sub:
                contadorCanciones = 0
                
                while contadorCanciones < longitudCanciones:
                    contadorCanciones += 1
                    contador += 1
                    cancion: Cancion
                    cancion = listaCanciones.encontrarPorIndiceInicioFinal(contadorCanciones).obtenerDato()
                    
                    sub.attr(style='filled', color='lightgrey')
                    sub.node_attr.update(style='filled', color='white')             
                    sub.node(str(contador), nohtml('{ Canción:  ' +  cancion.get_nombre() + ' | Artista:  ' + cancion.get_artista() + '}'), style='filled', shape='record')
                    
                    if contadorCanciones < longitudCanciones:
                        sub.edges([str(contador) + str(contador + 1)])
                    sub.attr(label='Albúm:  ' + album.obtenerNombre())
        
        print(dot.source)  
        dot.render(view=True) 
      
        
# COdigo de prueba si quieren ver el resutaldo, importante tener instanlado Graphviz

c = Graphviz
biblio = Biblioteca()
biblio.agregarCancionPorDatos("Merry Chirstman", "Javier", "Navidad", "imagen_1.png", "ruta_1.mp3")
biblio.agregarCancionPorDatos("Navidad", "Javier", "Navidad", "imagen_2.png", "ruta_2.mp3")
biblio.agregarCancionPorDatos("Peces en el Rio", "Luis", "Reflexion", "imagen_3.png", "ruta_3.mp3")
biblio.agregarCancionPorDatos("Belen", "Luis", "Reflexion", "imagen_3.png", "ruta_3.mp3")

# Seleccionen que quieren ver si las canciones o los albumnes

c.graficarTodasLasCanciones(biblio.obtenerTodasLasCanciones())
#c.graficarAlbum(biblio.obtenerListaAlbumes())
