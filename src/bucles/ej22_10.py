# Ejercicio 2.2.10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
from utils import *

def validar_primo(num) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():

    num = pedir_num("Introduce un número: ")

    if validar_primo(num):
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")

if __name__ == "__main__":
    main()