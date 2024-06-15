la=[12,4,9,32,8,5]
lb=[17,99,12,9,5,33]
lInte=[12,9,5]
 
def inter(la,lb):
    res=[]
    for a in la:
        if a in lb:
            res.append(a)    
    return res
 
def union(la,lb):
    res=[]+la
    for b in lb:
        if b not in res:
            res.append(b)            
    return res
 
def resta(la,lb):
    res=[]
    for a in la:
        if a not in lb:
            res.append(a)    
    return res   
 
def eliminar1(ls,v): # remove
    i=0
    while i<len(ls):
        if ls[i]==v:  
            #ls.remove(v)
            ls.pop(i)
        else:
            i+=1
 
#def eliminar2(ls,v): # pop
    
    
def main():
    ls=[1,2,3,3,6,3,7,8,9,3]
    print(ls)
    eliminar1(ls,3)
    #eliminar2(ls,3)
    print(ls)
main()
 
fra=":) 13 &39 - 1, /25 18..."
#fra="asiramonavanomarisa"
def esDig(d):
    return d in "0123456789" # d>="0" and d<="9"
#":) Asi ramona - va, no marisa...."   
def fun(fra):
    pri=""
    ult=""
    i=0  
    while i<len(fra):
        while i<len(fra) and not esDig(fra[i]):
            i+=1
        num=""
        while i<len(fra) and esDig(fra[i]):
            num=num+fra[i]
            i+=1
        if num!="":
            if pri=="":
                pri=num
            ult=num
            
    print(pri,ult)
       
    
fun(fra)
 
def fun(fra):
    res=0
    i=0  
    while i<len(fra):
        while i<len(fra) and not esDig(fra[i]):
            i+=1
        num=""
        while i<len(fra) and esDig(fra[i]):
            num=num+fra[i]
            i+=1
        if num!="":
            #['asi', 'ramona', 'va', 'no', 'marisa']
            res=res+int(num)
    
    return res   
def esLetra(c):
    return c>="a"and c<="z" or c>="A"and c<="Z"
 
def fun(fra):
    ls=[]
    i=0  
    while i<len(fra):
        while i<len(fra) and not esLetra(fra[i]):
            i+=1
        pal=""
        while i<len(fra) and esLetra(fra[i]):
            pal=pal+fra[i]
            i+=1
        if pal!="":
            #['asi', 'ramona', 'va', 'no', 'marisa']
            ls.append(len(pal))
    return ls
 
def colapso(fra):
    ls=[]
    i=0  
    while i<len(fra):
        while i<len(fra) and not esLetra(fra[i]):
            i+=1
        pal=""
        while i<len(fra) and esLetra(fra[i]):
            pal=pal+fra[i]
            i+=1
        if pal!="":
            #print(pal,end=",")
            ls.append(pal)
    return ls
 
def fun2(fra):
    ls=[]
    idx=0
    pal=""
    i=0
    for x in fra:
        if esLetra(x):
            pal+=x
        else:
            if pal!="":
                ls.append(pal)
                pal=""
    return ls
            
            
            
 
def esPali(fra):
    fraCol=colapso(fra)
    return fraCol==fraCol[::-1]