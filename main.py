from gturtle import *
from math import *

makeTurtle()

def commandLine():
    eingabe=getEingabe()
    while eingabe[0] != "exit":
        eingabe=getEingabe()
        if eingabe[0] == "help":
            printHelp(eingabe) 
        elif eingabe[0] == "vieleck":
            vieleck(eingabe)
        elif eingabe[0] == "clear_screen":
            clear()
        elif eingabe[0] == "reset":
            clearScreen() 
        else:
            print("Unbekannter Befehl. Gebe help ein für mehr Infos")
    exit("Programm beendet...")

def getEingabe():
    eingabe = input("")
    #eingabe = "vieleck r=20 n=6"
    eingabe = eingabe.split()
    return(eingabe)

def polarToXY(r,theta):
    theta=theta/360*2*pi
    y=r*sin(theta)
    x=r*cos(theta)
    return(x,y)

def innenwinkel(n):
    alpha=180-360/n
    return(alpha)

def printHelp(eingabe):
    if len(eingabe) == 1: #Bug: es wird nicht geprintet
        print("Möglich befehle: help, vieleck, exit, clear_screen, reset. Für mehr Infos schreibe z.B. help reset um mehr Infos zu reset befehl zubekommen")
        return()#return to commandLine()
    else:
        if eingabe[1] == "help":
            print("help druck die Hilfe.") 
        elif eingabe[1] == "vieleck":
            print("vieleck") 
        elif eingabe[1] == "exit":
            print("exit")
        elif eingabe[1] == "clear_screen":
            print("clear_screen")
        elif eingabe[1] == "reset":
            print("reset") 
        else:
            print("Unbekannter Befehl. Gebe help ein für mehr Infos")
    return()#return to commandLine()
    
def vieleck(eingabe):
    r=3
    n=3
    s=3
    startPos=getPos()
    
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
    rt(alpha)
    fd(s/2)
    rt(alpha)
    repeat n-1:
        fd(s)
        rt(alpha)
    fd(s/2)









commandLine()