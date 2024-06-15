import math

def areaCirc1(radio):
    res=math.pi*(radio**2)
    return res

def ingreseLado(lado):
    print(lado,end="")
    ladoC=int(input())
    return ladoC

def main():
    num1=int(input("Ingrese el diametro del círculo 1: "))
    num2=int(input("Ingrese el diametro del círculo 2: "))
    num3=int(input("Ingrese el diametro del círculo 3: "))
    area1=areaCirc1(num1/2)
    area2=areaCirc1(num2/2)
    area3=areaCirc1(num3/2)
    print("El area de los 3 círculos es {:4.2f} {:4.2f} y {:4.2f}".format(area1,area2,area3))
    lado=ingreseLado("Ahora ingrese el lado del cuadrado: ")
    areaC=lado**2 
    areaN=areaC-area1-area2-area3
    porAreaN=areaN*100/areaC
    print("El area negra es {:4.2f} y es un {:4.2f}% total del area del cuadrado".format(areaN,porAreaN))
    
main()