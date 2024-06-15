def sumaMitades(num):
    cifNum=len(str(num))
    if cifNum%2==0 and cifNum>=2 and cifNum<=6:          #<>
        u=num%10
        d=num//10%10
        c=num//100%10
        um=num//1000%10
        dm=num//10000%10
        cm=num//100000%10
        sum1=um+c
        sum2=d+u
        sum3=um+dm+cm
        sum4=u+d+c
        if cifNum==2:
            if u!=0:
                rta="{}-{}".format(d,u)
            if u==0:
                rta="El numero es incompleto"
        if cifNum==4:
            if sum1!=0 or sum2!=0:
                rta="{}-{}".format(sum1,sum2)
            if sum1==0 or sum2==0:
                rta="El numero es incompleto"
        if cifNum==6:
            if sum3!=0 or sum4!=0:
                rta="{}-{}".format(sum3,sum4)
            if sum3==0 or sum4==0:
                rta="El numero es incompleto"
    else:
        rta="El numero es invalido"
    
    return rta

def main():
    print(sumaMitades(2345))
    print(sumaMitades(103090))
    print(sumaMitades(61))
    print(sumaMitades(994456))
    
    print(sumaMitades(103000))
    print(sumaMitades(40))
    
    print(sumaMitades(4))
    print(sumaMitades(1234567))
    print(sumaMitades(12345678))
    
main()