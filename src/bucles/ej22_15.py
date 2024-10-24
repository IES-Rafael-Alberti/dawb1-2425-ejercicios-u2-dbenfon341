# Ejercicio 2.2.15
# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
from utils import *

def sumar_numeros_enteros():
    suma_total = 0

    while True:
        numero = pedir_num("Introduce un número (0 para salir): ")
        if numero == 0:
            return suma_total

        if numero > 0:
            suma_total += numero

def mostrar_sumatoria(sumatoria):
    return f"La sumatoria total de números es de {sumatoria}."

def main():
    sumatoria = sumar_numeros_enteros()

    print(mostrar_sumatoria(sumatoria))

if __name__ == "__main__":
    main()
