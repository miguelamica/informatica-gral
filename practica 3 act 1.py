def operacion(signo,num1,num2):
    if signo=="+":
        res=num1+num2
    if signo=="-":
        res=num1-num2
    if signo=="*":
        res=num1*num2
    if signo=="/":
        res=num1/num2
        
    return res
def main():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    sig=str(input("Ingrese la operacion: "))
    rta=operacion(sig,num1,num2)
    print("{}{}{}""=""{}".format(num1,sig,num2,rta))
    
main()