# Ejercicio 2.2.16
# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

def main():
    while True:
        numero = int(input("Introduce un número: "))
        numero_mayor = numero
        while numero != 0:
            numero = int(input("Introduce otro número: "))
            if numero > numero_mayor:
                numero_mayor = numero

        print(f"El número mayor introducido es: {numero_mayor}")

if __name__ == "__main__":
    main()