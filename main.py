
from webbrowser import get
from Ejercicios import *
if __name__ == '__main__':
    ejercicio= int(input("¿Que ejercicio desea ejecutar (1,2,3 o 4): "))

    if ejercicio == 1:
        from Ejercicios.ejercicio1 import *
        ejecutar = sum1()
        print(ejecutar)
    if ejercicio == 2:
        from Ejercicios.ejercicio2 import *
        ejecutar = get_cadena
        print(ejecutar)
    if ejercicio == 3:
        from Ejercicios.ejercico3 import *
        ejecutar = (pares(),impares(),negativo(), multiplos_de_5(), crear_listas() )
        print(ejecutar)
    if ejercicio == 4:
        from Ejercicios.ejercicio4 import *
        ejecutar= crear()
        print(ejecutar)


