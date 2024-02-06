ancho = int(input("Ingrese el ancho "))
alto = int(input("Ingrese el alto "))

if ancho > 0 and alto > 0:
    for x in range(0,alto):
        for y in range(0,ancho):
            print("X",end="")
            if y == 6:
                print("\n")
else:
    print("--INGRESE VALORES POSITIVOS--")            
    