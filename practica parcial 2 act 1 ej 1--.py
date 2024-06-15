def esLetra(c):
    if (c>="a" and c<="z") or (c>="A" and c<="Z"):
        res=True
    else:
        res=False
    return res

def numVocA(pal):
    i=0
    x=0
    while i<len(pal):
        if pal[i] ==  "A" or pal[i] == "a" or pal[i] == "E" or pal[i] == "e" or pal[i] == "O" or pal[i] == "o" :
            x+=1
            i+=1
        else:
            i+=1
    return x

def numVocC(pal):
    i=0
    x=0
    while i<len(pal):
        if pal[i] ==  "I" or pal[i] == "i" or pal[i] == "U" or pal[i] == "u":
            x+=1
            i+=1
        else:
            i+=1
    return x
    

def maxima(sec):
    mayor=""
    i=0
    while i<len(sec):
        while i<len(sec) and not esLetra(sec[i]):
            i+=1
            
        pal=""       
        while i<len(sec) and esLetra(sec[i]):     
            pal = pal + sec[i]                      
            i+=1
        
        if len(pal)>=len(mayor) and numVocA(pal) == numVocC(pal):
            mayor=pal
            
    return mayor


def main():
    print(maxima("guam,chau"))
    print(maxima("pucho pucherito"))
    print(maxima("pucho"))
    
main()