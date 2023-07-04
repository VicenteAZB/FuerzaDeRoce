import matplotlib.pyplot as plt
import numpy as np
from Tkinter import *


def calcular_movimiento():
    masa_valor = float(masa.get())
    fuerza_valor = float(fuerza.get())
    coef_est_valor = float(coef_est.get())
    coef_din_valor = float(coef_din.get())
    
    # Parametros del movimiento
    tiempo_total = 10  # Tiempo total de simulacion en segundos
    delta_t = 0.01  # Incremento de tiempo en segundos

    # Coeficientes de friccion
    friccion_estatica = coef_est_valor  # Coeficiente de friccion estatica
    friccion_dinamica = coef_din_valor  # Coeficiente de friccion dinamica

    # Listas para almacenar los resultados
    tiempo = np.arange(0, tiempo_total, delta_t)
    posicion = []
    velocidad = []

    # Inicializacion de variables
    posicion_actual = 0
    velocidad_actual = 0
    friccion = 0

    # Simulacion del movimiento
    for t in tiempo:
        if velocidad_actual == 0:
            friccion = friccion_estatica
        else:
            friccion = friccion_dinamica

        aceleracion = (fuerza_valor - friccion * np.sign(velocidad_actual)) / masa_valor
        velocidad_actual += aceleracion * delta_t
        posicion_actual += velocidad_actual * delta_t

        # Almacenar resultados
        posicion.append(posicion_actual)
        velocidad.append(velocidad_actual)

    # Grafico de la posicion en funcion del tiempo
    plt.figure()
    plt.plot(tiempo, posicion)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Posicion (m)')
    plt.title('Movimiento con Roce')
    plt.grid(True)
    plt.show()

    # Grafico de la velocidad en funcion del tiempo
    plt.figure()
    plt.plot(tiempo, velocidad)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.title('Velocidad con Roce')
    plt.grid(True)
    plt.show()


BG = Tk()
BG.resizable(0, 0)
BG.geometry("1000x600")
BG.config(bg='red')
BG.config(bd=30)
BG.config(relief='sunken')

C1 = Frame()
C1.pack(side="top", pady=10)
C1.config(bg='blue')
C1.config(width='300', height='100')
C1.config(bd=15)
C1.config(relief="sunken")

C2 = Frame()
C2.pack(side="bottom")
C2.config(bg='grey')
C2.config(width='300', height='100')
C2.config(bd=15)
C2.config(relief="sunken")

Label(C1, text=('Ingrese parametros'), font=('Arial', 20)).place(x='15', y='15')

masa = Entry(C2)
masa.grid(row=0, column=1)
Label(C2, text='Masa(Kg):', font=('Arial', 12)).grid(row=0, column=0, sticky='e', padx=10, pady=10)

fuerza = Entry(C2)
fuerza.grid(row=1, column=1)
Label(C2, text='Fuerza(N):', font=('Arial', 12)).grid(row=1, column=0, sticky='e', padx=10, pady=10)

coef_est = Entry(C2)
coef_est.grid(row=2, column=1)
Label(C2, text='Coef.Est:', font=('Arial', 12)).grid(row=2, column=0, sticky='e', padx=10, pady=10)

coef_din = Entry(C2)
coef_din.grid(row=3, column=1)
Label(C2, text='Coef.Din:', font=('Arial', 12)).grid(row=3, column=0, sticky='e', padx=10, pady=10)

Button(C2, text='Calcular', command=calcular_movimiento).grid(row=4, column=0, columnspan=2, pady=10)

BG.mainloop()



