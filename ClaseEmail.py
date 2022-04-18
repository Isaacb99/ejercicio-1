import menu

class Email:
    __idCuenta= str
    __dominio= str
    __tipoDominio= str
    __contrasena= str
    def __init__ (self,cuenta=None,dominio=None,tDominio=None,cont=None):
        self.__idCuenta= cuenta
        self.__dominio= dominio
        self.__tipoDominio= tDominio
        self.__contrasena= cont
    def retornaMail(self):
        return (self.__idCuenta +'@'+ self.__dominio +'.'+ self.__tipoDominio)
    def getDominio(self):
        return (self.__dominio)
    def crearCuenta(self,correo,cont):
        if (correo.find('@')!= -1):
            auxCorreo= correo.split('@')
            user= auxCorreo[0]
            if (auxCorreo[1].find('.')!= -1):
                domCompleto= auxCorreo[1].split('.')
                auxDominio= domCompleto[0]
                auxTipoDominio= domCompleto[1]
                self.__init__(user,auxDominio,auxTipoDominio,cont)
                print('Correo creado con exito')
            else: print('Error: El dominio no contiene punto')
        else: print ('Error: El correo ingresado no contiene @')
    def modificaCont (self):
        aux= input('Ingrese su contrasena: ')
        while self.__contrasena != aux:
            aux= input('Contrasena incorrecta, intente nuevamente: ')
        self.__contrasena= input('Ingrese su nueva contrasena: ')
    
        

