def esPerfecto(n):
    sumaDivisores=0
    for i in range (1,n):
        if n%i==0:    
            sumaDivisores+=i
    if sumaDivisores==n:
        rta=True
    else:
        rta=False
    return rta

def perfectos():
    x=0
    i=1
    while x<=4:
        if esPerfecto(i)==True:
            print(i)
            x+=1
        i+=1

def main():
    print(perfectos())

main()