def operacion(num1,num2):
    if num1>=num2:
       mayor=num1
       menor=num2
    else:
        mayor=num2
        menor=num1
    resta=mayor-menor
    if resta<=mayor and resta>=menor:
        rta= "SI cumple condicion"
    else:
        rta="NO cumple condicion"
    return rta


def main():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    print("{}".format(operacion(num1,num2)))
    
main()