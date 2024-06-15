lstAlumnos = ['152002,Juan Gonzalez\n','152001,Ana Martinez\n','151988,Ricardo Bochini\n',
'180372,Vicente Pernia\n']
lstMaterias = ['132,Informática Gral\n','127,Álgebra y Geometría\n','137,Física I\n']
lstCursadas= ['137,152001,4.0\n', '127,151988,6.0\n', '137,151988,7.5\n' ,'132,152002,2.0\n',
'132,151988,6.0\n', '127,152001,2.0\n', '127,180372,10.0\n']

def aprobadas(lstAlumnos,lstMaterias,lstCursadas,nombre):          #><
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
        
    for i in range(len(lst1)):
        if lst1[i][1]==nombre:
            n=lst1[i][0]
    
    lst=[]
    for j in range(len(lst3)):
        if lst3[j][1]==n:
            if lst3[j][2]>=4:
                lst.append(lst3[j])
                
    
    lista=[]
    for x in range(len(lst)):
        mat=""
        for z in range(len(lst2)):
            if lst[x][0]==lst2[z][0]:
                mat=lst2[z][1]
                nota=lst[x][2]
        tup=(mat,nota)
        lista.append(tup)
        
        
    print(lista)
    
aprobadas(lstAlumnos ,lstMaterias ,lstCursadas,'Ricardo Bochini' )
        