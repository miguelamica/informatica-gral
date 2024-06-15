import random

def secM(azar):
    u=azar%10
    d=azar//10%10
    c=azar//100%10
    um=azar//1000%10
    cm=azar//10000%10
    par=0
    impar=0
    if cm%2:
        impar=cm
    else:
        par=cm
    if um%2:
        impar=impar*10+um
    else:
        par=par*10+um
    if c%2:
        impar=impar*10+c
    else:
        par=par*10+c
    if d%2:
        impar=impar*10+d
    else:
        par=par*10+d
    if u%2:
        impar=impar*10+u
    else:
        par=par*10+u
        
    
    if par>impar:
        return par
    elif impar>par:
        return impar
    
def main():
    azar=random.randint(10000,99999)
    print(azar)
    print(secM(azar))
    
main()
            

    
    
