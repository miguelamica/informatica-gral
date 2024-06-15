def carAMayu(car):
    if car>='a' and car<='z':
        car = chr(ord (car)-32)    
    return car

def priLetraMayu(texto):
    res=""
    i=0
    while i<len(texto):
        if texto[i]==" ":
            letra=carAMayu(texto[i+1])
            res=res+" "+letra
            i+=2
        elif i==0:
            letra=carAMayu(texto[i])
            res=res+letra
            i+=1
        else:
            letra=texto[i]
            res=res+letra
            i+=1
    return res

def main():
    texto=input("Ingrese el texto: ")
    print(priLetraMayu(texto))
    
main()
            
            