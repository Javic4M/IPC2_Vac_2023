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

## Tecnologias
***
Las tecnologias usadas para la realizacion del proyecto fueron:
* [Lenguaje Principal: Python](https://www.python.org/): Version 3.12.1
* [IDE: Visual Studio Code](https://code.visualstudio.com/): Version 1.85
* [Libreria: PyGame](https://www.pygame.org): Version 2.5.1
* [Libreria: Pillow](https://pypi.org/project/Pillow/): Version 2.5.1
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
Si se tienen problemas a instalar las librerias, revisar la seccion Problemas Generales.

## Problemas Generales
***


## FAQs
***
A list of frequently asked questions
1. **¿Como se agregan las canciones?: **
Las canciones se pueden agregar de dos formas:

>Individual (Archivo MP3): Al dar clic en el boton (NOMBRE BOTON), se abrira una ventana donde se puede escoger entre esta opcion y la siguiente, al dar clic en (NOMBRE BOTON) se abrira una ventana para buscar su archivo mp3 (podrá llenar su información de manera manual o llenarse de manera automática)

>Grupal (Archivo XML): Al dar clic en el boton (NOMBRE BOTON), se abrira una ventana donde se puede escoger entre esta opcion y la anterior, al dar clic en (NOMBRE BOTON) se abrira una ventana para buscar su archivo XML (en esta opcion no esta disponible el llenado de informacion manual, ya que esos datos deberian estar en el archivo XML)

2. **Otra pregunta**
Otra respuesta
3. **¿Que formato debe tener los archivos XML?**
El archivo debe tener el siguiente formato:
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
Trata de seguir este formato para que se agregen las canciones que desees de manera correcta.
