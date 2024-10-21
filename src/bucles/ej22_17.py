# Ejercicio 2.2.17
# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

def main():
    numero = int(input("Introduce un numero"))

    numero_completo = 0
    for i in range(numero):
        numero_completo += i

    print(numero_completo)

if __name__ == "__main__":
    main()