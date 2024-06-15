def rotacionTexto(texto):
    texto1=texto[0:(len(texto)//2)]
    texto2=texto[len(texto)//2:]
    rta=texto2+texto1
    return rta

def main():
    texto=input("Ingrese un texto: ")
    esPar=len(texto)%2
    while len(texto)<2 or esPar!=0:
        texto=input("Error. Ingrese un texto: ")
        esPar=len(texto)%2
    rta=rotacionTexto(texto)
    print(rta)
    
main()