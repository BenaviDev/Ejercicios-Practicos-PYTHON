def conver():
    try:
        response = float(input("Ingrese los grados fahren: "))
        cels = (response - 32.0) * 5.0 / 9.0
        print(cels)

    except:
        print("ingresa un numero valido")


if __name__ == "__main__":
    conver()
