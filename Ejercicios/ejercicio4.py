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