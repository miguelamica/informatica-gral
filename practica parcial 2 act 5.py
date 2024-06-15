def esLetra(c):
    return (c>="a" and c<="z") or (c>="A" and c<="A") or (c in "ÁÉÍÓÚÜÑáéíóúüñ")

def nuevaLista(texto):                    #<>
    lista=[]
    i=0
    while i<len(texto):
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        pal=""
        while i<len(texto) and esLetra(texto[i]):
            pal=pal+texto[i]
            i+=1
            
        if "bilidad" in pal and pal not in lista:
            lista.append(pal)
    return lista
            
def main():
    print(nuevaLista("amabilidad,gato portabilidad, &%$#modabilidad*amabilidad gatito"))
    
main()