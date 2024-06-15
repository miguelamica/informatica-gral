def textoEnTexto (largo,corto):
    cont=0
    i=0
    while i<len(largo):
        if corto==largo[i:i+len(corto)]:
            cont+=1
            i+=len(corto)
        else:
            i+=1
    return cont

def main():
    largo=input("Ingrese el texto largo: ")
    corto=input("Ingrese el texto corto: ")
    num=textoEnTexto(largo,corto)
    rta="El texto corto se encontró {} veces en el texto largo".format(num)
    print(rta)
    
main()