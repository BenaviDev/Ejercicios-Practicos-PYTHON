def run():
    #variable (contador) que le asigna el valor de (1)
    # contador = 1
    # #imprime el contador
    # print(contador)
    # #mientras que (contador) sea menor a (1000)
    # while contador<1000:
    #     #(contador) va ser igual a (contador) mas (1) osea que ahora vale (2)
    #     contador = contador + 1
    #     #atajo para escribir lo mismo que arriba
    #     contador +=1
    #     #imprime el nuevo valor del (contador)
    #     print(contador)


    #para el contador en el rango de 1000 sucede:
    #va desde el 0 hasta el 1000
    for contador in range(1001):
        print(contador)

    print('La tabla del 11')
    for i in range(0, 10):
        print(11*i)

if __name__ == '__main__':
    run()