"""
Calculadora de IMC (Índice de Masa Corporal):
Escribe un programa que solicite al usuario su peso (en kilogramos) y su altura (en metros)
y luego calcule y muestre su IMC. La fórmula para calcular el IMC es: IMC = peso / (altura * altura).

"""
def imc ():
    peso = float(input("Ingrese su peso corporal en Kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = (peso / (altura * altura))
    print("Su IMC (Indice de masa corporal) es: ", imc)

    

if __name__ == "__main__":
    imc()