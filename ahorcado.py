# importar random
import random

# lista con las palabras del ahorcado
lista_palabras = ["jirafa", "Leon", "hipopotamo", "tigre"]
# a la variable palabra_seleccionada le damos un elemento de la lista aleatoriamente
palabra_seleccionada = random.choice(lista_palabras)
# CREAR 2 CONTADORES
# intentos = [] para saber los intentos acertados por el jugador
intentos = []
####################################################
# contador para los intentos fallidos del jugador
intentos_fallidos = 0
# mientras que los intentos sean menores a 6 ejecuta lo siguiente
while intentos_fallidos < 10:
    ## end =" " la próxima impresión se realizará en la misma línea y con un espacio en blanco al final.
    print("Palabra:", end=" ")
    ##############################+###################
    # nuevo bucle  for llamado  (letra)
    # para la letra en la palabra seleccionada
    for letra in palabra_seleccionada:
        # si es correcta agrega la letra a la consola
        if letra in intentos:
            print(letra, end=" ")
        else:
            # si no es correcta imprime ("_")
            print("_", end=" ")
            # imprime que no es correcto y concatena los intentos fallidos
    print("\nIncorrecto: " + str(intentos_fallidos))

    # pregunta de nuevo una palabra
    # .lower sirve para convertir todas las letras a minusculas
    intento = input("Pon una letra: ").lower()

    # revisa si las letras son correctas
    # si el intento esta en la palabra seleccionada entonces imprime correcto
    if intento in palabra_seleccionada:
        print("Correcto!")
        # .append agrega un numevo intento a los intentos[]
        intentos.append(intento)
        #######################################################################
    else:
        # si no es correcto imprime incorrecto y agrega al contador de intentos fallidos +=1
        print("Incorrecto.")
        intentos_fallidos += 1

    # Check para saber si el jugador ganó
    # si todas las letras de intentos son correctas y estan dentro de la palabra seleccionada
    if all(letra in intentos for letra in palabra_seleccionada):
        print("felicidades, ganaste un: " + palabra_seleccionada + " De peluche")
        break

# si el jugador llega a un maximo de intentos fallidos de 10 entonces imprime que ha perdido
if intentos_fallidos == 10:
    print("PERDISTE. la palabra era:", palabra_seleccionada)
