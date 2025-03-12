mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

poblacion_paises = {
        'Argentina': 45345123,
        'Colombia': 490534231,
        'Mexico': 35599443,
        'Rusia': 34203001,
    }


#solo la llave
# for pais in poblacion_paises.keys():
#     print(pais)

#solo los valores de la llave
# for pais in poblacion_paises.values():
#     print(pais)

#devuelve todos los items


#concatenar todo
for pais, poblacion in poblacion_paises.items():
    print(pais + ' Tiene ' + str(poblacion)+ ' habitantes')



print('la poblacion es de: ', poblacion_paises['Mexico'], ' De personas')

