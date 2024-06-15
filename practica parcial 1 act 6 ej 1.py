import math

def areaCirculo(radio):
    areaC=math.pi*(radio**2)
    return areaC

def areaTriangulo(byh):
    areaT=(byh)**2//2
    return areaT

def areaNegra(x):
    if x>0:
        res=(areaCirculo(x/2)-areaCirculo(x/4))+areaTriangulo(x)
        rta="El area es {:5.2f}".format(res)
    else:
        rta="Error"
    return rta

def main():
    print(areaNegra(10))
    print(areaNegra(-56))
    
main()
