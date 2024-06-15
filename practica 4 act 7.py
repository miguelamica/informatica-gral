def notas():         #<>
    n=1
    num=0
    n1=0
    n2=0
    n3=0
    nota1=n
    nota2=n
    nota3=n
    if 1<=n<=10:
        while n!=0:
            n=int(input("Ingresar notas: "))
            if 1<=n<4:
                n1+=1
                nota1=n
            elif 4<=n<=7:
                n2+=1
                nota2=n
            elif 7<n<=10:
                n3+=1
                nota3=n
            if 1<=n<=10:
                num+=1
    
        por1=(n1*100)/num
        por2=(n2*100)/num
        por3=(n3*100)/num
        
        rta1=print("Cantidad de aplazados: {} ({:4.2f}%)".format(n1,por1))
        rta2=print("Cantidad de aprobados: {} ({:4.2f}%)".format(n2,por2))
        rta3=print("Cantidad de promocionados: {} ({:4.2f}%)".format(n3,por3))
        
    
    return rta1, rta2, rta3

def main():
    notas()
    
main()