def promedio(num1,num2,num3):
    if num1<=num2<=num3:
        menor=num1
        medio=num2
        mayor=num3
    elif num1<=num3<=num2:
        menor=num1
        medio=num3
        mayor=num2
    elif num2<=num3<=num1:
        menor=num2
        medio=num3
        mayor=num1
    elif num2<=num1<=num3:
        menor=num2
        medio=num1
        mayor=num3
    elif num3<=num1<=num2:
        menor=num3
        medio=num1
        mayor=num2
    elif num3<=num2<=num1:
        menor=num3
        medio=num2
        mayor=num1
    if (menor+mayor)/2==medio:
        res=True
    else:
        res=False
    return res


def main():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    num3=int(input("Ingrese el tercer numero: "))
    rta=promedio(num1,num2,num3)
    if rta==True:
        print("Los numeros estan igualmente distanciados")
    if rta==False:
        print("Los numeros NO estan igualmente distanciados")
        
main()