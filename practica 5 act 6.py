def recorrerStr(frase):
    res=""
    for i in range(0,len(frase)):
        rta=frase[i]
        res=res+rta
    return res
def fraseReves(frase):
    i=len(frase)-1
    res=""
    while i!=-1:
        rta=frase[i]
        res=res+rta
        i=i-1
    return res

def esPalindrola(frase):
    frase1=recorrerStr(frase)
    frase2=fraseReves(frase)
    if frase1==frase2:
        rta=True
    else:
        rta=False
    return rta

def main():
    frase=input("Ingrese una frase: ")
    res=esPalindrola(frase)
    if res==True:
        rta="La frase es palindrola!"
    else:
        rta="La frase no es palindrola"
    print(rta)
    
main()