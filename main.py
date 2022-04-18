import csv
from menu import Menu
from ClaseEmail import Email
import os

def test () :
    print('------ TEST ------')
    print('datos a probar: \nDatos correctos: \ninformatica.fcefn@gmail.com, wicc2019@unsj-cuim.edu, juanLiendro1957@yahoo.com \n\nDatos incorrectos: \njulio3312gmail.com, ernesto@yahoo')
    nuevotest= Email()
    print('\n\n--- DATOS CORRECTOS')
    print('informatica.fcefn@gmail.com')
    nuevotest.crearCuenta('informatica.fcefn@gmail.com','contrasena1')
    print('wicc2019@unsj-cuim.edu')
    nuevotest.crearCuenta('wicc2019@unsj-cuim.edu','contrasena2')
    print('juanLiendro1957@yahoo.com')
    nuevotest.crearCuenta('juanLiendro1957@yahoo.com','contrasena3')
    print('\n--- DATOS INCORRECTOS')
    print('julio3312gmail.com')
    nuevotest.crearCuenta('julio3312gmail.com','contrasena4')
    print('ernesto@yahoo')
    nuevotest.crearCuenta('ernesto@yahoo','contrasena5')
    os.system('Pause')
    os.system('cls')


if __name__ == '__main__':
    
    op=int (input('Desea ejecutar el test? \n 1 - SI \n 2 - NO\n'))
    if op==1:
        test()
    nuevoMail= Email()
    xmenu=Menu()
    b=False
    while not b:
        print('----------- MENU')
        op= int(input('Ingrese la opcion:\n1- Ingresar el nombre de una persona y su dirección de e-mail\n2- Cambiar la contrasena de la cuenta creada anteriormente\n3- Leer de un archivo\n4- Salir\n'))
        if op != 4:
            xmenu.manejoMenu(op,nuevoMail)
        else:
            b= True