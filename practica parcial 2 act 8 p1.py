def esLetra(c):                             #<>
    return (c>="a" and c<="z") or (c>="A" and c<="Z") or (c in "áéíóúüñÁÉÍÓÚÜÑ")

def numVocal(pal):
    i=0
    x=0
    while i<len(pal):
        if pal[i] in "aeiouAEIOUáéíóúüÁÉÍÓÚÜ":
            i+=1
            x+=1
        else:
            i+=1
    return x

def extraerPal(texto,nVoc):
    i=0
    lst=[]
    while i<len(texto):
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        pal=""
        while i<len(texto) and esLetra(texto[i]):
            pal=pal+texto[i]
            i+=1
        if numVocal(pal)==nVoc and pal!="":
            lst.append(pal)
    return lst

def main():
    texto="_ A veCes MmmmHHhh!!!sentimos que soLo_faltaríA Una gota En el mar!!!!!,"
    print(extraerPal(texto,0))
    print(extraerPal(texto,1))
    print(extraerPal(texto,2))
    print(extraerPal(texto,3))
    print(extraerPal(texto,4))
    print(extraerPal(texto,5))
    print(extraerPal(texto,70))
    
main()
            
    
    
    