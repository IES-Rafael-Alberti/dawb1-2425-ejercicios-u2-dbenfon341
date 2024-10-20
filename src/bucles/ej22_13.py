# Ejercicio 2.2.13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
frase = ""
palabra = ""
while palabra != "fin":
    palabra = input("Introduce una palabra: ")
    frase += (f" {palabra}")
    print(frase.strip())


def main():
    return

if __name__ == "__main__":
    main()