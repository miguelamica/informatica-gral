def estaEnLista(lista,num):
    res=False
    for i in range(0,len(lista)):
        if lista[i]==num:
            res=True
    return res

def cargarLista():
    lista=[]
    num=""
    while num!=0:
        num=float(input("Ingrese numeros, o 0 (cero) para terminar:"))
        if num<0:
            print("ERROR. Número NO positivo.")
        elif estaEnLista(lista,num)==True:
            print("ERROR. Número repetido.")
        elif int(num)!=num:
            print("Número NO valido")
        else:
            lista.append(int(num))
    lista.pop(-1)
    return lista

def main():
    print(cargarLista())
    
main()
    