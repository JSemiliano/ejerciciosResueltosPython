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

if edad <= 0 and edad >= 80:
    print("Ingrese un valor valido")
elif sueldo < 10000:
        descuento = descuento+((PORCENTAJE_DESCUENTO1/100)*sueldo)
elif sueldo < 20000:
        descuento = descuento+((PORCENTAJE_DESCUENTO2/100)*sueldo)   
elif sueldo < 30000:
        descuento = descuento+((PORCENTAJE_DESCUENTO3/100)*sueldo)
else:    
        descuento = descuento+((PORCENTAJE_DESCUENTO4/100)*sueldo)
                               
if edad <= LIMITE_EDAD:
        descuento = descuento+((DESCUENTO_ADICIONAL/100)*descuento)
       
print("El monto a descontar es:",descuento,"dolares")     