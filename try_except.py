
"""
Esta función convierte grados Fahrenheit a grados Celsius.

Funcionamiento:
1. Se solicita al usuario que ingrese una temperatura en grados Fahrenheit.
2. Se convierte la entrada a un número decimal (`float`).
3. Se aplica la fórmula de conversión: `C = (F - 32) * 5/9`.
4. Se imprime el resultado en pantalla.
5. Si la entrada no es un número válido, se muestra un mensaje de error.
"""

def conver():
    try:
        response = float(input("Ingrese los grados Fahrenheit: "))  # Solicita la temperatura al usuario y la convierte a float
        cels = (response - 32.0) * 5.0 / 9.0  # Aplica la fórmula de conversión
        print(cels)  # Muestra el resultado en pantalla
    except:
        print("Ingresa un número válido")  # Captura errores si el usuario ingresa un valor no numérico

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    conver()  # Llama a la función de conversión
