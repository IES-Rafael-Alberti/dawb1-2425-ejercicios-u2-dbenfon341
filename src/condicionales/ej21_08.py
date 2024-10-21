# Ejercicio 2.1.8
# 
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
# Nivel 	Puntuación
# Inaceptable 	0.0
# Aceptable 	0.4
# Meritorio 	0.6 o más
# 
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

puntuacion = 2400

niveles_validos = [0.0, 0.4, 0.6]

inaceptable = 0
aceptable = 0.4
meritorio = 0.6

def calcular_rendimiento(puntuacion: int):
    if puntuacion == inaceptable:
        puntuacion = puntuacion * inaceptable
        return puntuacion, inaceptable
    return





def mostrar_rendimiento() -> str:
    return


def main():
    return

if __name__ == "__main__":
    main()