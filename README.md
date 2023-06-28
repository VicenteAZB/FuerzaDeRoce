# FuerzaDeRoce
Nombre del proyecto: Simulación del roce estático y dinámico

Descripción: Nuestro proyecto consiste en simular el movimiento fisico de un cuerpo el cual se somete a la fuerza de roce estático y dinámico.

Origen: El estudio del roce entre dos cuerpos comienza con Leonardo Da Vinci, él dedujo las leyes aplicadas al movimiento de un cuerpo
rectangular sobre una superficie plana, sin embargo este estudio pasó desapercibido en su época.

Matemática empleada: 
La fuerza de fricción se calcula con la fórmula Fr = u * N, donde Fr es fuerza de roce, u es coeficiente de roce y N 
es la fuerza normal. 

La aceleración del cuerpo en un plano inclidado (como es el caso de nuestra simulación) se define con la siguiente 
fórmula: a = g * sin alpha - u * g * cos alpha, donde a es aceleración, g es aceleración de gravedad (9.8), sin alpha es seno del ángulo 
(en ese caso ángulo alpha) y cos alpha es coseno del ángulo alpha. 

La posición del cuerpo en el plano inclidado se define con la fórmula x = 0.5 * a * t^2, donde x es la posición y t es el tiempo transcurrido 
desde que el cuerpo empezó a acelerar. 

Uso de las fórmulas:
Cuando el coeficiente de roce sea 0.7 y la masa del cuerpo sea 15 Kg (Coeficiente de roce y masa serán parametros que el usuario agregará)
la fuerza de roce se calculará como Fr = 0.7 * N, pero N en un plano inclinado es lo mismo que m * g * cos alpha, por ende la fuerza normal 
será 15 * 9.8 * cos 70°(ángulo del plano inclinado). Finalmente la fórmula resultante será Fr = 0.7 * 93 = 65 N (Newton).

La aceleración del ejemplo anteriór se calculará como a = 9.8 * sin 70° - 0.7 * 9.8 * cos 70°, dando como resultado 3.24 m/s^2.

La posición en tres segundos desde que empezó a acelerar el cuerpo de los ejemplos anteriores se define con la fórmula x = 0.5 * 3.24 * 3^2
Lo que dará como resultado 14.58 m desde la posición inicial.

Aplicación de las fórmulas en la simulación:
Se usarán estas fórmulas para acercar nuestra simulación a la realidad, estas fórmulas se usarán con números reales puesto que los resultados
no siempre son enteros.

Descripción de las herramientas utilizadas:
Python: Lenguaje base de nuestro código.
Matplotlib: Libreria diseñada para crear gráficos.
Numpy: Libreria usada para hacer cálculos matemáticos
Tkinter: Libreria utilizada para crear la interfaz de usuario.
PyGame: Libreria diseñada para agregarimagenes (o Sprites) a una surface (Superficie)
GitHub: Repositorio para compartir y mantener al dia a todos los colaboradores del proyecto.
Visual Studio Code: Editor de texto 

Guía de instalación:
Para descargar Python deberán dirigirse a su navegador y dirigirse a la pagina python.org, estando en la página descargan python 2.7.15 y luego lo instalan.
Para instalar Visual Studio Code es lo mismo se entra a la pagina visualstudio.com se descarga y luego se instala en el pc.
Luego dentro del Visual Studio Code se abre una terminal y se ingresan los siguientes comandos para instalar las librerias necesarias:

1) Pygame: python -m pip install -U pygame==2.4.0 --user
2) Matplotlib: python -m pip install -U matplotlib
3) Numpy: pip install numpy
4) Tkinter: python -m tkinter

Guía de uso: 

Visual Studio Code: Interpreta el lenguaje Python para poder utilizarlo.

Pygame: Es una librería para el desarrollo de videojuegos en segunda dimensión 2D con el lenguaje de programación Python, y para utilizarlo se debe colocar al inicio del código "import pygame".

Matplotlib: Es una librería completa para crear estática, animada, y visualizaciones interactivas en Python. Matplotlib hace cosas fáciles cosas fáciles y difíciles posibles, para utilizar también se deberá colocar al inicio del código "import matplotlib.pyplot as plt"

Numpy: NumPy se puede utilizar para realizar una amplia variedad de operaciones matemáticas en matrices. Agrega poderosas estructuras de datos a Python que garantizan cálculos eficientes con arreglos y matrices y proporciona una enorme biblioteca de funciones matemáticas de alto nivel que operan en estos arreglos y matrices, en este caso igual se debe escribir al inicio del código "import numpy".

Tkinter: Una librería del lenguaje de programación Python y funciona para la creación y el desarrollo de aplicaciones de escritorio. Esta librería facilita el posicionamiento y desarrollo de una interfaz gráfica de escritorio con Python, igual al inicio del código se debe colocar "from Tkinter import *", esta forma sirve para python 2.7.15.

Conclusiones: En conclusión nuestro trabajo al hacer uso de diferentes programas y librerías pudimos hacer un código que puede mostrar de forma gráfica y númerica como se ve el roce estático y dinámico usando diferentes parámetros prar ejemplificarlo en diferentes escenarios. 
