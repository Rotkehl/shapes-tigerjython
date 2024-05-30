from gturtle import *
from math import *

makeTurtle()

def commandLine():
    eingabe=getEingabe()
    while eingabe[0] != "exit":
        if eingabe[0] == "help" or "h" or "he":
            printHelp(eingabe) 
        elif eingabe[0] == "vieleck" or "vi":
            vieleck(eingabe)
        elif eingabe[0] == "clear" or "cl":
            clear()
        elif eingabe[0] == "reset" or "re":
            clearScreen()
        elif eingabe[0] == "set" or "se":
            set(eingabe)
        else:
            print("Unbekannter Befehl. Gebe help ein für mehr Infos")
        eingabe=getEingabe()
    exit("Programm beendet...")

def getEingabe():
    eingabe = input("")
    while eingabe=="":
        eingabe = input("")
        print("Benutze den help Befehl um mehrzuerfahren!")
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
    r=3
    n=3
    s=3
    startPos=getPos()
    startAngel=heading()

    for e in eingabe:
        par = e.split("=")
        if par[0] == "r":
            r=int(par[1])
        elif par[0] == "n":
            n=int(par[1])
    s=2*r*sin(pi/n)
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
    setHeading(startAngel)
    return()

def set(eingabe):
    if len(eingabe) == 1:
        print("Ungültiger Befehl. Sehe help")
        return()
    else:
        #out of range bug on whole if statement
        if eingabe[1] == "pos": 
            setPos(int(eingabe[2]), int(eingabe[3])) 
        elif eingabe[1] == "angle":
            setHeading(int(eingabe[2]))
    return()



repeat 2: #Damit das Fenster nicht den output überlappt.
    print("\n")

commandLine()