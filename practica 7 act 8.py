def poblacion(id_prov):                     #<>
    arc=open("alocalidades.csv","r")
    lst=arc.readlines()
    lst1=[]
    for linea in lst:
        linea=linea[:-1]
        linea1=linea.split(";")
        linea1[0]=int(linea1[0])
        linea1[2]=int(linea1[2])
        linea1[3]=int(linea1[3])
        linea1[4]=int(linea1[4])
        lst1.append(linea1)
    arc.close()
    cont=0
    for x in range(len(lst1)):
        if lst1[x][2]==id_prov:
            cont=cont+lst1[x][4]
    arc1=open("aprovincias.csv","r")
    lst2=arc1.readlines()
    lst3=[]
    for lin in lst2:
        lin=lin[:-1]
        lin1=lin.split(";")
        lin1[0]=int(lin1[0])
        lin1[2]=int(lin1[2])
        lst3.append(lin1)
    arc1.close()
    i=0
    nom=lst3[i][1]
    while lst3[i][0]!=id_prov:
        if lst3[i][0]!=id_prov:
            i+=1
        else:
            nom=lst3[i][1]
    
    return "{}: {} habitantes".format(nom,cont)


def localidadMaxima():
    arc=open("alocalidades.csv","r")
    lst=arc.readlines()
    lst1=[]
    for linea in lst:
        linea=linea[:-1]
        linea1=linea.split(";")
        linea1[0]=int(linea1[0])
        linea1[2]=int(linea1[2])
        linea1[3]=int(linea1[3])
        linea1[4]=int(linea1[4])
        lst1.append(linea1)
    arc.close()
    i=0
    mayor=lst1[i][4]
    ciudad=lst1[i][1]
    prov=lst1[i][1]
    while i<len(lst1):
        if lst1[i][4]>mayor:
            mayor=lst1[i][4]      #usar
            ciudad=lst1[i][1]     #usar
            prov=lst1[i][2]
            i+=1
        else:
            i+=1
    #encontrar resto data
    arc1=open("aprovincias.csv","r")
    lst2=arc1.readlines()
    lst3=[]
    for lin in lst2:
        lin=lin[:-1]
        lin1=lin.split(";")
        lin1[0]=int(lin1[0])
        lin1[2]=int(lin1[2])
        lst3.append(lin1)
    arc1.close()
    arc2=open("apaises.csv","r")
    lst4=arc2.readlines()
    lst5=[]
    for line in lst4:
        line=line[:-1]
        line1=line.split(";")
        line1[0]=int(line1[0])
        line1[2]=int(line1[2])
        lst5.append(line1)
    arc2.close()
    #proviincia
    x=0
    prov1=lst3[x][1]
    pais=lst3[x][2]
    while x<len(lst3):
        if lst3[x][0]==prov:
            prov1=lst3[x][1]   #usar
            pais=lst3[x][2]
            x+=1
        else:
            x+=1
    print(pais)
    #pais
    z=0
    pais1=lst5[z][1]
    while z<len(lst5):
        if lst5[z][0]==pais:
            pais1=lst5[z][1]  #usar
            z+=1
        else:
            z+=1
            
    rta="Poblacion: {}\nLocalidad: {}\nProvincia: {}\nPaís: {}".format(mayor,ciudad,prov1,pais1)
    return rta
    

def main():
    print(poblacion(1))
    print(localidadMaxima())
    
main()