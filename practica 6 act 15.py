def agregar(di,a,b):
    di[a]=b

def agregarDicEle2(di):
    clave=""
    while clave!=".":
        clave=input("Ingrese numero de documento (o un punto(.) para terminar): ")
        valor=cargarValor() #o puedo poner aca como cosa una lista vacía y abajo llamar a la funcion cargarValor
        agregar(di,clave,valor)
    di.pop(".")
    return di

def cargarValor():                    #<>
    lista=[]
    nombre=[]
    notas=[]
    n=""
    nom=input("Ingrese nombre (o un punto(.) para terminar) : ")
    nombre.append(nom)
    ape=input("Ingrese apellido (o un punto(.) para terminar): ")
    nombre.append(ape)
    lista.append(nombre)
    while n!=0:
        n=int(input("Ingrese notas del alumno, o cero (0) para terminar: "))
        notas.append(n)
    notas.pop(-1)
    lista.append(notas)
    return lista #si yo paso la lista como parametro no hace falta returnar

def imprimirDic(di):
    print(di)
    
def imprimirDicOrd(di):
    di.keys()
    lst=list(di.keys())
    for x in range((len(lst)-1)):
        for y in range((len(lst)-1)):
            if lst[y]>lst[y+1]:
                aux=lst[y]
                lst[y]=lst[y+1]
                lst[y+1]=aux
    for clave in lst:
        print(clave,di[clave])

def main():
    di={}
    agregarDicEle2(di)
    imprimirDic(di)
    imprimirDicOrd(di)
    
main()
