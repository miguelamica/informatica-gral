def mensaje(c1,c5,m):
    cn5=m//5
    cn1=m%5
    if cn5<=c5:
        if cn1<=c1:
            msj="ES posible cubrir el tendido.\nSugerencia:\n{} unidades de caño de 5 metros.\n{} unidades de caño de 1 metro ".format(cn5,cn1)
        else:
            msj="no es posible cubrir el tendido"
    else:
        falta=cn5-c5
        cn1=falta*5+cn1
        if cn1<=c1:
            msj="ES posible...2. \n{}sugerencia {} unidades de 5 m. \n{} unidades de 1 m ".format(cn5,cn1)
        else:
            msj="no es posible cubrir el tendido"
    return msj


def main():
    caños1=int(input("ingrese cant caños m1: "))
    caños2=int(input("igrese: "))
    metros=int(input("i: "))
    print(mensaje(caños1,caños2,metros))
    
main()