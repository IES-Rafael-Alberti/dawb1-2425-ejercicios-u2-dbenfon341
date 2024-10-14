from os import system, name

# Funcion para validar y introducir enteros
def validar_int(msg: str) -> bool:
   msg = msg.strip()
   return msg.isdigit() or (msg.startswith("-") and msg[1:].isdigit())

def introducir_int(msg: str) -> int:
    msg = input(msg)
    while not validar_int(msg):
        msg = input("Debe ser un número entero: ")
    return int(msg)


# Funcion para validar y introducir enteros
def validar_float(valor: str) -> bool:
    valor = valor.strip()
    if not valor or valor in ['-', '+', '.']:
        return False

    if valor.startswith("-") or valor.startswith("+"):
        valor = valor[1:]

    pos_punto = valor.find(".")
    if valor.count(".") > 1:
        return False

    if pos_punto >= 0:
        if len(valor) == 1:
            return False
        valor = valor[:pos_punto] + valor[pos_punto + 1:]

    return valor.isdigit()

def introducir_float(msg: str) -> float:
    msg = input(msg)
    while not validar_float(msg):
        msg = input("Debe ser un número flotante: ")
    return float(msg)


# Funcion para limpiar la consola
def clear():
    if name == 'nt':
        _ = system('cls')