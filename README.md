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
