    #Desarrollar un algoritmo que permita ingresar la edad y el sueldo
    #anual en dólares de un empleado.La computadora debe mostrar el monto
    #del aporte al sindicato que se debe descontar del salario del empleado

PORCENTAJE_DESCUENTO1=0.5
PORCENTAJE_DESCUENTO2=1
PORCENTAJE_DESCUENTO3=2
PORCENTAJE_DESCUENTO4=2.5
DESCUENTO_ADICIONAL=20

LIMITE_EDAD=30
descuento=0

edad=int(input("Ingrese la edad "))
sueldo=float(input("Ingrese el sueldo "))

if edad<=0 and edad >=100:
    print("Ingrese un valor valido")

elif sueldo < 10000:
    if edad>LIMITE_EDAD:
        descuento = descuento+((PORCENTAJE_DESCUENTO1/100)*sueldo)
        print("El monto a descontar es:",descuento,"dolares")
    elif edad<=LIMITE_EDAD:
        descuento = descuento+((PORCENTAJE_DESCUENTO1/100)*sueldo)
        descuento = descuento+((DESCUENTO_ADICIONAL/100)*descuento)
        print("El monto a descontar es:",descuento,"dolares")
elif sueldo < 20000:
    if edad>LIMITE_EDAD:
        descuento = descuento+((PORCENTAJE_DESCUENTO2/100)*sueldo)
        print("El monto a descontar es:",descuento,"dolares")
    elif edad<=LIMITE_EDAD:
        descuento = descuento+((PORCENTAJE_DESCUENTO2/100)*sueldo)
        descuento = descuento+((DESCUENTO_ADICIONAL/100)*descuento)
        print("El monto a descontar es:",descuento,"dolares")
elif sueldo < 30000:
    if edad>LIMITE_EDAD:
        descuento = descuento+((PORCENTAJE_DESCUENTO3/100)*sueldo)
        print("El monto a descontar es:",descuento,"dolares")
    elif edad<=LIMITE_EDAD:
        descuento = descuento+((PORCENTAJE_DESCUENTO3/100)*sueldo)
        descuento = descuento+((DESCUENTO_ADICIONAL/100)*descuento)
        print("El monto a descontar es:",descuento,"dolares")
else:
    if edad>LIMITE_EDAD:
        descuento = descuento+((PORCENTAJE_DESCUENTO4/100)*sueldo)
        print("El monto a descontar es:",descuento,"dolares")
    elif edad<=LIMITE_EDAD:
        descuento = descuento+((PORCENTAJE_DESCUENTO4/100)*sueldo)
        descuento = descuento+((DESCUENTO_ADICIONAL/100)*descuento)
        print("El monto a descontar es:",descuento,"dolares")                        
    