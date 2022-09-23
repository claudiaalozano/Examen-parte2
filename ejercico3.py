
def crear_listas(x):
    
    list(x)
    print(list(x))
    

def multiplos_de_5(x):
    e1 = 0
    e2 = 50
    multiple = 5
    list = []
    i=0
    for i in range(0, 101):
        if multiple(i,5):
            list.append(i)
    return True if e1 and e2 % multiple == 0 else False
        
    

n1= int(input("Introduce el numero:"))
n2 = int(input("Introduce el numero: "))

x = range(n1, n2+1)

print(crear_listas(x))
print(multiplos_de_5(x))




