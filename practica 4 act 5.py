def cuatroC(num):
    if len(str(num))==4:
        u=num%10
        d=num//10%10
        c=num//100%10
        um=num//1000%10
        if u+c==d+um:
            rta=True
        else:
            rta=False
        return rta

def numCuatroC():
    i=1000
    while i<10000:
        if cuatroC(i)==True:
            print(i)
        i+=1

def main():
    numCuatroC()
    
main()