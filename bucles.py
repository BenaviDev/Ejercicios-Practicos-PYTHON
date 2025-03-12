#obligatorio definir la funcion inicial
def run():
    #variable constante, ya no varía
    #si se define la variable con mayuscula se vuelve una constante
    LIMITE = 1000000
    #definir variable (contador)
    contador = 0
    #crea la variable (potencia_2)
    potencia_2 = 2**contador
    #MIENTRAS LA (POTENCIA_2) SEA MENOR AL LIMITE SE EJECUTA:
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str (contador) + ' Es igual a:' + str(potencia_2))
        #contador ahora vale 1
        contador=contador+1
        #y potencia_2 elevado al contador que ahora es 1 lo cual es 2
        potencia_2 = 2**contador
        #y se repite el ciclo

if __name__ == '__main__':
    run()
