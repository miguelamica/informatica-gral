def esLetra(c):
    if (c>="a" and c<="z") or (c>="A" and c<="Z"):
        res=True
    else:
        res=False
    return res

def palabras(frase):
    i=0                                                
    res=""
    while i<len(frase):
        while i<len(frase) and not esLetra(frase[i]):
            i+=1                                     
           
        pal=""       
        while i<len(frase) and esLetra(frase[i]):     
            pal = pal + frase[i]                      
            i+=1 
        if pal!="":
            res= res + pal + "\n"    
    return res

def caracteres(cad):    
    i=0
    res=""
    while i<len(cad):
        res=res+cad[i]
        i=i+1
    return res
                                                                                                                         

def encontrarPal(pal,texto):
    c=caracteres(pal)
    f=palabras(texto)
    i=0
    while i<len(pal):
        if pal[i] in f:
            rta=True
        else:
            rta=False
        i+=1
    return rta

def main():
    texto=input("Ingrese el texto: ")
    palabra=input("Ingrese la palabra: ")
    res=encontrarPal(palabra,texto)
    if res==True:
        print("Se cumple la condición")
    else:
        print("No se cumple la condición")
        
main()

    