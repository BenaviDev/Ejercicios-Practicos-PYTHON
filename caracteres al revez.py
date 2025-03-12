# Definir la función principal 'run'
# Esta función invierte una cadena de caracteres ingresada por el usuario

def run():
    # Solicitar al usuario que ingrese una cadena de texto
    cadena = input('Escriba una cadena de caracteres: ')
    
    # Invertir la cadena utilizando el slicing [::-1]
    # Este método recorre la cadena desde el final hasta el inicio
    reves = cadena[::-1]
    
    # Mostrar el texto invertido al usuario
    print('Su texto al revés es: ', reves)

# Se verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    run()  # Llamada a la función principal
