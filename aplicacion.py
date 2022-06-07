def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido 

usuario = leer_archivo('usuario.txt')
contraseña = leer_archivo('claves.txt')

contador=1

def menu():
     print("* MENU PRINCIPAL *")
     print("1. Listar")
     print("2. Agregar")
     print("3. Salir")

def validar():
    dato1 = input('ingrese usuario: ')
    dato2 = input('ingrese la clave: ')
    if usuario == dato1 and contraseña == dato2:
             return menu()
               
    else:
         while contador < 3:
            print("vuelva a ingresar los datos")
            contador == contador+1
            return validar()
validar()