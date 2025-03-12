# importar libreria random
import random

# importar libreria tkinter interfaz
import tkinter as tk
from tkinter import ttk


# funcion para el boton enviar
def boton_enviar():

    # el numero obtenido de caja 1 se pasa a entero y se almacena en la variable (numero_elegido)
    numero_elegido = int(caja_1.get())
    # si el numero_elegido es menor al numero aleatorio
    if numero_elegido < numero_aleatorio:
        # actualiza el label del resultado para que aparezca:
        label_resultado.config(text="Busca un número más grande")
        # elif (numero_elegido) es mayor al numero elegido aleatoriamente entonces:
    elif numero_elegido > numero_aleatorio:
        # actualiza el texto del label de resultado para que diga:
        label_resultado.config(text="Busca un número más pequeño")
        # si todo sale bien entonces:
    else:
        # actualiza label de resultado para que diga que ganó
        label_resultado.config(text="¡Ganaste!")


def run():
    # variable global
    global numero_aleatorio
    # seleccion de un numero aleatorio entre el 1 y 50
    numero_aleatorio = random.randint(1, 50)
    # configuramos el texto del label 1 para que diga:
    label_1.config(text="Elige un número del 1 al 50: ")
    # limpiamos contenido de la caja
    caja_1.delete(0, tk.END)
    # actializamos el label de resultado para poder mostrar otro mensaje
    label_resultado.config(text="")


# Ventana principal
ventana = tk.Tk()
ventana.title("Adivina el número")
ventana.geometry("380x80")
ventana.resizable(0, 0)

# Variables
numero_aleatorio = 0
n_ingresado = tk.StringVar()

# label 1 ( Elige un número del 1 al 50: )
label_1 = tk.Label(ventana, text="Elige un número del 1 al 50: ")
label_1.grid(column=0, row=0, padx=10, pady=10)

# caja 1
caja_1 = ttk.Entry(ventana, textvariable=n_ingresado)
caja_1.grid(column=1, row=0)

# crear boton para enviar
boton_enviar = ttk.Button(ventana, text="Prueba", command=boton_enviar)
boton_enviar.grid(column=2, row=0)

# label para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.grid(column=1, row=2)

# Iniciar el juego
run()

ventana.mainloop()
