LIMITE_INFERIOR = 0
LIMITE_MADRUGADA = 5
LIMITE_MANIANA = 11
LIMITE_MEDIODIA = 13
LIMITE_TARDE = 19
LIMITE_SUPERIOR = 23

hora=int(input("Ingrese un horario entre: "+str(LIMITE_INFERIOR)+" y "+str(LIMITE_SUPERIOR)+" "))

if hora < LIMITE_INFERIOR:
	print("La hora no puede ser negativa")
elif hora > LIMITE_SUPERIOR: 
	print("La hora no puede ser mayor que",LIMITE_SUPERIOR)
elif hora <= LIMITE_MADRUGADA:
    print("Madrugada")
elif hora <= LIMITE_MANIANA:
    print("Mañana")
elif hora <= LIMITE_MEDIODIA:
    print("Mediodia")
elif hora <= LIMITE_TARDE:
    print("Tarde")
else:
    print("Es de noche.")                
