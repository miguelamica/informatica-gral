def numAlReves(n):
    i=0
    numN=len(str(n))
    numD=numN-1
    cif1=0
    for i in range(0,numN):
        cif=n//(10**(i))%10
        cif1=cif*(10**numD)+cif1
        numD-=1
    return cif1

def capicua(num1):
    num2=numAlReves(num1)
    if num2==num1:
        rta=True
    else:
        rta=False
    return rta

def main():
    num=int(input("Ingrese un numero entero: "))
    res=capicua(num)
    if res==True:
        rta="El numero es capicua"
    else:
        rta="El numero no es capicua"
    print(rta)
    
main()