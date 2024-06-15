def tipoNum(num):
    if num==0:
       res= "El numero es cero y entero"
    elif int(num)==num:
        if num>0:
            res= "El numero es positivo y entero natural"
        else:
            res= "El numero es negativo y entero"
    elif int(num)!=num:
        if num>0:
            res= "El numero es positivo y real"
        else:
            res= "El numero es negativo y real"
    return res


def main():
    numero=float(input("Ingrese un número: "))
    print(tipoNum(numero))
    
main()