def raiz(num1,num2):
    rz=num1**(num2/(num2**2))
    return rz
def ingreseMsj1(msj):
    print(msj,end="")
    mensaje1=float(input())
    return mensaje1
def ingreseMsj2(msj):
    print(msj,end="")
    mensaje2=int(input())
    return mensaje2
def main():
    radicando=ingreseMsj1("Ingrese el radicando: ")
    indice=ingreseMsj2("Ingrese el indice: ")
    rta=raiz(radicando,indice)
    print("La raiz",indice,"de",radicando,"es:",rta)

main()
