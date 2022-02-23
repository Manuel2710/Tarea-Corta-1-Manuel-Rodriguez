from Fichas import *
from Dado import *

class Tablero:

    #Defina aquí los atributos de Tablero
    nombre = ""
    Casillas=0
    Turno = 0
    Jugadores=0
    Orden = [(0),(0),(0),(0)]
    Fichas=[]#Jugador,posición

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno

    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self,nombrejuego,NumCasillas):
        #inicialice aquí todos los atributos
        self.nombre = nombrejuego
        self.Turno = Turno
        self.Casillas = NumCasillas
        self.Jugadores = 4
        self.Fichas = [Azul,Verde,Amarillo,Rojo]
        #no olvide usar self.atributo para acceder el atributo de la clase


    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self 
        

    def Turnos_Todos(self):
        if self.Turno == 0 or self.Turno==4:
            self.Turno = 1
        elif self.Turno == 1:
            self.Turno = 2
        elif self.Turno == 2:
            self.Turno = 3
        elif self.Turno == 3:
            self.Turno = 4
        
        print ("Ahora le toca a", self.Jugadores[self.Turno-1].color)

    def turno_individual(self):
        self.jugadores[i].avanzar()
        if self.jugadores[i].posicion >= self.Casillas:
            print("El jugador", self.jugadores[i].color,"ha gando")
            return True
        else:
            return False

    def Orden_Fichas(self):
        self.Orden[self.Turno-1] += self.posicion()
        print("El Azul va en la casilla"self.Orden[0])
        print("El Verde va en la casilla"self.Orden[1])
        print("El Amarillo va en la casilla"self.Orden[2])
        print("El Rojo va en la casilla"self.Orden[3])













        
