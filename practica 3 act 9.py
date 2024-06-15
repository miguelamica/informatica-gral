def bono(sBase):
    if sBase>2000:
        bon=sBase*0.15
    else:
        bon=sBase*0.2
    return bon

def plusH(hijos,sBase):
    if hijos==True:
        plusHij=sBase*0.05
    if hijos==False:
        plusHij=0
    return plusHij

def plusC(cat,sBase):
    if 1<=cat<=3:
        plusCat=sBase*0.1
    elif 4<=cat<=6:
        plusCat=sBase*0.12
    elif 7<=cat<=9:
        plusCat=sBase*0.2
    return plusCat

def plus(hijos,cat,sBase):
    if hijos==True and cat<=6:
        plusHC=plusH(hijos,sBase)+plusC(cat,sBase)
    elif hijos==True and 7<=cat<=9:
        plusHC=plusC(cat,sBase)
    elif hijos==False and 1<=cat<=9:
        plusHC=plusC(cat,sBase)
    return plusHC
        

def main():
    sBase=int(input("Ingrese el sueldo base: "))
    hij=input("Tiene hijos (responder s o n): ")
    cat=int(input("A que categoria pertenece?: "))
    res1=bono(sBase)
    if hij=="s":
        hijos=True
    else:
        hijos=False
    plusH(hijos,sBase)
    plusC(cat,sBase)
    res2=plus(hijos,cat,sBase)
    rta=res1+res2+sBase
    print("El sueldo total sera de ${:6.2f}".format(rta))
    
    
main()

    