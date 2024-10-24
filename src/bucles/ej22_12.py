# Ejercicio 2.2.12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def main():

    palabra = "ejercicio"
    
    cont = 0
    for letras in palabra:
        cont += 1
    
    print (cont)


if __name__ == "__main__":
    main()