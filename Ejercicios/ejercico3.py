
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
