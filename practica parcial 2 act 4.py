def numMenores(lst,n):                            #<> 
    if len(lst)!=0:
        for j in range(len(lst)-1):
            for x in range(len(lst)-1):
                if lst[x]>lst[x+1]:
                    aux=lst[x]
                    lst[x]=lst[x+1]
                    lst[x+1]=aux
                
    return lst[0:n]

def main():
    lst=[9,8,7,6,5,3,2,7,9,62,1,89159,1,6,4,7,9,3,2236,2,1,3,6,97,548]
    n=7
    lst2=(numMenores(lst,n))
    if lst!=0:
       rta="Para la lista {}, y n={}, resultado: {}".format(lst,n,lst2)
    else:
        rta=""
    print(rta)
    
main()
                


