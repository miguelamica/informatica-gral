def fun1t1(anInf,anSup):               #<>
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
   
    lst2=[]
    i=1
    while i<len(lst1):
        if lst1[i][6]>=anInf and lst1[i][6]<=anSup:
            lst3=[]
            lst3.append(lst1[i][0])
            lst3.append(lst1[i][5])
            lst3.append(lst1[i][6])
            lst2.append(lst3)
            i+=1
        else:
            i+=1
            
    
    for x in range(len(lst2)-1):
        for z in range(len(lst2)-1):
            if lst2[z][1]>lst2[z+1][1]:
                aux=lst2[z]
                lst2[z]=lst2[z+1]
                lst2[z+1]=aux
               
    
    di={}
    if len(lst2)==0:
        rta=di
    else:
        di["año"]=lst2[-1][2]
        di["club"]=lst2[-1][0]
        di["tiros"]=lst2[-1][1]
        rta=di
        
    return rta



print(fun1t1(2016,2020))
print(fun1t1(2016,2016))
print(fun1t1(2020,2020))
print(fun1t1(2025,2029))
