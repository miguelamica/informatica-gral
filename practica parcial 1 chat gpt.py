#practica parcial 1 chat gpt
def decABin(dec):
    u=dec%10
    d=dec//10%10
    c=dec//100%10
    um=dec//1000%10
    umB=um//2%2
    cB=c//2%2
    dB=d//2%2
    uB=u//2%2
    rta="{}{}{}{}".format(umB,cB,dB,uB)
    

def main():
    dec=int(input("Ingrese un numero decimal: "))
    print(decABin(dec))
    
main()
    