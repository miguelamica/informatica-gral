def recortePal(pal):                 #><
    if len(pal)>=4:
        rec=pal[-2:]
        rta="La función ha retornado: {}{}{}".format(rec,rec,rec)
    else:
        rta="La función ha retornado una palabra vacía"
    return rta

def main():
    pal=input("Ingrese una palabra: ")
    res=recortePal(pal)
    print(res)
    
main()
    