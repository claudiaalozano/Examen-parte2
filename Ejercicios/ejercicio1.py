
matriz = [

    [1, 1, 1, 3],

    [2, 2, 2, 7],

    [3, 3, 3, 9],

    [4, 4, 4, 13]

]


def sum1(n):
    sumita= v1 + v2 + v3 
    if sumita == v4:
        print("El resultado es correcto, los tres primeros elementos sumados son igual al cuarto.")
    else:
        print("La suma de los tres primeros elementos no es igual al cuarto.")



n= int(input("Introduce el valor de la fila que quieres analizar de la matriz (0-3): "))
v1 = matriz[n][0]
v2 = matriz[n][1]
v3 = matriz[n][2]
v4 = matriz[n][3]

print(sum1(n))