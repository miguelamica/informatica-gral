def estaEnLista(lista,num):
    res=False
    for i in range(0,len(lista)):
        if lista[i]==num:
            res=True
    return res

def cargarConjuntos():
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
    
def union(l1,l2):
    lista3=[]+l1
    for b in l2:
        if b not in lista3:
            lista3.append(b)
    return lista3

def interseccion(l1,l2):
    lista3=[]
    for a in l1:
        if a in l2:
            lista3.append(a)
    return lista3

def diferencia(l1,l2):
    lista3=[]
    for a in l1:
        if a not in l2:
            lista3.append(a)
    return lista3

def diferenciaSimetrica(l1,l2):
    lista3=[]
    for a in l1:
        if a not in l2:
            lista3.append(a)
    for b in l2:
        if b not in l1:
            lista3.append(b)
    return lista3
    
    

def nombre():
    print("1. CARGAR CONJUNTOS \n2. UNIÓN \n3. INTERSECCIÓN \n4. DIFERENCIA (A-B) \n5. DIFERENCIA SIMÉTRICA \n6. SALIR")
    opc=int(input("Ingresa la opción que deseas ejecutar: "))
    while opc!=6:
        if opc==1:
            lista1=cargarConjuntos()
            lista2=cargarConjuntos()
            opc=int(input("Ingresa la opción que deseas ejecutar: "))
    
        elif opc==2:
            lista1=cargarConjuntos()
            lista2=cargarConjuntos()
            print(union(lista1,lista2))
            opc=int(input("Ingresa la opción que deseas ejecutar: "))
        
        elif opc==3:
            lista1=cargarConjuntos()
            lista2=cargarConjuntos()
            print(interseccion(lista1,lista2))
            opc=int(input("Ingresa la opción que deseas ejecutar: "))
            
        elif opc==4:
            lista1=cargarConjuntos()
            lista2=cargarConjuntos()
            print(diferencia(lista1,lista2))
            opc=int(input("Ingresa la opción que deseas ejecutar: "))
                
        elif opc==5:
            lista1=cargarConjuntos()
            lista2=cargarConjuntos()
            print(diferenciaSimetrica(lista1,lista2))
            opc=int(input("Ingresa la opción que deseas ejecutar: "))
                    
        elif opc==6:
            res=None

def main():
    print(nombre())
    
main()
