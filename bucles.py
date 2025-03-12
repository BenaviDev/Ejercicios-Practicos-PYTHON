# Definir la función principal 'run'
# Esta función calcula y muestra las potencias de 2 hasta alcanzar un límite

def run():
    # Variable constante que define el límite máximo
    # En Python, las constantes se escriben en mayúsculas por convención
    LIMITE = 1000000
    
    # Se define una variable contador para llevar el seguimiento del exponente
    contador = 0
    
    # Se calcula la primera potencia de 2 (2^0 = 1)
    potencia_2 = 2 ** contador
    
    # Mientras la potencia de 2 calculada sea menor que el límite, el ciclo se ejecuta
    while potencia_2 < LIMITE:
        # Se imprime el valor actual de la potencia de 2
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        
        # Se incrementa el contador en 1 (siguiente exponente)
        contador = contador + 1
        
        # Se recalcula la potencia de 2 con el nuevo contador
        potencia_2 = 2 ** contador
        
        # El ciclo se repite hasta que la potencia de 2 sea mayor o igual al límite

# Se verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    run()  # Llamada a la función principal
