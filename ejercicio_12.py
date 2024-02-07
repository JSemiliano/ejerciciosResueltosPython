ancho = int(input("Ingrese el ancho "))
alto = int(input("Ingrese el alto "))

while ancho and alto < 0:
    print("--INGRESE VALORES POSITIVOS--")
    ancho = int(input("Ingrese el ancho: "))
    alto = int(input("Ingrese el alto: "))

for x in range(alto):
    for y in range(ancho):
        print("X",end="")
    print()            
            
    