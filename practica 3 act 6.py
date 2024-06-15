def pregunta(num):
    if num%2==0:
        num2=(int(input("{} {}{}".format("Ingrese un numero menor que",num,": "))))
        if num2<num:
            rta=True
        else:
            rta=False
    if num%2==1:
        num2=(int(input("{} {}{}".format("Ingrese un numero mayor que",num,": "))))
        if num2>num:
            rta=True
        else:
            rta=False
    return rta
        
         
def main():
    num=int(input("Ingrese un numero entero positivo: "))
    res=(pregunta(num))
    if res==True:
        print("Es correcto")
    if res==False:
        print("Es incorrecto")
    
main()

