# Definición de un diccionario simple con llaves y valores numéricos
mi_diccionario = {
    'llave1': 1,
    'llave2': 2,
    'llave3': 3,
}

# Diccionario que almacena la población de algunos países
poblacion_paises = {
    'Argentina': 45345123,
    'Colombia': 490534231,
    'Mexico': 35599443,
    'Rusia': 34203001,
}

# Iterar sobre las claves del diccionario (solo imprime los nombres de los países)
# for pais in poblacion_paises.keys():
#     print(pais)

# Iterar sobre los valores del diccionario (solo imprime las poblaciones)
# for poblacion in poblacion_paises.values():
#     print(poblacion)

# Iterar sobre los elementos del diccionario usando .items()
# Esto devuelve tuplas con clave y valor (país y su población)
for pais, poblacion in poblacion_paises.items():
    print(pais + ' tiene ' + str(poblacion) + ' habitantes')

# Acceder a un valor específico del diccionario mediante su clave
print('La población de México es de:', poblacion_paises['Mexico'], 'personas')
