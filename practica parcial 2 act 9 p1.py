def promedio(lst,n):                    #<>
    suma=0
    nLst=[]
    i=0
    if n<len(lst):
#         while i+n!=len(lst)+1:
        while i+n<=len(lst):
            for x in range(i,i+n):
                suma=suma+lst[x]
            rta=suma/n
            rta=nLst.append(rta)
            suma=0
            i+=1
    else:
        nLst=[]
    return nLst

def main():
    print(promedio([10,20,30,40,50,60],3))
    print(promedio([10,20,30,40,50,60],2))
    print(promedio([10,20,30,40,50,44],4))
    print(promedio([-2,22,0,7,-1],2))
    print(promedio([10,-22,0,7],3))
    print(promedio([10,-22,0,7],1))
    print(promedio([10,5],4))
    print(promedio([],2))
    
main()
    