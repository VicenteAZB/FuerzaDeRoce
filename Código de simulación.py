import pygame

# Inicializacion de Pygame
pygame.init()

# Dimensiones de la ventana
width = 425
height = 700

# Colores
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black= (0,0,0)
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
        fuerza_friccion = -coeficiente_roce_dinamico * masa * 9.8 * 0.95  # Fuerza de friccion dinamica
        aceleracion = (fuerza + fuerza_friccion) / masa
        velocidad = aceleracion * tiempo

    # Posicion resultante
    posicion = 0.5 * aceleracion * (tiempo ** 2)

    return aceleracion, velocidad, posicion

# Parametros de ejemplo
masa = float(input("Ingrese masa: "))  # en kg
fuerza = float(input("Ingrese fuerza: "))  # en N
coeficiente_roce_estatico = float(input("Ingrese el coeficiente de roce estatico: "))
coeficiente_roce_dinamico = float(input("Ingrese el coeficiente de roce dinamico: "))
tiempo = float(input("Ingrese el tiempo: "))  # en segundos

# Posicion inicial
posicion_x = 150 
posicion_y = 300   #pelota verde
 
# Triangulo rectangulo
triangulo = [(20, height - 100), (420, height - 100), (20, height - 500)]#triangulo rojo

def Plano():
    # Dibujo del triangulo rectangulo
    pygame.draw.polygon(window, red, triangulo)

def Masa():
    # Dibujo del objeto (pelota)
    pygame.draw.circle(window, green, (int(posicion_x), int(posicion_y)), 21)

# Bucle principal del juego
while True:
    X = 150 ; Y = 300
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posicion_x = X ; posicion_y = Y
 

    # Actualizacion de la posicion y velocidad del circulo verde
    window.fill(white)

    
    Plano()
    Masa()

    posicion_y += (masa+fuerza+coeficiente_roce_dinamico+tiempo)-(coeficiente_roce_estatico+coeficiente_roce_dinamico)
    posicion_x += (masa+fuerza+coeficiente_roce_dinamico+tiempo)-(coeficiente_roce_estatico+coeficiente_roce_dinamico)

    

    # Actualizacion de la ventana
    pygame.display.flip()
    clock.tick(60)












