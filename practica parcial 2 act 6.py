def esLetra(c):
    return (c>="a" and c<="z") or (c>="A" and c<="Z") or (c in "áéíóúüñÁÉÍÓÚÜÑ")

def numVoc(pal):
    i=0
    x=0
    while i<len(pal):
        if pal[i] in "aeiouAEIOUáéíóúÁÉÍÓÚüÜ":
            x+=1
            i+=1
        else:
            i+=1
    return x

def listita(texto):                           #<>
    i=0
    lista=[]
    while i<len(texto):
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        pal=""
        while i<len(texto) and esLetra(texto[i]):
            pal=pal+texto[i]
            i+=1
        if numVoc(pal)>=3:
            lista.append(pal)
            
    return lista

def main():
    texto="....,Otto Orozco y Hanz Orozco--, quisieran rodar sus máquinas! Vamos hombres!!!!!!!"
    print(listita(texto))
    
main()
        