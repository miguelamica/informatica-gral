import math

def areaCirc(diametro):
    areaC=math.pi*((diametro/2)**2)
    return areaC

def areaTri(base,altura):
    areaT=(base*altura)/2
    return areaT

def areaColor(letraColor,d):
    if letraColor=="g":
        area=areaCirc(d)-areaCirc(d/3)-areaTri((d/3),(d/3))-areaTri((d/3),(d/3))-areaTri((d/3),(d/6))-areaTri((d/3),(d/6))
        rta="El area gris es {:4.2f}".format(area)
    if letraColor=="n":
        area=areaTri((d/3),(d/3))+areaTri((d/3),(d/3))+areaTri((d/3),(d/6))
        rta="El area negra es {:4.2f}".format(area)
    if letraColor=="v":
        area=areaCirc(d/3)+areaTri((d/3),(d/6))
        rta="El area verde es {:4.2f}".format(area)
    return rta
    
    
def main():
    print(areaColor("v",12))
    
main()
    
    