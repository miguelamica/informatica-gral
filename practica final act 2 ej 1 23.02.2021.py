lstEnergia = ['101205, 1, 24.2\n', '110607, 8, 54.4\n', '120318, 3, 18.1\n',
'090501, 9, 88.4\n', '101209, 1, 26.8\n', '101217, 3, 22.4\n', '190101, 8, 44.0\n']

def minimos(lstenergia):
    lst1=[]
    for linea in lstenergia:
        linea=linea[:-1]
        linea1=linea.split(",")
        linea1[0]=int(linea1[0])
        linea1[1]=int(linea1[1])
        linea1[2]=float(linea1[2])
        lst1.append(linea1)
    
    
    lst2=[]
    for x in range(len(lst1)):
        cont=0
        lst3=[]
        for z in range(len(lst1)):
            if str(lst1[x][0])[:2]==str(lst1[z][0])[:2]:
                cont=cont+lst1[z][2]
        
        if str(lst1[x][0])[:1]=="1":
            lst3.append(str(lst1[x][0])[:2])
        else:
            lst3.append(str(lst1[x][0])[:1])
        lst2.append(lst3)
        lst2[x][0]=int(lst2[x][0])
        lst3.append(cont)
        
                                 #<>
        
    for i in range(len(lst2)-1):
        for j in range(len (lst2)-1):
            if lst2[j][1]>lst2[j+1][1]:
                aux=lst2[j]
                lst2[j]=lst2[j+1]
                lst2[j+1]=aux
            
    ele=tuple(lst2[0])
    
    
    mayor=0
    mes=""
    for m in range(len(lst1)):
        if str(ele[0])==str(lst1[m][0])[:2]:
            if lst1[m][2]>mayor:
                mayor=lst1[m][2]
                mes=str(lst1[m][0])[:4]
                
    lst4=[]
    lst4.append(mes)
    lst4[0]=int(lst4[0])
    lst4.append(mayor)
    
    ele1=tuple(lst4)
    
    rta=[]
    rta.append(ele)
    rta.append(ele1)
    
    return rta

print(minimos(lstEnergia))
                