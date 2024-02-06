numero = int(input("Ingrese un numero "))

bandera = numero
if numero > 0:
    for x in range(0,numero):
        bandera = bandera - 1
        if bandera > 0:
            numero = numero * bandera
    print(numero) 
else:
    print("--El numero debe ser positivo--")           
                 