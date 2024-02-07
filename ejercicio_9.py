personas = int(input("Ingrese la cantidad de personas: "))

#cont_per = personas
cont = 0
porcentaje = 0
'''
Lo hice con un while porque todavia no me se la 
sintaxis de FOR en python y se me corto el wifi,
cuando vuelva lo hago con un for.
while cont_per > 0:
'''
    #edad = int(input("Ingrese la edad "))
    #if edad >=18:
        #cont = cont + 1
    #elif edad < 0:
        #print("Edad invalida")
    #cont_per = cont_per - 1

#porcentaje = porcentaje+((cont*100)/personas)
#porcentaje = porcentaje+((cont/100)*personas)
#print("El porcentaje de personas mayores de 18 años es: ",str(porcentaje)+"%")


for x in range(0,personas):
    edad = int(input("Ingrese la edad "))
    if edad >=18:
        cont = cont + 1
    elif edad < 0:
        personas = personas - 1
        print("Edad invalida")

porcentaje = porcentaje+((cont*100)/personas)
#porcentaje = porcentaje+((cont/100)*personas)
print("El porcentaje de personas mayores de 18 años es: ",str(porcentaje)+"%")        

