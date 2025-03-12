
     for contador in range(1000):
         #si el contador al dividirlo entre 2, el resto de la division es distinto
         #de 0 salta la vuelta del ciclo y lo que esta abajo de continue no se ejecuta
         if contador % 2 != 0:
             continue
         print(contador)


    #la variable (i) recorre los numeros del 0 al 10000
     for i in range (10000):
         #se imprimen los numeros del 0 al 10000
         print(i)
         #pero...
         #si la variable (i) es igual a (5678) entonces para el ciclo
         if i == 5678:
             #detener (romper)
             break

     #la variable (texto) almacena un texto ingresado por el usuario
     texto = input('Escribe un texto: ')
     #para cada (letra) en la variable (texto)
     for letra in texto:
     #si la (letra) es igual a la letra (o) entonces para: 
         if letra == 'o':
         break
     #imprime cada letra hasta encontrarse con una (o)
     print(letra)

# Definir la función principal 'run'
# Esta función maneja la lógica de la licorería

def run():
    # Se muestra un mensaje de bienvenida
    print('LICORERIA !')
    
    # Se solicita la edad del usuario y se convierte a entero
    edad = int(input('Ingresa tu edad: '))
    
    # Se verifica si el usuario es mayor de edad
    if edad >= 18:
        # Se muestra el menú de bebidas alcohólicas y se solicita la selección del usuario
        menu = int(input("""
        Bienvenido a la licorería de Mou

                SELECCIONA UN NÚMERO DEL 1 AL 5

                1. Corona           $3.000
                2. Poker            $3.500
                3. Andina           $4.000
                4. Azteca           $4.500
                5. Club Colombia    $5.000
                """))
        
        # Se solicita la cantidad de productos a comprar
        cantidad = int(input('Cuántos productos va a comprar: '))
        
        # Se inicializa la variable 'total'
        total = 0
        
        # Se verifica qué bebida eligió el usuario y se calcula el total a pagar
        if   menu == 1:
            total = cantidad * 3000
        elif menu == 2:
            total = cantidad * 3500
        elif menu == 3:
            total = cantidad * 4000
        elif menu == 4:
            total = cantidad * 4500
        elif menu == 5:
            total = cantidad * 5000
        
        # Si se realizó una compra válida, se muestra el total a pagar
        if total > 0:
            print('El total de la compra es de:', total)
    
    # Si el usuario es menor de edad, se muestra un mensaje de restricción
    else:
        print('Lo siento, debes ser mayor de 18 años para comprar bebidas alcohólicas')

# Se verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    run()  # Llamada a la función principal
