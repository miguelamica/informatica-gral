def promedio(lst):                    #<>
    i=0
    y=1
    suma=0
    if len(lst)%2==0:
        while i<len(lst):
            s=lst[i]+lst[y]
            suma=s+suma
            i+=2
            y+=2
    else:
        while y<=len(lst): 
            if y<len(lst):
                s=lst[i]+lst[y]
                suma=s+suma
                i+=2
                y+=2
            if y==len(lst):
                suma=suma+lst[-1]
                y+=1
    if suma!=0:
        prom=suma/len(lst)
    else:
        prom=""
        
    return prom

#opcion alternativa para calcular promedio:
#def promedio(lst):
#	suma=0
#	cant=len(lst)
#	for x in lst:
#		suma=suma+n
#	return suma/cant
        

def nuevaLst(lst,prom):
    i=0
    while i<len(lst):
        if lst[i]>prom:
#             lst.remove(lst[i])
            lst.pop(i)
        else:
            i+=1
    return lst
            
def main():
    lst=[24,30,2,10,15,6,65,42]
    prom=promedio(lst)
    print("Lista original: {}".format(lst))
    lst2=(nuevaLst(lst,prom))
    print("Lista modificada: {}".format(lst2))
    
main()
