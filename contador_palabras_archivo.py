nombre_archivo = input("Ingresa el nombre del archivo a contar: ")

with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    cantidad_palabras = len(contenido.split())

print("El archivo", nombre_archivo, "tiene", cantidad_palabras, "palabras.")
