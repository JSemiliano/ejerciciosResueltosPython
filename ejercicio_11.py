nombre = input("Ingrese un nombre ")
edad = int(input("Ingrese la edad "))

min_edad=0
while nombre != "*":
    if min_edad == 0: 
        min_edad = edad
        mas_joven = nombre
    elif edad < min_edad:
        min_edad = edad
        mas_joven = nombre

    nombre = input("Ingrese un nombre ")
    if nombre != "*":
        edad = int(input("Ingrese la edad "))

print("---La persona mas joven es "+mas_joven+"---")        

