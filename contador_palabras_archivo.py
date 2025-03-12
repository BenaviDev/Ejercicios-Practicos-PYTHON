# Solicitar al usuario el nombre del archivo que desea analizar
nombre_archivo = input("Ingresa el nombre del archivo a contar: ")

# Abrir el archivo en modo lectura ('r')
# Se usa 'with open' para asegurar que el archivo se cierre automáticamente después de su uso
with open(nombre_archivo, 'r') as archivo:
    # Leer todo el contenido del archivo
    contenido = archivo.read()
    
    # Contar la cantidad de palabras en el archivo
    # Se utiliza el método split() que divide el texto en palabras basándose en espacios
    cantidad_palabras = len(contenido.split())

# Mostrar el resultado en pantalla
print("El archivo", nombre_archivo, "tiene", cantidad_palabras, "palabras.")
