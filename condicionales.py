# preguntar al usuario la edad y a ese valor se
# convierte a entero con el (int) y ese valor se guarda 
# en la variable edad
# edad = int(input("Escribe tu edad: "))

# #(if) es (Si) ---> entonces se hace (algo)
# if edad >17: 
#     print("Eres mayor de edad")
#     #(else) significa (Sino)
# else:
#     print("Eres menor de edad")

numero = int(input("Escribe un numero: "))
if numero >5:
    print("El numero que ingreso es Mayor a 5")
elif numero == 5:
    print('El numero que ingreso es igual 5')
else:
    print('El numero que ingreso es menor a 5')