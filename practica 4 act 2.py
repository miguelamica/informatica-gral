def numH0():
    num=int(input("Ingrese un numero entero (finaliza con 0):"))
    mayor=num
    menor=num
    while num!=0:
        if num>mayor:
            mayor=num
        elif num<menor:
            menor=num
        
        num=int(input())
        
    print("El numero mayor es {}".format(mayor))
    print("El numero menor es {}".format(menor))

        
        
def main():
    numH0()
main()