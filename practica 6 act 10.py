import random as rd

def cargarListaAleat(a,b,can):
    lista=[]
    i=0
    while i<can:
        num=rd.randint(a,b)
        lista.append(num)
        i+=1
    return lista

def atributoSimple(lst):
    i=0
    cont=0
    while i<len(lst)-2:
        if lst[i]==lst[i+1] and lst[i+1]==lst[i+2]:
            cont=cont+1
            i+=3
        else:
            i+=1
    if cont==0:
        rta="NADA"
    elif cont==1:
        rta="UN TRIPLE"
    elif cont==2:
        rta="dos triples"
    elif cont>=3:
        rta="+ triples"
    return rta
    
def main():
    num1=int(input("Ingrese el primer extremo de la lista: "))
    num2=int(input("Ingrese el segundo extremo de la lista: "))
    can=int(input("Ingrese la cantidad de numeros que contendrá la lista: "))
    lst=cargarListaAleat(num1,num2,can)
    print(atributoSimple(lst))
    
main()