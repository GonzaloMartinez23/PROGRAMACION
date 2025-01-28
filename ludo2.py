import random 
import os

def resultado():
    return random.randint(1,6)
def jug():
    return random.randint(1,cantjugadores)

cantjugadores=int(input("Ingrese la cantidad de jugadores (2 a 4)"))

if cantjugadores==2:
    print("Bienvenidos jugador1 y jugador 2")
    start=(input("Desea comenzar el juego"))
    if start=="s":
        os.system("cls")
        print("Comience el juego")
        print("Lancen los dados")
        input("presione enter")
        jugador=(jug())
        while True:
            if jugador==1:
                print("Turno:Jugador 1, lance los dados")
                input("presione enter")
                os.system("cls")
                print("Su resultado es",resultado)
                
           
            if jugador==2:
                print("Turno:Jugador 2, lance los dados")
                input("presione enter")
                os.system("cls")
                print("Su resultado es",resultado)
                
        