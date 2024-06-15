def esLetra(c):
    return (c>="A" and c<="Z") or (c>="a" and c<="z") or (c in "áéíóúüñÁÉÍÓÚÜÑ")

def vocAbi(pal):
    i=0
    x=0
    while i<len(pal):
        if pal[i] in "AaEeOoÁáÉéÓó":
            i+=1
            x+=1
        else:
            i+=1
    return x

def vocCer(pal):
    i=0
    x=0
    while i<len(pal):
        if pal[i] in "IiUuÍíÚú":
            i+=1
            x+=1
        else:
            i+=1
    return x

def maxima(sec):                        #<>
    i=0
    mayor=""
    while i<len(sec):
        while i<len(sec) and not esLetra(sec[i]):
            i+=1
        pal=""
        while i<len(sec) and esLetra(sec[i]):
            pal=pal+sec[i]
            i+=1
          
        if len(pal)>=len(mayor) and (vocAbi(pal)==vocCer(pal)):
            mayor=pal
            
    
    return mayor
        
def main():
    print(maxima("pucho pucherito nito carlin "))
    
main()
        