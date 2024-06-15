num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
u=num1%10
d=num2//10%10
print("El numero resultante es: ",'{}{}'.format(d,u))