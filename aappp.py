def fun(x):
    i=0
    tam=len(x)
    while i< (tam/2):
        a = x[i]
        x[i] = x[tam-1-i]
        x[tam-1-i] = a
        i+=1
def main():
    x=[1,2,3,4,5]
    fun(x)
    print(x)
main()