def cicloNumEnt():
    i=0
    while i<5:
        num=int(input("Ingrese un numero entero: "))
        if num%2==0:
            i=i+1
            print("Numero par. Total de numeros pares: {}".format(i))

def main():
    cicloNumEnt()
main()


        