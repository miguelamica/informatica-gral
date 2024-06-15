import random
def elige(num):
    numCif=len(str(num))
    pos=random.randint(0,(numCif-1))
    dig=num//(10**pos)%10
    return dig

def gen(num):
    c=elige(num)
    d=elige(num)
    u=elige(num)
    return "{}{}{}".format(c,d,u)
    
def main ():
    rta=(gen(55468135451))
    print("El numero que genero gen es: {}".format(rta))
    if int(rta)%2==0:
        print("El numero es par")
    else:
        print("El numero es impar")
    

main()