def esLetra(c):
    return (c>="a" and c<="z") or (c>="A" and c<="Z") or (c in "áéíóúüñÁÉÍÓÚÜÑ")

def cabecera2(arc,cant,pmin,pmax):
    arch=open(arc,"r")
    lst=arch.readlines()
    lstPal=[]
    for linea in lst:
        linea=linea[:-1]
        linea1=linea.split(" ")
        i=0
        while i<len(linea1):
            while i<len(linea1) and not esLetra(linea1[i]):
                i+=1
            pal=""
            y=0
            while i<len(linea1) and y<len(linea1[i]) and esLetra(linea1[i][y]):
                pal=pal+linea1[i][y]
                y+=1
            i+=1
            lstPal.append(pal)
    print(lstPal)
    lstFin=[]
    i=0
    cont=0
    while i<len(lstPal):
        while i<len(lstPal) and (len(lstPal[i])<pmin or len(lstPal[i])>pmax):
            i+=1        
        while  i<len(lstPal) and (len(lstPal[i])>=pmin and len(lstPal[i])<=pmax):
            lstFin.append(lstPal[i])
            i+=1
            cont+=1
    arch1=open("act4.csv","a")
    lstFIN=[]
    for x in range(cant):
        if lstFin[x] not in lstFIN:
            arch1.write(lstFin[x])
            arch1.write("\n")
            lstFIN.append(lstFin[x])
    arch.close()
    arch1.close()
    return lstFIN
    
def main():
   print(cabecera2("act4.txt",5,2,9))
   
main()

    