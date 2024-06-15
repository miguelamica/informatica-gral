def esPrimo(n):
    primo=True
    for i in range(2,n):
        if n%i==0:
            primo=False
    return primo and n!=1

def cantidad():
    c=1
    i=0
    i2=2
    d=0
    cant=int(input("Ingrese un numero entero  natural: "))
    for i in range(2,cant):
        if esPrimo(i)==True:
            print(i)
            i+=1
            
    while c<=cant :
        if esPrimo(i2)==True:
            print(i2)
            c+=1
        i2+=1
        
def main():
    cantidad()

main()
