#Ingresa 20m, 14m y USD1200, debe devolver USD336000 y 204 metros de alambre.

#INGRESO
ancho = int(input("Ingrese el ancho del terreno: "))
largo = int(input("Ingrese el alto del terreno: "))
precio_m2 = float(input("Ingrese el precio del terreno: "))

pasadas = 3
#PROCESO
superficie = ancho * largo
precio_terreno = superficie * precio_m2

perimetro = 2 * ancho + 2 * largo
metros_de_alambre = perimetro * pasadas
#SALIDA
print("--Precio del terreno:",precio_terreno,"\n" "--Metros de alambre para cercar el terreno:",metros_de_alambre)
