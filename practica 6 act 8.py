def cargarLista():
    lista=[]
    num=""
    while num!=0:
        num=float(input("Ingrese numeros, o 0 (cero) para terminar:"))
        lista.append(int(num))
    inserOrd(lista)
    lista.pop(-1)
    return lista

def ordenarLst(lst):
    for x in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                num=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=num
    return lst

def inserOrd(lst):
    lst=ordenarLst(lst)
    i=0
    while i<len(lst):
        if lst[i]<lst[i+1]:
            lst.insert(i,(i+1))
            i+=2
        elif lst[i] > lst[len(lst)-1]:
            lst.insert(len(lst),i)
            i+=1
        else:
            i+=1
            
def main():
    lst=cargarLista()
    print(lst)
    
main()