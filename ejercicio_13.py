USUARIO = "emi"
CONTRA = "solis"

usuario = input("Ingrese el usuario ")
contraseña = input("Ingrese la contraseña ")

cont = 1

while cont < 3:
    if usuario == USUARIO and contraseña == CONTRA:
        print("Acceso concedido")
        cont = 3
    else:
        print("-------------------")
        print("Credenciales invalidas")
        print("Vuelva a ingresar las credenciales")
        print("-------------------")
        usuario = input("Ingrese el usuario ")
        contraseña = input("Ingrese la contraseña ")
        cont = cont + 1
        intentos = cont
        if intentos == 3:
            ("-------------------")
            print("Cuenta bloqueada")
