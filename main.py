from gpanel import *
from math import *

siz=15
makeGPanel(-siz,siz,-siz,siz)


def commandLine():
    #eingabe = input('')
    eingabe = "vieleck r=2 fill=true n=4"
    
    eingabe = eingabe.split()
    
    if eingabe[0] == "help":
        #printHelp()
        printHelp() 
    elif eingabe[0] == "vieleck":
        vieleck(eingabe)
    elif eingabe[0] == "exit":
        exit(0)
    elif eingabe[0] == "clear_screen":
        clear()
    elif eingabe[0] == "reset":
        clearScreen() 
    else:
        print("Unbekannter Befehl. Gebe help ein für mehr Infos")

def polarToXY(r,theta):
    theta=theta/360*2*pi
    y=r*sin(theta)
    x=r*cos(theta)
    return(x,y)

def innenwinkel(n):
    alpha=180-360/n
    return(alpha)

def printHelp():
    print("
          ")
    commandLine()
    
def vieleck(eingabe):
    r=0
    n=3
    theta=360/n
    
    for e in eingabe:
        par = e.split("=")
        if par[0] == "r":
            r=int(par[1])
        elif par[0] == "n":
            n=int(par[1])
        print(innenwinkel(n))
        
commandLine()