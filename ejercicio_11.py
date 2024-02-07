
CORTE = "*"
NOMBRE_INVALIDO = "XXXXXX"
mas_joven = NOMBRE_INVALIDO
nombre = input(f"Ingrese un nombre ({CORTE} para cortar) ")

min_edad=0
while nombre != CORTE:
    edad = int(input("Ingrese la edad: "))
    if min_edad == 0: 
        min_edad = edad
        mas_joven = nombre
    elif edad < min_edad:
        min_edad = edad
        mas_joven = nombre

    nombre = input(f"Ingrese un nombre ({CORTE} para cortar) ")
    

if mas_joven == NOMBRE_INVALIDO:
        print("No se ingresaron personas")
else:        
    print(f"---La persona mas joven es {mas_joven}---")
    
        

