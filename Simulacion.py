import pygame

# Inicializacion de Pygame
pygame.init()

# Dimensiones de la ventana
width = 1400
height = 600

# Colores
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Configuracion de la ventana
window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

def movimiento_con_friccion(masa, fuerza, coeficiente_roce_estatico, coeficiente_roce_dinamico, tiempo):
    # Coeficientes de friccion
    coeficiente_roce_estatico = coeficiente_roce_estatico
    coeficiente_roce_dinamico = coeficiente_roce_dinamico

    # Fuerza maxima de friccion estatica
    fuerza_max_estatica = 10

    # Determinar si hay movimiento o no
    if abs(fuerza) <= fuerza_max_estatica:
        # Fuerza aplicada no supera la fuerza maxima estatica
        fuerza_friccion = -fuerza  # Fuerza de friccion estatica contrarresta la fuerza aplicada
        aceleracion = 0
        velocidad = 0
    else:
        # Fuerza aplicada supera la fuerza maxima estatica
        fuerza_friccion = -coeficiente_roce_dinamico * masa * 9.8  # Fuerza de friccion dinamica
        aceleracion = (fuerza + fuerza_friccion) / masa
        velocidad = aceleracion * tiempo

    # Posicion resultante
    posicion = 0.5 * aceleracion * (tiempo ** 2)

    return aceleracion, velocidad, posicion

# Parametros de ejemplo
masa = 3  # en kg
fuerza = 20  # en N
coeficiente_roce_estatico = 0.7
coeficiente_roce_dinamico = 0.6
tiempo = 0.5  # en segundos

# Posicion inicial
posicion_x = 887 
posicion_y = 200   #pelota roja
posicion_x2 = 215
posicion_y2 = 200  #pelota verde
 
# Triangulo rectangulo
triangulo = [(20, height - 100), (650, height - 100), (20, height - 500)] #triangulo verde
triangulo2 = [(770, height - 100), (1158, height - 100), (770, height - 500)]#triangulo rojo

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    # Actualizacion de la posicion y velocidad del circulo verde
    aceleracion, velocidad, posicion = movimiento_con_friccion(masa, fuerza,
                                                            coeficiente_roce_estatico,
                                                            coeficiente_roce_dinamico, tiempo)
    posicion_y += aceleracion+velocidad+posicion
    posicion_x += aceleracion+velocidad+posicion

    # Dibujo en la ventana
    window.fill(white)

    # Dibujo del triangulo rectangulo
    pygame.draw.polygon(window, green, triangulo)
    pygame.draw.polygon(window, red, triangulo2)

    # Dibujo del objeto (pelota)
    pygame.draw.circle(window, green, (int(posicion_x), int(posicion_y)), 21)
    pygame.draw.circle(window, red, (int(posicion_x2), int(posicion_y2)), 21)

    # Actualizacion de la ventana
    pygame.display.flip()
    clock.tick(60)
