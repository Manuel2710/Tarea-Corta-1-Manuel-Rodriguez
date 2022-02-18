from Ficha import *
from Dado import *

class Tablero:

    #Defina aquí los atributos de Tablero
    Turno=0
    Casillas=0
    Jugadores=0
    Fichas=[(1,0),(2,0),(3,0),(4,0),(5,0)]#Jugador,posición

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno
    if Turno == 0 or Turno==5:
        Turno = 1
    elif Turno == 1:
        Turno = 2
    elif Turno == 2:
        Turno = 3
    elif Turno == 3:
        Turno = 4
    elif Turno == 4:
        Turno = 5

    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self,Turno,NumCasillas,CantJugadores):
        #inicialice aquí todos los atributos
        self.Turno = Turno
        self.Casillas = NumCasillas
        self.Jugadores = CantJugadores
        #no olvide usar self.atributo para acceder el atributo de la clase


    #defina aquí los métodos de Tablero
    def posicionTodas(self,Fichas):
    #recuerde que el primer parámetro de cada método es siempre self 
        Fichas[Turno-1][1] = self.posicion()
        print(self.Orden)
        #Movimiento














        
