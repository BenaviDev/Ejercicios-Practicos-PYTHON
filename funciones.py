# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print ('Estoy aprendiendo a usar funciones')

# #invocar la funcion  ir a la def de la funcion y ejecuta la logica dentro de ella
# imprimir_mensaje()
# imprimir_mensaje()


#parametros son variables disponibles para usar dentro de la funcion

 # instrucciones de la función
# def conversacion( mensaje):
#     print('Hola')
#     print('como estas')
#     print(mensaje)
#     print('Adios')

# opcion = int(input('elige una opcion: (1, 2, 3) '))

# if opcion== 1:
    
#     conversacion('Elegiste la opcion 1')
# elif opcion== 2:
    
#     conversacion('Elegiste la opcion 2')
# elif opcion== 3:
    
#     conversacion('Elegiste la opcion 3')
# else:
#     print('Elige la opcion correcta')


#definir la funcion
def suma (a, b):
    #se imprime por pantalla:
    print('se suman 2 numeros (1+4)')
    #se crea una variable que sera (resultado)
    #dentro de la variable (resultado) se va guardar (1 + 4 osea 5)
    resultado = a + b
    #luego (return) devuelve o retorna el (resultado)
    #El cual se guarda en la variable (sumatoria)
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)