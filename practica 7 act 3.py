def esLetra(c):                            #<>
    return (c>="a" and c<="z") or (c>="A" and c<="Z") or (c in "áéíóúüñÁÉÍÓÚÜÑ")

def estaEnLista1(lst,num):
    if num in lst:
        res=True
    else:
        res=False
    return res

def frecuenciaPalabra():
    arc=open("act3.txt","r")
    lst=arc.readlines()
    
    #sacar palabras
    
    i=0
    lstPal=[]
    arc1=open("act_3.csv","a")
    while i<len(lst[0]):
        while i<len(lst[0]) and not esLetra(lst[0][i]):
            i+=1
        pal=""
        while i<len(lst[0]) and esLetra(lst[0][i]):
            pal=pal+lst[0][i]
            i+=1
        lstPal.append(pal)
    
    #armar el archivo nuevo
        
    cont=0
    lstPal2=[]
    for x in range(len(lstPal)-1):
        cont=0
        for y in range(1,len(lstPal)-1):
            if lstPal[x]==lstPal[y]:
                cont=cont+1
        if lstPal[x] not in lstPal2:
            arc1.write(lstPal[x])
            arc1.write(",")
            arc1.write(str(cont))
            arc1.write("\n")
            lstPal2.append(lstPal[x])
            lstPal2.append(cont)
            lstPal2.append("\n")
    arc.close()
    arc1.close()
    return lstPal2

def main():
    print(frecuenciaPalabra())
    
main()