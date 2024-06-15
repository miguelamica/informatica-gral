def sueldoSemana(hSem,hFinSem):
    sueldoSem=0
    sueldoFinSem=0
    if hSem>=0:
        if hSem>=1 and hSem<=9:
            sueldoSem=hSem*15
        elif hSem>=10 and hSem<=19:
            sueldoSem=hSem*20
        elif hSem>=20:
            sueldoSem=hSem*25

    
    if hFinSem>=0:
        if hFinSem>=1 and hFinSem<=9:
            sueldoFinSem=hFinSem*29
        elif hFinSem>=10:
            sueldoFinSem=hFinSem*35
        
    sueldo=sueldoSem+sueldoFinSem
    return sueldo

def main():
    print(sueldoSemana(16,8))
    print(sueldoSemana(8,6))
    print(sueldoSemana(22,8))
    print(sueldoSemana(16,18))
    print(sueldoSemana(0,10))
    print(sueldoSemana(10,0))
    
    print(sueldoSemana(0,-10))
    print(sueldoSemana(-3,-3))
    
main()