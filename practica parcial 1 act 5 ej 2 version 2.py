import random

def elige(num):
    cifNum=len(str(num))
    nAzar=random.randint(0,int(cifNum)-1)
    rta=num//(10**nAzar)%10
    return rta

def gen(num):
    c=elige(num)
    d=elige(num)
    u=elige(num)
    return "{}{}{}".format(c,d,u)

def main():
    num=int(input("Ingrese un numero entero: "))
    rta=gen(num)
    if int(rta)%2==0:
        print("Un llamado a gen con parametro {} retorna {}. {} es par".format(num,rta,rta))
    else:
        print("Un llamado a gen con parametro {} retorna {}. {} es impar".format(num,rta,rta))

main()