class Punto:
    __x=0
    __y=0
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def setX(self, v):
        self.__x = v
    def getX(self):
        return self.__x
    def setY(sel, v):
        sel.__y = v
    def getY(self):
        return self.__y
    def mostrarDatos(self):
        print("(x,y) = (",self.__x,",",self.__y,")")

if __name__ == '__main__':
    unPunto = Punto(3,4)
    otroPunto = Punto(4)
    unPunto.mostrarDatos()
    otroPunto.mostrarDatos()
    tercerPunto = Punto() 
    tercerPunto.mostrarDatos()   
