CARACTER ="*"
CARACTER = "*"
ESPACIO = " "
base = int(input("Ingrese un la base (impar o mayor a 1): "))

while not (base > 1 and base % 2 != 0):
    base = int(input("ERROR: Ingrese un la base (impar o mayor a 1): "))

espacios_iniciales = base // 2

for cont_caracteres in range(1,base+1,2):
    for cont_espacios in range(espacios_iniciales):
        print(ESPACIO,end="")
    espacios_iniciales -= 1
    for col in range(cont_caracteres):
        print(CARACTER,end="")
    print() 


            

                             


    
