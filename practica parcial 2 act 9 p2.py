def esLetra(c):
    return (c>="a" and c<="z") or (c>="A" and c<="Z") or (c in "áéíóúüñÁÉÍÓÚÜÑ")

def extraerPal(texto,inf,sup):                      #<>
    i=0
    lst=[]
    while i<len(texto):
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        pal=""
        while i<len(texto) and esLetra(texto[i]):
            pal=pal+texto[i]
            i+=1
        if len(pal)>=inf and len(pal)<=sup:
            lst.append(pal)
    return lst

def main():
    texto="667Me*- color,las __ estrellas"
    print(extraerPal(texto,1,5))
    
main()