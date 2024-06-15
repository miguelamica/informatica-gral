def fun2T1(a,b,c):
    if a>0 and b>0 and c>0:      #<>
        d=a+b+c
        if d%a==0 and d%b==0 and d%c==0:
            rta="La sumatoria es: {}".format(d)
        else:
            if a!=b and b!=c:
                if a<b and b<c:
                    medio=b
                if a<c and c<b:
                    medio=c
                if b<a and a<c:
                    medio=a
                if b<c and c<a:
                    medio=c
                if c<b and b<a:
                    medio=b
                if c<a and a<b:
                    medio=a
                rta="El numero del medio es: {}".format(medio)
    else:
        rta="ERROR"
    
    return rta

def main():
    print(fun2T1(1,2,3))
    print(fun2T1(6,4,2))
    print(fun2T1(5,5,10))
    
    print(fun2T1(3,7,9))
    print(fun2T1(17,7,9))
    print(fun2T1(17,21,9))

    print(fun2T1(-1,2,2))
    print(fun2T1(-1,-2,-3))
    
main()
    
