def cargarLista():                    #<>
    lista=[]
    num=""
    while num!=0:
        num=float(input("Ingrese numeros, o 0 (cero) para terminar:"))
        lista.append(int(num))
    lista.pop(-1)
    return lista
    
def ordenarLst(lst):
    for x in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                num=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=num           
        
def main():
    lst=cargarLista()
    ordenarLst(lst)
    print(lst)
    
main()