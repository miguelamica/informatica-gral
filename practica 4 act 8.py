def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return "El factorial de {} es {}".format(n,f)
            
        
        
def main():
    n=int(input("Ingrese un numero entero: "))  
    if n>=0:
        rta=print(factorial(n))
    else:
        rta="No se puede calcular el factorial de un número negativo."
    rta

main()
