"""
    Escribir una función que tome un caracter y devuelva true si es vocal y false si no es vocal

    1. definimos la funcion  caracter_vocal con un parametro llamado (caracter)
    2. creamos una variable (caracteres) que contendra una lista con las vocales ['a','e','i','o','u']
    3. si el caracter esta en la lista de caracteres imprime True, sino es False

"""

def caracter_vocal(caracter):
    caracteres = ['a', 'e', 'i', 'o', 'u']
    if caracter in caracteres:
        return True
    else:
        return False
print(caracter_vocal('f'))
    