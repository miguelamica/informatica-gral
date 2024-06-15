def estaEnLista1(lst,num):
    if num in lst:
        res=True
    else:
        res=False
    return res

def estaEnLista2(lst,num):
    res=False
    for i in range(0,len(lst)):
        if lst[i]==num:
            res=True
    return res

def estaEnLista3(lst,num):
    i=0
    res=False
    while i<len(lst) and res==False:
        if lst[i]==num:
            res=True
        else:
            i+=1
    return res
        
def main():
    lst=[1,127,7,4,5,3,4,9,154,6]
    num=4
    res=estaEnLista2(lst,num)
    print(res)
    
main()
        