numero = int(input("Ingrese un numero "))

while numero <= 0:
    print("-El numero debe ser positivo-")
    numero = int(input("Ingrese un numero "))

bandera = numero
for x in range(0,numero):
    bandera = bandera - 1
    if bandera > 0:
        numero = numero * bandera
print(numero) 
       
                 