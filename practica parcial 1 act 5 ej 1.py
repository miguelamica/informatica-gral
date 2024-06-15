def aDec(num,base):
    u=num%10
    d=num//10%10
    c=num//100%10
    um=num//1000%10
    dm=num//10000%10
    return dm*(base**4)+um*(base**3)+c*(base**2)+d*(base**1)+u

def main():
    b1=int(input("Ingrese la primera base: "))
    num1=int(input("Ingrese el numero en esa primera base: "))
    b2=int(input("Ingrese la segunda base: "))
    num2=int(input("Ingrese el numero en esa segunda base: "))
    res1=aDec(num1,b1)
    res2=aDec(num2,b2)
    print("{} es el decimal de {} en base {} y {} es el decimal de {} en base {}".format(res1,num1,b1,res2,num2,b2))
    if res1>res2:
        rta="{} es mayor que {}".format(res1,res2)
    elif res2>res1:
        rta="{} es mayor que {}".format(res2,res1)
    elif res1==res2:
        rta="{} y {} son iguales".format(res1,res2)
    print(rta)
    
main()