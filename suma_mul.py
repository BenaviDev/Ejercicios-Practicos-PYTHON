"""
Esta función toma una lista de números y calcula el producto de todos sus elementos.

Funcionamiento:
1. Se inicializa la variable `result` con 1.
2. Se recorre la lista y se multiplica cada número por `result`.
3. Se muestra el resultado en pantalla con `print(result)`.
"""

def mult(lista):
    result = 1  # Inicializa el resultado en 1
    for num in lista:
        result = result * num  # Multiplica cada número de la lista
    print(result)  # Imprime el resultado

# Llamada a la función con una lista de prueba
mult([5, 5, 5])
