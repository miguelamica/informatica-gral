def palConExtremos(extremos,pal):        #><
    if len(extremos)==2 and len(pal)>0:
        ext1=extremos[0]
        ext2=extremos[-1]
        rta="La función retornó: {}{}{}".format(ext1,pal,ext2)
    else:
        rta="La función ha retornado una palabra vacía"
    return rta

def main():
    extremos=input("Ingrese los extremos: ")
    pal=input("Ingrese la palabra: ")
    res=palConExtremos(extremos,pal)
    print(res)
    
main()