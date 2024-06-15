def esLetra2(car):
    res = False
    acentos = car in "áéíóúüñÁÉÍÓÚÜÑ"
    if ((car>='a'and car<='z') or (car>='A' and car<='Z') or acentos  ):
        res = True
    return res

def esPalabra(pal):
    res = True
    i=0
    while i<len(pal):
        if not esLetra2(pal[i]):
            res=False
        i=i+1
    return res

def primeraMitad(pal):
    rta=pal[0:len(pal)//2]
    return rta

def main():
    pal=input("Ingrese una palabra: ")
    esPar=len(pal)%2
    while esPar!=0 or esPalabra(pal)==False:
        pal=input("Error. Ingrese una palabra: ")
        esPar=len(pal)%2
        esPalabra(pal)
    rta=primeraMitad(pal)
    print(rta)
        
        
main()
        