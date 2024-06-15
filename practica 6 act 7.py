def ordenarLst(lst):
    for x in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                num=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=num  

def inserOrd(lst,num):
    i=0
    while i<len(lst) and num not in lst:
        if num<lst[i]:
            lst.insert(i,num)
            i+=2
        elif num > lst[len(lst)-1]:
            lst.insert(len(lst),num)
            i+=1
        else:
            i+=1
            
def main():
    lst=[5,31,70,12,2]
    ordenarLst(lst)
    print("Lista ingresada: {}".format(lst))
    num=int(input("Ingrese valor a insertar: "))
    inserOrd(lst,num)
    print("La lista con la inserción ordenada es: {}".format(lst))
    
main()
