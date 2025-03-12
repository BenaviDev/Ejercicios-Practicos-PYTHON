# Una función en Python es un bloque de código reutilizable que realiza una tarea específica.
# Las funciones pueden aceptar valores de entrada (parámetros) y devolver un resultado.
# Permiten estructurar el código de manera modular y reutilizable.

# Definir la función suma con dos parámetros a y b
# Los parámetros permiten que la función reciba valores al ser llamada
def suma(a, b):
    # Se imprime un mensaje indicando la operación que se va a realizar
    print('Se suman 2 números:', a, '+', b)
    
    # Se crea una variable llamada 'resultado' que almacena la suma de a y b
    resultado = a + b
    
    # La función retorna el resultado de la suma
    # El valor retornado puede ser almacenado en una variable o utilizado directamente
    return resultado

# Se llama a la función 'suma' con los valores 1 y 4, 
# y se almacena el resultado en la variable 'sumatoria'
sumatoria = suma(1, 4)

# Se imprime el resultado de la suma
print(sumatoria)
