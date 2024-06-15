import random as rd

#,dest,cant

def generadora(ori,dest,cant):                 #<>
    arch=open(ori,"r")
    lst=arch.readlines()
    lst1=[]
    for linea in lst:
        linea=linea[:-1]
        lst1.append(linea)
    arch1=open(dest,"a")
    lst2=[]
    i=0
    tot=int(len(lst1))
    while i<cant:
        x=rd.randint(0,tot)
        while lst1[x] in lst2:
            x=rd.randint(0,tot)
        while lst1[x] not in lst2:
            lst2.append(lst1[x])
            arch1.write(lst1[x])
            arch1.write("\n")
            i+=1
    
    arch.close()
    arch1.close()
    return lst2

def main():
    print(generadora("act6.txt","act_6.txt",5))
    
main()