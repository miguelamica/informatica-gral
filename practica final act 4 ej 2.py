lstAlumnos = ['152002,Juan Gonzalez\n','152001,Ana Martinez\n','151988,Ricardo Bochini\n',
'180372,Vicente Pernia\n']
lstMaterias = ['132,Informática Gral\n','127,Álgebra y Geometría\n','137,Física I\n']
lstCursadas= ['137,152001,4.0\n', '127,151988,6.0\n', '137,151988,7.5\n' ,'132,152002,2.0\n',
'132,151988,6.0\n', '127,152001,2.0\n', '127,180372,10.0\n']


def segmentos(lstAlumnos,lstMaterias,lstCursadas):         #><
    lst1=[]
    lst2=[]
    lst3=[]
    for linea in lstAlumnos:
        linea=linea[:-1]
        linea1=linea.split(",")
        linea1[0]=int(linea1[0])
        lst1.append(linea1)
        
    for line in lstMaterias:
        line=line[:-1]
        line1=line.split(",")
        line1[0]=int(line1[0])
        lst2.append(line1)
        
    for lin in lstCursadas:
        lin=lin[:-1]
        lin1=lin.split(",")
        lin1[0]=int(lin1[0])
        lin1[1]=int(lin1[1])
        lin1[2]=float(lin1[2])
        lst3.append(lin1)
    
    for i in range(len(lst3)):
        for j in range(len(lst2)):
            if lst3[i][0]==lst2[j][0]:
                lst3[i][0]=lst2[j][1]
    
    
    
    for k in range(len(lst3)):
        for l in range(len(lst1)):
            if lst3[k][1]==lst1[l][0]:
                lst3[k][1]=lst1[l][1] 
    
    m1=[]
    r1=[]
    b1=[]
    e1=[]
    for i in range(len(lst3)):
        if lst3[i][2]<4:
            l1=[]
            l1.append(lst3[i][0])
            l1.append(lst3[i][1])
            m1.append(l1)
        elif lst3[i][2]>=4 and lst3[i][2]<7:
            l2=[]
            l2.append(lst3[i][0])
            l2.append(lst3[i][1])
            r1.append(l2)
        elif lst3[i][2]>=7 and lst3[i][2]<8:
            l3=[]
            l3.append(lst3[i][0])
            l3.append(lst3[i][1])
            b1.append(l3)
        elif lst3[i][2]>=8 and lst3[i][2]<=10:
            l4=[]
            l4.append(lst3[i][0])
            l4.append(lst3[i][1])
            e1.append(l4)

    di={}
    di["M"]=m1
    di["R"]=r1
    di["B"]=b1
    di["E"]=e1
    
    return di      
    
print(segmentos(lstAlumnos,lstMaterias,lstCursadas)) 