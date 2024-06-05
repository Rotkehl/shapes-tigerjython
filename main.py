from gturtle import *
from math import *

makeTurtle()

def commandLine():
    eingabe=getEingabe()
    e0 = eingabe[0]
    while not(e0 == "exit" or e0 == "ex" ): 
        if e0 == "help" or e0 == "h" or e0 == "he":
            printHelp(eingabe) 
        elif e0 == "vieleck" or e0 == "vi":
            vieleck(eingabe)
        elif e0 == "clear" or e0 == "cl":
            clear()
        elif e0 == "reset" or e0 == "re":
            clearScreen()
        elif e0 == "set" or e0 == "se":
            set(eingabe)
        else:
            print("Unbekannter Befehl. Gebe help ein für mehr Infos:", eingabe)
        eingabe=getEingabe()
        e0 = eingabe[0]
    exit("Programm beendet...")

def getEingabe():
    eingabe = input("")
    while eingabe=="":
        eingabe = input("")
        print("Benutze den help Befehl um mehr zu erfahren!")
    #eingabe = "vieleck r=100 n=5"
    eingabe = eingabe.split()
    return(eingabe)

def polarToXY(r,theta):
    theta=theta/360*2*pi
    y=r*sin(theta)
    x=r*cos(theta)
    return(x,y)

def innenwinkel(n):
    alpha=360/n
    return(alpha)

def printHelp(eingabe):
    if len(eingabe) == 1:
        print("Möglich Befehle: help, vieleck, exit, clear, reset, set. Für mehr Infos schreibe z.B. help reset um mehr Infos zu reset befehl zubekommen.\n Tipp: Du kannst auch immer nur die ersten 2 Buchstaben von einen Command nehmen.")
        return()#return to commandLine()
    else:
        if eingabe[1] == "help":
            print("help druck die Hilfe.") 
        elif eingabe[1] == "vieleck":
            print("Mit vieleck kannst du ein symetrisches Vieleck zeichnen. Parameter sind r für den Ausenradius und n für die Anzahl an Kanten.") 
        elif eingabe[1] == "exit":
            print("Der Befehl exit beendet das Programm.")
        elif eingabe[1] == "clear":
            print("Löscht alles was gezeichnet wurde")
        elif eingabe[1] == "reset":
            print("Löscht alles was gezeichnet wurde und set die Turtle wider auf die Startposition.") 
        elif eingabe[1] == "set":
            print("Set werte der Turtle. Position setzen: set pos x y (x und y sind hier variabel und müssen besetzt werden.),\n set angle α  (α ist hier eine variabel und must besetzt werden.)") 
        else:
            print("Unbekannter Befehl. Gebe help ein für mehr Infos")
    return()#return to commandLine()
    
def vieleck(eingabe):
    r=100
    n=6
    s=3
    startPos=getPos()
    startAngle=heading()

    for e in eingabe:
        par = e.split("=")
        if par[0] == "r":
            r=abs(int(par[1]))
        elif par[0] == "n":
            n=abs(int(par[1])) #abs damit der int postiv ist
    s=2*r*sin(pi/n) #formle für kantenlänge
    alpha=innenwinkel(n)
    pu()
    fd(r)
    pd()
    rt(90)
    fd(s/2)
    rt(alpha)
    repeat n-1:
        fd(s)
        rt(alpha)
    fd(s/2)
    setPos(startPos)
    setHeading(startAngle)
    return()

def set(eingabe):
    if len(eingabe) == 1:
        print("Ungültiger Befehl. Sehe help")
        return()
    else:
        if eingabe[1] == "pos":
            if len(eingabe) == 4:
                setPos(int(eingabe[2]), int(eingabe[3])) 
            else:
                print("Ungültiger Befehl! Du musst 2 Koordinaten eingeben x y.")
                return()
        elif eingabe[1] == "angle":
            if len(eingabe) == 3:
                setHeading(int(eingabe[2]))
            else:
                print("Ungültiger Befehl! Du musst einen Winkel eingeben.")
                return()
    return()

# hideTurtle()

repeat 2: #Damit das Fenster nicht den output überlappt.
    print("\n")

commandLine()
