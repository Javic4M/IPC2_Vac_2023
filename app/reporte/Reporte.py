import os.path
import webbrowser
from app.lista.Lista import Lista
from app.reporte.BubbleSort import BubbleSort
from xml.dom import minidom


class Reporte:
    def __init__(self, ruta):
        self.ruta = ruta
        self.lista_canciones = Lista()

    def get_reporte(self):
        self.write_file()
        file = WebView()
        file.run()

    def lector(self):
        self.lista_canciones = Lista() #limpiar la lista.
        doc = minidom.parse(self.ruta)
        canciones = doc.getElementsByTagName("cancion")
        for cancion in canciones:
            nombre = cancion.getAttribute("nombre")
            imagen = cancion.getElementsByTagName("imagen")[0]
            repro = cancion.getElementsByTagName("reproducciones")[0]
            self.lista_canciones.agregarALaLista(InfoRanking(nombre, imagen.firstChild.data, repro.firstChild.data))

        for i in range(0, self.lista_canciones.obtenerLongitud()):
            print(self.lista_canciones.obtenerPorIndice(i + 1))

        self.ordenar()

    def obtener_pocentaje(self, cantidad):
        num_max = int(self.lista_canciones.obtenerPorIndice(1).reproducciones)
        resultado = (int(cantidad) * 100) / num_max
        return round(resultado, 0)

    def ordenar(self):
        list_tmp = Lista()
        arr = [self.lista_canciones.obtenerLongitud()]
        # pasar datos de la lista a un arreglo
        for i in range(0, self.lista_canciones.obtenerLongitud()):
            arr.append(self.lista_canciones.obtenerPorIndice(i + 1))

        # ordenar el arreglo temporal o lista
        bubble_sort = BubbleSort(arr)
        bubble_sort.ordenar()

        # pasar los datos del arreglo temporal a una lista doble
        for i in range(0, self.lista_canciones.obtenerLongitud()):
            list_tmp.agregarALaLista(arr[i + 1])
        # asignar los datos de la lista doble a la lista de canciones ya con orden de Mayor a menor
        self.lista_canciones = list_tmp

        print(" ")
        for i in range(0, self.lista_canciones.obtenerLongitud()):
            print(self.lista_canciones.obtenerPorIndice(i + 1))

    def generar_html(self):
        head_0 = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Reportes</title>
                <style>
                    *{
                        padding: 0;
                        margin: 0;
                        box-sizing: border-box;            
                    }
        
                    body{
                        height: 100vh;
                        background: black;            
                    }
        
                    .caja_padre{
                        width: 40%;                
                        min-width: 590px;
                        position: absolute;
                        transform: translate(-50%, -50%);
                        left: 50%;
                        top: 50%;
                    }
        
                    .contenedor{
                        width: 100%;
                        padding: 30px 30px 50px;
                        background: linear-gradient(450deg, #ff00cc, #333399);
                        border: 2px solid rgba(0, 0, 0, 0.06);
                        border-radius: 10px;
                        box-shadow: 0 20px 30px rgba(0, 0, 0, 0.2);
                        backdrop-filter: blur(10px);                
                    }
        
                    .contenedor *{
                        font-family: 'Courier New', Courier, monospace;
                        color: rgb(255, 255, 255);
                        font-weight: bolder;
                    }
        
                    h2{
                        margin-bottom: 50px;
                        letter-spacing: 2px;
                        text-align: center;
                        font-size: 25px;
                        font-weight: lighter;
                    }
        
                    .canciones:not(:last-child){
                        margin-bottom: 25px;
                    }
        
                    .detalles{
                        width: 100%;
                        display: flex;
                        justify-content: space-between;
                        margin-bottom: 8px;
                    }
        
                    .menu{
                        position: relative;
                        border: 1px solid #ffffff;
                        border-radius: 20px;
                    }
        
                    .menu div{
                        position: relative;
                        width: 0;
                        height: 8px;
                        border-radius: 10px;
                        background: linear-gradient(450deg,#00F260, #0575E6);
                    }\n
        """

        ani_css = ""
        for i in range(0, self.lista_canciones.obtenerLongitud()):
            if i == 10:
                break
            else:
                nombre = self.lista_canciones.obtenerPorIndice(i + 1).nombreCancion

                id_menu = nombre.replace(" ", "") + "-menu"
                id_barra_animacion = nombre.replace(" ", "") + "-barra"
                p1 = "\t#a" + id_menu + "{animation: a" + id_barra_animacion + " 3s forwards;\n\t}"
                p2 = f"\n\t\t@keyframes a{id_barra_animacion}" + " {"
                p3 = "\n\t100% { \n\twidth: " + str(
                    self.obtener_pocentaje(self.lista_canciones.obtenerPorIndice(i + 1).reproducciones)) + "%;"
                p4 = "\n\t}\n\t} \n"
                pf = p1 + p2 + p3 + p4
                ani_css += pf

        head = head_0 + ani_css + "</style> \n</head>\n"

        body_0 = """
            <body>
                <div class="caja_padre">
                    <div class="contenedor">
                        <h2>RESUMEN DE REPRODUCCIONES</h2>\n
            """

        body_1 = ""
        for i in range(0, self.lista_canciones.obtenerLongitud()):
            if i == 10:
                break
            else:
                id_menu = self.lista_canciones.obtenerPorIndice(i + 1).nombreCancion.replace(" ", "") + "-menu"
                contenido = f"""
                    <div class="canciones">
                        <div class="detalles">
                            <span>{self.lista_canciones.obtenerPorIndice(i + 1).nombreCancion}</span>
                            <span>{self.lista_canciones.obtenerPorIndice(i + 1).reproducciones}</span>
                        </div>
                        <div class="menu">
                        <div id="a{id_menu}"></div>
                    </div>
                    </div>\n
                    """
                body_1 += contenido

        body = body_0 + body_1

        end = """
                </div>
                </div>
                </body>
                </html>
            """

        return head + body + end

    def write_file(self):
        self.lector()
        path = ManejoDirectorio()
        if os.path.exists(path.obtener_directorio_anterior() + "_report.html"):
            os.remove(path.obtener_directorio_anterior() + "_report.html")
        else:
            print("File not Found")
        with open(path.obtener_directorio_anterior() + "_report.html", "w") as f:
            f.write(self.generar_html())
            f.close()
            print("archivo escrito correctamente")


class InfoRanking:
    def __init__(self, nombre_cancion, ruta_img, reproducciones):
        self.nombreCancion = nombre_cancion
        self.rutaImg = ruta_img
        self.reproducciones = reproducciones

    def __str__(self):
        cadena = f"Cancion= {self.nombreCancion}, Img= {self.rutaImg}, Count= {self.reproducciones}"
        return cadena


class ManejoDirectorio:
    @staticmethod
    def obtener_directorio_anterior():
        separador = os.path.sep
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        return separador.join(dir_actual.split(separador)[:-1])


class WebView:
    @staticmethod
    def run():
        patch = ManejoDirectorio()
        webbrowser.open_new_tab(patch.obtener_directorio_anterior() + "_report.html") #abre una el archivo html en el navegador
        print("vista iniciada")
