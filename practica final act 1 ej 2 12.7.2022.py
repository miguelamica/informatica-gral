def fun2t1(n):                  #<>
    lsArch = ['club,jugador,partidos,minutos,goles,tiros,anio\n', '(JUV),Cristiano Ronaldo,29,2634,25,162,2016\n',
    '(PSG),Neymar,30,2694,13,105,2016\n', '(BAR),Lionel Messi,32,2910,37,179,2016\n',
    '(RMA),Eden Hazard,36,3101,16,77,2016\n', '(TOT),Dele Alli,35,3182,18,95,2016\n', '(BAR),Lionel Messi,32,3123,33,197,2017\n',
    '(JUV),Cristiano Ronaldo,27,2375,26,178,2017\n', '(BAR),Lionel Messi,29,2849,36,170,2018\n',
    '(JUV),Cristiano Ronaldo,30,2857,21,177,2018\n', '(PSG),Angel Di Maria,28,2418,12,97,2018\n', '(PSG),Neymar,16,1517,15,54,2018\n',
    '(MNU),Edinson Cavani,20,1747,18,52,2018\n', '(RMA),Eden Hazard,32,3115,16,93,2018\n',
    '(BAR),Lionel Messi,32,3067,25,159,2019\n', '(JUV),Cristiano Ronaldo,33,3127,31,208,2019\n',
    '(INT),Lautaro Martinez,29,2581,14,125,2019\n', '(PSG),Neymar,15,1396,12,71,2019\n', '(PSG),Angel Di Maria,23,2106,8,74,2019\n',
    '(BAR),Lionel Messi,8,824,4,39,2020\n', '(JUV),Cristiano Ronaldo,5,397,8,26,2020\n']
    lst1=[]
    for linea in lsArch:
        linea=linea[:-1]
        linea1=linea.split(",")
        lst1.append(linea1)
        
    for i in range(1,len(lsArch)):
            lst1[i][2]=int(lst1[i][2])
            lst1[i][3]=int(lst1[i][3])
            lst1[i][4]=int(lst1[i][4])
            lst1[i][5]=int(lst1[i][5])
            lst1[i][6]=int(lst1[i][6])
    
    lista=[]
    for k in range(1,len(lst1)):
        if lst1[k][1] not in lista:
            lista.append(lst1[k][1])
    
    lista1=[]
    for l in range(len(lista)):
        cont=0
        for m in range(len(lst1)):
            if lista[l]==lst1[m][1]:
                cont=cont+lst1[m][3]
        nuv=[]
        nuv.append(lista[l])
        nuv.append(cont)
        lista1.append(nuv)
        
    for x in range(len(lista1)-1):
        for z in range(len(lista1)-1):
            if lista1[z][1]>lista1[z+1][1]:
                aux=lista1[z]
                lista1[z]=lista1[z+1]
                lista1[z+1]=aux
    lista1=lista1[::-1]
                
    return lista1[:n]
        
    
print(fun2t1(0))
print(fun2t1(1))
print(fun2t1(2))
print(fun2t1(3))
print(fun2t1(4))