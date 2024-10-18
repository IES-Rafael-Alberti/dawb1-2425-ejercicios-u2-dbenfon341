# Ejercicio 2.1.10
# 
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# 
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# 
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
from utils import *

# Listas con ingredientes
ingredientes_vegetarianos = ["Pimiento", "Tofu"]
ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]


INGREDIENTES_DEFAULT =  "Tomate", "Mozzarella"
OPCIONES_VEG = "vegetariana", "veg"
OPCIONES_NO_VEG = "no vegetariana", "no veg"

def preguntar_tipo_pizza(respuesta: int) -> bool:
    # True vegetariano
    # False No vegetariano
    
    if respuesta in OPCIONES_VEG:
        return True
    elif respuesta in OPCIONES_NO_VEG:
        return False
    else:
        return None

def escoger_ingrediente(opcion) -> tuple:
    

    return

def mostrar_pizza(opcion_ingrediente) -> str:
    return

def mostrar_ingredientes_veg():
    print(f"Puedes elegir SOLO UNO de los siguientes ingredientes para tu pizza: ")
    for _ in ingredientes_vegetarianos:
        print(_)

def menu():
    print("Bienvenido a la pizzeria Bella Napoli")
    print("Tenemos dos tipos de pizza: Vegetariana y No vegetariana")
    print(f"TODAS las pizzas de nuestra carta llevan {INGREDIENTES_DEFAULT[0]} y {INGREDIENTES_DEFAULT[1]}.")
    print(f"Las pizzas veganas pueden llevar unos ingredientes u otros")
    print(f"Solo puedes escoger un ingrediente extra para cada tipo de pizza.")


def main():
    clear()
    menu()
    validar_pizza = None
    while validar_pizza is None:
        tipo_de_pizza = input("Introduce el tipo de pizza que deseas: ").strip().lower()
        if preguntar_tipo_pizza(tipo_de_pizza) is True:
            validar_pizza = 1
            clear()
            print("Has escogido una pizza vegetariana")
            mostrar_ingredientes_veg()
        elif preguntar_tipo_pizza(tipo_de_pizza) is False:
            clear()
            print("Has escogido una pizza no vegetariana")
            mostrar_ingredientes_veg()
        else:
            print("Esa pizza no existe.")
            
    



    # print(INGREDIENTES_DEFAULT[1])
    return

if __name__ == "__main__":
    main()