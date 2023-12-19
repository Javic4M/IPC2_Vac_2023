## Table of Contents
1. [Informacion General](#info-general)
2. [Tecnologias](#tecnologias)
3. [Instalacion](#instalacion)
4. [Problemas Generales](#problemas-generales)
5. [FAQs](#faqs)
### Informacion General
***
El proyecto consiste en realizar una aplicacion de escritorio, la cual es un reproductor de musica (de nombre IPCmusic) con una interfaz de usuario amigable la cual permite ordenar la musica en el ordenador del usuario, asi como presentar estadisticas de las canciones
### Screenshot
***
<img src="https://i.imgur.com/kWmEQ9a.jpg"/>
<img src="https://i.imgur.com/GUjH2ML.jpg"/>
<img src="https://i.imgur.com/ectR5D5.jpg"/>
<img src="https://i.imgur.com/BjWCvKq.jpg"/>
<img src="https://i.imgur.com/9rIQkcG.jpg"/>

## Tecnologias
***
Las tecnologias usadas para la realizacion del proyecto fueron:
* [Lenguaje Principal: Python](https://www.python.org/): Version 3.12.1
* [IDE: Visual Studio Code](https://code.visualstudio.com/): Version 1.85
* [Libreria: PyGame](https://www.pygame.org): Version 2.5.1
* [Libreria: Pillow](https://pypi.org/project/Pillow/): Version 2.5.1
* [Libreria: Graphbiz](https://graphviz.org/)

## Instalacion
***
Para ejecutar el programa, es necesario tener las librerias PyGame y Pillow en su ultima versión a la fecha (18 de diciembre de 2023).

Para instalar PyGame, se ingresa el siguiente comando en la terminal/CMD (En VSC es suficiente abrir la terminal).
```bash
pip install pygame
```

Para instalar Pillow, se ingresa el siguiente comando en la terminal/CMD (En VSC es suficiente abrir la terminal).
```bash
pip install Pillow
```

Para instalar Graphbiz, se ingresa el siguiente comando en la terminal/CMD (En VSC es suficiente abrir la terminal).
```bash
pip install graphviz
```
Adicional se tiene que instalar nativamente Graphbiz para su correcto funcionamiento, esto se puede realizar desde su pagina web.

Si se tienen problemas a instalar las librerias, revisar la seccion Problemas Generales.
Para ejecutar el programa, se debe abrir el archivo **Main.py**

## Problemas Generales
***
Si se tiene algun problema al instalar las librerias, se puede probar a colocar un "--user" al final de los comandos.
Si se presenta otro problema adicional, contactar a cualquiera de los colaboradores.


## FAQs
***
1. **¿Como puedo cargar listas de reproducción?**
Las listas se cargan al iniciar la aplicación leyendo un archivo xml en el directorio donde se encuentra Main.py con la ruta ./Listas de reproduccion.xml

2. **¿Que formato debe tener los archivos XML?**
El archivo debe tener el siguiente formato 
(Biblioteca):
```bash
<?xml version="1.0" encoding="UTF-8"?> 
<biblioteca>
    <cancion nombre="Nombre de la Cancion">
        <artista>"Nombre del Artista"</artista>
        <album>"Nombre del Album"</album>
        <imagen>"la\ruta\de\imagen.jpg"</imagen>
        <ruta>"la\ruta\de\cancion.mp3"</ruta>
    </cancion>
    <cancion nombre="Nombre de la Cancion">
        <artista>"Nombre del Artista"</artista>
        <album>"Nombre del Album"</album>
        <imagen>"la\ruta\de\imagen.jpg"</imagen>
        <ruta>"la\ruta\de\cancion.mp3"</ruta>
    </cancion>
    ...
    ...
</biblioteca>
```

(Listas de Reproducción):
```bash
<?xml version="1.0" encoding="UTF-8"?> 
<ListasReproduccion>
    <Lista nombre="IPC2!">
        <cancion nombre="Afterthought">
            <artista>Joji</artista>
            <album>Nectar</album>
            <imagen>./Ejemplo de archivos/nectar.png</imagen>
            <ruta>./Ejemplo de archivos/Joji Afterthought.mp3</ruta>
        </cancion>
        <cancion nombre="YUKON">
            <artista>Joji</artista>
            <album>Smithereens</album>
            <imagen>./Ejemplo de archivos/smithereens.jpg</imagen>
            <ruta>./Ejemplo de archivos/Joji - YUKON.mp3</ruta>
        </cancion>
        <cancion nombre="Prendele Fuego">
            <artista>Mon Laferte</artista>
            <album>Autopoietica</album>
            <imagen>./Ejemplo de archivos/Autopoietica.jpg</imagen>
            <ruta>./Ejemplo de archivos/Mon - Prendele Fuego.mp3</ruta>
        </cancion>
    </Lista>
    <Lista nombre="Lista 2">
        <cancion nombre="Amantes Suicidas">
            <artista>Mon Laferte</artista>
            <album>Autopoietica</album>
            <imagen>./Ejemplo de archivos/Autopoietica.jpg</imagen>
            <ruta>./Ejemplo de archivos/Mon - Amantes Suicidas.mp3</ruta>
        </cancion>
        <cancion nombre="Dissolve">
            <artista>Joji</artista>
            <album>Smithereens</album>
            <imagen>./Ejemplo de archivos/smithereens.jpg</imagen>
            <ruta>./Ejemplo de archivos/Joji - Dissolve.mp3</ruta>
        </cancion>
    </Lista>
</ListasReproduccion>
```
Trata de seguir este formato para que se agregen las canciones que desees de manera correcta.
