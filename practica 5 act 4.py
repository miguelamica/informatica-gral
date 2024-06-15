def carAMinu(car): 
    if car>='A' and car<='Z':
        car = chr(ord (car)+32)    
    return car

def textoAMinu (texto):
    i=0
    textoMinu = ""
    while i<len(texto):
        textoMinu = textoMinu + carAMinu(texto[i])
        i=i+1    
    return textoMinu

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

def principioFin(texto):
    res=""
    pri=""
    ult=""
    i=0                                               
    largoTexto = len(texto)
    while i<largoTexto:        
        while i<largoTexto and not esLetra2(texto[i]):
            i+=1        
        pal=""
        while i<largoTexto and esLetra2(texto[i]):
            pal=pal+texto[i]
            i+=1
        if pal!="":
            if pri=="":
                pri=pal
            ult=pal
    if pri==ult:
        rta=True
    else:
        rta=False
    return rta

def main():
    texto=input("Ingrese un texto: ")
    convertido=textoAMinu(texto)
    res=principioFin(convertido)
    if res==True:
        print("El texto cumple la condición")
    else:
        print("El texto no cumple la condición")
        
main()