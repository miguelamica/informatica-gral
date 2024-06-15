def archivo():
    arc=open("act1.txt","r")
    lst=arc.readlines()
    lst1=[]
    for j in lst:
        j=j[:-1]
        lst1.append(j)
    arc.close()
    return lst1

def informe(lst):                      #<>
    lst1=[]
    #mayor y menor
    i=0
    num=int(lst[i])
    mayor=num
    menor=num
    while i<len(lst):
        if int(lst[i])>mayor:
            mayor=int(lst[i])       #o max()
        elif int(lst[i])<menor:
            menor=int(lst[i])       #o min()
        i+=1
    lst1.append(mayor)
    lst1.append(menor)
    #promedio y total de elementos
    ele=len(lst)-1
    tot=0
    for i in range(len(lst)-1):
        tot=tot+int(lst[i])
    pro=tot/ele         #o mean()
    lst1.append(pro)
    lst1.append(ele)
    return lst1

        
def main():
    lst=archivo()
    print(informe(lst))
    
main()
    