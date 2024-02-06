numero = int(input("Ingrese un número positivo "))

#cont=1
#Lo hice con un while porque todavia no me se la 
#sintaxis de FOR en python y se me corto el wifi,
#cuando vuelva lo hago con un for.
#if numero > 0:
    #while cont <= 10 and cont > 0:
        #tabla = numero * cont
        #print(tabla)
        #cont = cont + 1
#else:
    #print("El número debe ser positivo te dije, que parte no entendes?")  

if numero > 0:
    for x in range(1,11):
        print(numero*x)
else:
    print("El número debe ser positivo te dije, que parte no entendes?")        