def fra(texto):
    print(texto,end="")
    frase=str(input())
    return frase

def justificado(fra,ancho):
    rta=("'"+"{:>{d}}"+"'").format(fra,d=ancho-2)
    return rta

def main():
    frase=fra("Ingrese la frase: ")
    ancho=int(fra("Ingrese el ancho: "))
    res=justificado(frase,ancho)
    print(res)
    
main()