USUARIO = "emi"
CONTRA = "solis"
INTENTOS_MAX = 3
usuario = input("Ingrese el usuario ")
contraseña = input("Ingrese la contraseña ")
intentos = 1

while not (usuario == USUARIO and contraseña == CONTRA) and intentos < INTENTOS_MAX:
    print("Credenciales invalidas")
    usuario = input("Ingrese el usuario ")
    contraseña = input("Ingrese la contraseña ")
    intentos +=1

if usuario == USUARIO and contraseña == CONTRA:
    print("¡Acceso consedido!") 
else:
    print("¡Cuenta bloqueada!")       


    