from ClaseEmail import Email
import csv
import os


class Menu :
    __op= int
    def __init__ (self):
        self.__op=None
    def getOpcion (self):
        return self.__op
    def manejoMenu (self,op,auxCorreo):
        if op == 1:
            self.opcion1(auxCorreo)
        elif op == 2:
            self.opcion2(auxCorreo)
        elif op == 3:
            self.opcion3()
        else:
            self.Salir()

    def opcion1 (self,auxCorreo):
        print("Procederemos a ingresar su direccion de e-mail")
        nom=input('Ingrese su nombre: ')
        correo=input('Ingrese su nuevo correo: ')
        contrasena=input('Ingrese su contrasena: ')
        auxCorreo.crearCuenta(correo,contrasena)
        print("Estimado {} te enviaremos tus mensajes a la dirección {}".format(nom,auxCorreo.retornaMail()))
        
    def opcion2 (self,auxCorreo):
        print()
        print('--------- CAMBIO DE CONTRASENA')
        auxCorreo.modificaCont()
        os.system('pause')
        os.system('cls')
        
    def opcion3 (self):
        cont = 0
        path_archivo='Actividad1\Correos.csv'
        archivo = open(path_archivo,"r")
        reader = csv.reader(archivo,delimiter=',')
        id=input('Ingrese identificador a buscar: ')
        for fila in reader:
            if fila[0] == id:
                cont += 1
        print("La cantidad de personas con el identificador '{}' es: {}".format(id,cont))
        if cont > 1:
            print("El identificador se repite")
        else:
            print("El identificador no se repite")
        archivo.close()
        os.system('pause')
        os.system('cls')
        
    def Salir(self):
        print('Salir')
        os.system('Pause')
