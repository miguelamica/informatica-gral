import random as rd

def ruleta(can):
    lista=[]
    i=0
    while i<can:
        num=rd.randint(0,36)
        lista.append(num)
        i+=1
    return lista

def porcentual(lst):
    cont=0
    for x in range(0,37):
        for y in range(len(lst)-1):
            if x==lst[y]:
                cont+=1
        if cont!=0:
            por=(cont*100)/len(lst)
            rta="El numero {} salio {}% veces".format(x,por)
            print(rta)
            cont=0
        
def main():
    can=int(input("Ingrese la cantidad de numeros de la lista:"))
    lst=ruleta(can)
    print(lst)
    print(porcentual(lst))
    
main()
         