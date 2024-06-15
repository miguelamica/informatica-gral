def esLetra(c):                          #<>
    return (c>="a" and c<="z")

def esVocal(c):
    return c in "aeiou"

def esMonolavica(pal):
    i=0
    x=0
    vocal=""
    while i<len(pal):
        if esVocal(pal[i])==True:
            vocal=vocal+pal[i]
            i+=1
        else:
            i+=1
    res=True
    if len(vocal)==1:
        res=True
    elif vocal=="":
        res=False
    else:
        while (x<len(vocal)-1):
            if vocal[x]==vocal[x+1]:
                x+=1
            else:
                res=False
                x=len(vocal)-1
    return res

def crearLista(texto):
    i=0
    lst=[]
    while i<len(texto):
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        pal=""
        while i<len(texto) and esLetra(texto[i]):
            pal=pal+texto[i]
            i+=1
        if esMonolavica(pal)==True and pal not in lst:
            lst.append(pal)
    return lst

def main():
    print(crearLista("_a veces sentimos que lo que hacemos es tan solo una gota de agua en el mar!!!!!, pero el mar seria muucho menos si le falta una gota"))
    
main()
        

        
        