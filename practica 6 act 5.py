import random as rd

def cargarLista():
    lista=[]
    num=""
    while num!=0:
        num=float(input("Ingrese numeros, o 0 (cero) para terminar:"))
        lista.append(int(num))
    lista.pop(-1)
    return lista

def estaEnLista(l,a,b):
    res=False
    if a<=l<=b:
            res=True
    return res

def cambiarLista(ls,a,b):
    i=0
    while i<len(ls):
        l=ls[i]
        if estaEnLista(l,a,b)!=True:
            nn=rd.randint(a,b)
            ls[i]=nn
            i+=1
        else:
            i+=1
    return ls
            
def main():
    ls=cargarLista()
    num1=int(input("Ingrese el primer extremo de la lista: "))
    num2=int(input("Ingrese el segundo extremo de la lista: "))
    print(cambiarLista(ls,num1,num2))

    
main()
        
        