# Examen-parte2

Mi dirección de GitHub: https://github.com/claudiaalozano/Examen-parte2.git

### Ejercicio 1

La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

Ayuda

La función llamada sum(lista) devuelve una suma de todos los elementos de la lista ¡Pruébalo!

matriz = [

    [1, 1, 1, 3],

    [2, 2, 2, 7],

    [3, 3, 3, 9],

    [4, 4, 4, 13]

]

El código empleado es:

```

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
```

###Ejercicio 2

Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

El código empleado es:

```
cadena_de_texto= input("Introduce una cadena de texto: ")

def get_cadena(cadena_de_texto):
    
    if len(cadena_de_texto)>=3 and len(cadena_de_texto)<10:
        print("correcto.")
    else:
        print("No cumple con las condiciones.")



get_cadena(cadena_de_texto)
```

###Ejercicio 3

Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

·        Todos los números del 0 al 10 [0, 1, 2, ..., 10]

·        Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

·        Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

·        Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

·        Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

Concepto útil

Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto), experimenta.

El código empleado es:

```

def crear_listas(x):
    
    list(x)
    print(list(x))
    

def multiplos_de_5(y):
   
    lista = []
    start_num= int(0)
    end_num= int(50)
    cnt= start_num

    while cnt <= end_num:
        cnt +=1
        if cnt % 5 == 0:
            lista.append(cnt)
    print(lista)
        
    
    
    #if y % 5 == 0:
        #lista.append(y)
        #print(lista)
    #return True if e1 and e2 % multiple == 0 else False
        
def impares(z):
    lista = []
    start_num= int(-20)
    end_num= int(-1)
    cnt= start_num

    while cnt <= end_num:
        cnt +=1
        if cnt % 2 != 0:
            lista.append(cnt)
    print(lista)

def negativo(t):
    
    list(t)
    print(list(t))

def pares(w):
    lista = []
    start_num= int(0)
    end_num= int(20)
    cnt= start_num

    while cnt <= end_num:
        cnt +=1
        if cnt % 2 == 0:
            lista.append(cnt)
    print(lista)
x = range(0, 11)
y= range (0,51)
z = range(-20, 0)
t= range (-10, 1)
w= range (0,21)
print(crear_listas(x))
print(multiplos_de_5(y))
print(impares(z))
print(negativo(t))
print(pares(w))
```

###Ejercicio 4

Crea un script llamado tabla.py que realice las siguientes tareas:

·        Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.

·        El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.

·        En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.

·        El script contendrá un bucle for que itere el número de veces del primer argumento.

·        Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.

·        Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.

·        Ejecuta el código y observa el resultado.

·        Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.

El código empleado es:

```
n = int (input("Introduce el valor de las dimensiones: "))

def crear (n):
    tabla = []
    estrella = "*"
    for r in range(n):
        fila = []

        for t in range (n):
            fila.append(estrella)
        
        tabla.append(fila)
    return tabla
    #i=0
    #lista = []
    #estrella = "*"
    #list = [lista for i in range(n)]
    #list.append(n*estrella)
    #print(list)

print(crear(n))
```
