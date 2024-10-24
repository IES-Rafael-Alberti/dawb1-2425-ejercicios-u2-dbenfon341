# Ejercicio 2.2.11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def main():

    palabra = "ejercicio"

    for letras in reversed(palabra):
        print (letras)

    for letras in palabra[::-1]:
        print (letras)

if __name__ == "__main__":
    main()