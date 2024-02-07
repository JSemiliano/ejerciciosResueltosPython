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

if numero >= 1 and numero <= 10:
    for x in range(1,11):
        print(f"{numero} x {x} =",(numero*x))
else:
    print("El numero deber ser entre 1 y 10")        