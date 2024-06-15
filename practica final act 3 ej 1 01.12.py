lstCiudad = ['223,Parana\n', '114,Merlo\n', '218,Guaymallen\n', '132,C. Rivadavia\n', '341,Adolfo Alsina\n',
'404,Jose C. Paz\n']
lstResiduos = ['33,114,200518\n', '31,223,200519\n', '27,218,200319\n', '26,132,200616\n', '74,341,200319\n',
'62,404,200606\n', '46,218,200709\n', '55,132,200630\n', '55,341,200612\n', '54,404,200701\n',
'23,114,200315\n', '55,223,200519\n', '34,218,200319\n', '33,132,200425\n', '27,341,200422\n',
'21,404,200501\n', '31,114,200503\n', '44,114,200513\n', '44,218,200519\n']

def media_01(n,lstCiudad,lstResiduos):                         #<>
    lst1=[]
    lst2=[]
    for linea in lstCiudad:
        linea=linea[:-1]
        linea1=linea.split(",")
        linea1[0]=int(linea1[0])
        lst1.append(linea1)
        
    for line in lstResiduos:
        line=line[:-1]
        line1=line.split(",")
        line1[0]=int(line1[0])
        line1[1]=int(line1[1])
        line1[2]=int(line1[2])
        lst2.append(line1)
    
    tot=0
    for i in range(len(lst2)):
        tot=tot+lst2[i][0]
    pro=tot/len(lst2)
    
    lista=[]
    for x in range(len(lst1)):
        cont=0
        vec=0
        lst3=[]
        for z in range(len(lst2)):
            if lst1[x][0]==lst2[z][1]:
                cont=cont+lst2[z][0]
                vec+=1
        ci=lst1[x][1]      
        pro1=cont/vec
        lst3.append(ci)
        lst3.append(pro1)
        lista.append(lst3)
    
    for j in range((len(lista)-1)):
        for k in range((len(lista)-1)):
            if lista[k][1]>lista[k+1][1]:
                aux=lista[k]
                lista[k]=lista[k+1]
                lista[k+1]=aux
    lista=lista[::-1]
    lista=lista[:n]
    tup=(pro,lista)
    
    return tup
                    
            
    
print(media_01(3,lstCiudad,lstResiduos))
        