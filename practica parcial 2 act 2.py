def esLetra(c):
    return (c>="a" and c<="z") or (c>="A" and c<="Z") or (c in "áéíóúñüÁÉÍÓÚÑÜ")

def esVocal(pal):
    i=0
    for x in pal:
        if x in "aeiouáéíóúüAEIOUÁÉÍÓÚÜ":
            i+=1
    return i

def esConso(pal):
    i=0
    for x in pal:
        if x in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ":
            i+=1
    return i

def buscarPalabras(texto):                 #<>
    i=0
    rta=""
    while i<len(texto):
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        pal=""
        while i<len(texto) and esLetra(texto[i]):
            pal=pal+texto[i]
            i+=1
            
        if len(pal)%2!=0 and esVocal(pal)>esConso(pal):
            rta=rta+pal+" "
    return rta

def main():
    print(buscarPalabras("Si uno No zyzYz A que puerto NAVega"))
    
main()
    
            


            
            