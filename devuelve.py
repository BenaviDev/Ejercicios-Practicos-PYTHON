# definir la funcion principal
def main(numero):
    # si es menor que dos no es primo y retorna false
    if numero < 2:
        return False

    # Itera desde 2 hasta la mitad del numero (mas 1), ya que no hay divisores más allá de la mitad
    for i in range(2, int(numero * 0.5) + 1):
        # Si el número es divisible por algún valor en el rango, no es primo, retorna False
        if numero % i == 0:
            return False

    # Si no se encontraron divisores, el número es primo, retorna True
    return True


# Solicita al usuario que ingrese un límite hasta el cual se buscarán números primos
limite = int(input("Ingresa un límite de número: "))

# Imprime un mensaje indicando que se mostrarán los números primos hasta el límite ingresado
print("Números primos hasta", limite, ":")

# Itera desde 2 hasta el límite ingresado
for num in range(2, limite + 1):
    # Si la función 'main' devuelve True, el número es primo y se imprime
    if main(num):
        print(num)
