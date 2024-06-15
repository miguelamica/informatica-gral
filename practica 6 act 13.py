def agregar(di,a,b):
    di[a]=b
    
    
def agregarDicEle():
    di={}
    clave=""
    while clave!=".":
        clave=input("Ingrese un numero entero (o un punto(.) para terminar): ")
        valor=input("Ingrese el mismo numero escrito (o un punto(.) para terminar): ")
        agregar(di,clave,valor)
    di.pop(".")
    return di
    
def main():
    di=agregarDicEle()
    num=int(input("ingrese un numero entero (o un punto (.):"))
    while num !=".":
        if num in di:
            print(di[num])
        if num not in di:
            num=int(input("error. ingrese un numero entero (o un punto (.):"))
            print(di[num])
            
main()