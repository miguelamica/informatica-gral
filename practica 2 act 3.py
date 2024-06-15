def divisionBin(bin):
    a=bin%10
    b=bin//10%10
    c=bin//100%10
    d=bin//1000%10
    e=bin//10000%10
    f=bin//100000%10
    g=bin//1000000%10
    h=bin//10000000%10
    resultado=(a+b+c+d+e+f+g+h)%2
    return resultado

def ingreseNumBin(num):
    print(num,end="")
    binario=float(input())
    return binario

def main():
    binario1=ingreseNumBin("Ingrese un número binario de hasta 8 bits: ")
    rta=divisionBin(binario1)
    print("Bit de paridad generado: {} ".format(rta))
    
main()