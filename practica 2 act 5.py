import random
def funcionNumeros(num):
    print(num,end="")
    num1=int(input())
    return num1
def funcionNumeros1(num):
    print(num,end="")
    num2=int(input())
    return num2
def aleatorio(num1,num2):
    numero=random.randint(num1,num2)
    return numero
def main():
    numero1=funcionNumeros("Ingrese el limite inferior: ")
    numero2=funcionNumeros("Ingrese el limite superior: ")
    Aleatorio1=aleatorio(numero1,numero2)
    Aleatorio2=(aleatorio(Aleatorio1,numero2))
    Aleatorio3=(aleatorio(Aleatorio1,Aleatorio2))
    print("Limite inferior",numero1,"limite superior",numero2,". Numero generado: ",Aleatorio1)
    print("Limite inferior",Aleatorio1,"limite superior",numero2,". Numero generado: ",Aleatorio2)
    print("Limite inferior",Aleatorio1,"limite superior",Aleatorio2,". Numero generado: ",Aleatorio3)
    
main()