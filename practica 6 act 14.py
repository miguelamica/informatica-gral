def agregar(di,a,b):
    di[a]=b


def agregarDicEle2():
    di={}
    clave=""
    while clave!=".":
        clave=input("Ingrese un numero entero (o un punto(.) para terminar): ")
        esp=input("Ingrese el número en español: ")
        eng=input("Ingrese el número en inglés: ")
        deuch=input("Ingrese el número en alemán: ")
        valor=(esp,eng,deuch)
        agregar(di,clave,valor)
    di.pop(".")
    return di

def main():
    di=agregarDicEle2()
    num=int(input("ingrese un numero entero a traducir(o un punto (.):"))
    lan=input("Ingrese un idioma a traducir (esp, eng o deuch): ")
    while num !=".":
        if num in di:
            if lan==esp:
                print(di[num][0])
            elif lan==eng:
                print(di[num][1])
            elif lan==deuch:
                print(di[num][2])
        elif num not in di:
            num=int(input("error. ingrese un numero entero (o un punto (.):"))
            print(di[num])
            
main()
