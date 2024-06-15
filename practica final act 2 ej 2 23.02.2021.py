lstEnergia = ['101205, 1, 24.2\n', '110607, 8, 54.4\n', '120318, 3, 18.1\n',
'090501, 9, 88.4\n', '101209, 1, 26.8\n', '101217, 3, 22.4\n', '190101, 8, 44.0\n']
lstParque = ['1,Rosario, 8\n', '6,San Martin, 4\n', '8,Lavalle, 10\n',
'3,Esperanza,3\n', '7,General Pico, 9\n', '9,P.Madryn, 4\n']

def energiaTotal(n,lstEnergia,lstParque):                     #<>
    lst1=[]
    for linea in lstEnergia:
        linea=linea[:-1]
        linea1=linea.split(",")
        linea1[0]=int(linea1[0])
        linea1[1]=int(linea1[1])
        linea1[2]=float(linea1[2])
        lst1.append(linea1)
        
    lst2=[]
    for linea in lstParque:
        linea=linea[:-1]
        linea1=linea.split(",")
        linea1[0]=int(linea1[0])
        linea1[2]=int(linea1[2])
        lst2.append(linea1)
    
    lista=[]
    for x in range(len(lst1)):
        cont=0
        lst3=[]
        for z in range(len(lst1)):
            if lst1[x][1]==lst1[z][1]:
                cont=cont+lst1[z][2]
        i=0
        while lst1[x][1]!=lst2[i][0]:
            i+=1
        nombre=lst2[i][1]
        molino=lst2[i][2]
        cep=cont/molino
        lst3.append(nombre)
        lst3.append(cont)
        lst3.append(cep)
        if lst3 not in lista:
            lista.append(lst3)
    
    print(lista)
        
    for j in range(len(lista)-1):
        for k in range(len(lista)-1):
            if lista[k][1]>lista[k+1][1]:
                aux=lista[k]
                lista[k]=lista[k+1]
                lista[k+1]=aux
    lista=lista[::-1]
    
    return lista[:n]
    
        
print(energiaTotal(3,lstEnergia,lstParque))    

