cadena_de_texto= input("Introduce una cadena de texto: ")

def get_cadena(cadena_de_texto):
    
    if len(cadena_de_texto)>=3 and len(cadena_de_texto)<10:
        print("correcto.")
    else:
        print("No cumple con las condiciones.")



get_cadena(cadena_de_texto)