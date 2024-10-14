# Ejercicio 2.1.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
from src.utils import *

def es_mayor(edad) -> bool:
    if edad >= 18:
        return True
    else:
        return False
    
def anios_validos(edad) -> bool:
    while edad > 0 or edad < 100:
        print("Tu edad debe estar entre 0 y 100.")



def main():
    edad = introducir_int("Introduce tu edad: ")
    return

if __name__ == "__main__":
    main()