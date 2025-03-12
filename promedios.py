"""
Esta función toma una lista de números y calcula su promedio.

Funcionamiento:
1. Se recibe una lista de números como parámetro.
2. Se calcula la suma total de los elementos de la lista con `sum(numeros)`.
3. Se divide la suma total entre la cantidad de elementos en la lista con `len(numeros)`.
4. Se retorna el valor del promedio.
"""

def lista_num(numeros):
    total_suma = sum(numeros)  # Suma todos los elementos de la lista
    promedio = total_suma / len(numeros)  # Divide la suma entre la cantidad de elementos
    return promedio  # Retorna el promedio

# Lista de prueba
lista_numeros = [2, 5, 3, 3, 5, 7]

# Llamada a la función y mostrar el resultado
resultado = lista_num(lista_numeros)
print("El promedio es:", resultado)
