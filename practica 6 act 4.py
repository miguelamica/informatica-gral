import random as rd

def cargarListaAleat(a,b,can):
    lista=[a]
    i=0
    while i<can-2:
        num=rd.randint(0,9999999)
        lista.append(num)
        i+=1
    lista.append(b)
    return lista

def maxVal(ls):
    min=ls[0]
    i=0
    while i<len(ls):
        if min<ls[i]:
            min=ls[i]
        i+=1
    return min

def minVal(ls):
    max=ls[0]
    i=0
    while i<len(ls):
        if max>ls[i]:
            max=ls[i]
        i+=1
    return max

def main():
    num1=int(input("Ingrese el primer extremo de la lista: "))
    num2=int(input("Ingrese el segundo extremo de la lista: "))
    can=int(input("Ingrese la cantidad de numeros que contendrá la lista: "))
    lista=cargarListaAleat(num1,num2,can)
    mayor=maxVal(lista)
    menor=minVal(lista)
    rta="La lista generada es {}, siendo el mayor valor de la misma {} y el menor {}".format(lista,mayor,menor)
    print(rta)

    
    
main()