def perimetro(num1, num2, num3):
    per=(num1 + num2 + num3)/2
    return per

def area(per,num1, num2, num3):
    area1= ((per*(per-num1)*(per-num2)*(per-num3))**0.5)
    return area1

def ingresNums(msj):
    print(msj,end="")
    mensaje=int(input())
    return mensaje

def main():
    a=ingresNums("Ingresar lado 1: ")
    b=ingresNums("Ingresar lado 2: ")
    c=ingresNums("Ingresar lado 3: ")
    miPer=perimetro(a,b,c)
    miArea=float(area(miPer,a,b,c))
    print("El area del triangulo es: ""{:3.2f}".format(miArea))

main()
    