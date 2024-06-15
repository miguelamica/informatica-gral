lstCiudad = ['223,Parana\n', '114,Merlo\n', '218,Guaymallen\n', '132,C. Rivadavia\n', '341,Adolfo Alsina\n',
'404,Jose C. Paz\n']
lstResiduos = ['33,114,200518\n', '31,223,200519\n', '27,218,200319\n', '26,132,200616\n', '74,341,200319\n',
'62,404,200606\n', '46,218,200709\n', '55,132,200630\n', '55,341,200612\n', '54,404,200701\n',
'23,114,200315\n', '55,223,200519\n', '34,218,200319\n', '33,132,200425\n', '27,341,200422\n',
'21,404,200501\n', '31,114,200503\n', '44,114,200513\n', '44,218,200519\n']

def media_01(lstResiduos):                         #<>
    lst1=[]
    for line in lstResiduos:
        line=line[:-1]
        line1=line.split(",")
        line1[0]=int(line1[0])
        line1[1]=int(line1[1])
        line1[2]=int(line1[2])
        lst1.append(line1)
    
    for i in range(len(lst1)-1):
        for j in range(len(lst1)-1):
            if str(lst1[j][2])[2:4]>str(lst1[j+1][2])[2:4]:
                aux=lst1[j]
                lst1[j]=lst1[j+1]
                lst1[j+1]=aux
    
    di={}
    for x in range(len(lst1)):
        cont=0
        vec=0
        mes=str(lst1[x][2])[2:4]
        for z in range(len(lst1)):
            if str(lst1[x][2])[2:4]==str(lst1[z][2])[2:4]:
                cont=cont+lst1[z][0]
                vec+=1
        pro=cont/vec
        mes=int(mes)
        di[mes]=pro
        
    print(di)  
    
    
media_01(lstResiduos)
            