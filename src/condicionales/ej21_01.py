# Ejercicio 2.1.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
from utils import *

def es_mayor(edad) -> bool:
    """"""
    if edad >= 18:
        return True
    else:
        return False
    
def anios_validos() -> bool:
    """"""
    while True:
        edad = introducir_int_positivo("Introduce tu edad: ")
        if 1 <= edad <= 100: 
            return edad
        else:
            print("Debes tener entre 1 y 100 años.")



def main():
    """"""
    edad = anios_validos()
    if es_mayor(edad):
        print(f"Tienes {edad} años y eres mayor de edad.")
    print(f"Tienes {edad} años y eres menor de edad.")
    

if __name__ == "__main__":
    main()