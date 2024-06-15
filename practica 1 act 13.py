num1=int(input("Ingrese el multiplicando: "))
num2=int(input("ingrese el multiplicador: "))
mult1=num1*(num2%10)
mult2=num1*(num2//10%10)
mult3=num1*(num2//100%10)
rta=num1*num2
print("{:10}".format(num1))
print("x{:9}".format(num2))
print("{:_<10}".format("_"))
print("+{:8}-".format(mult1))
"""para que el + y el guion aparrezcan en los dos extremos se los tengo que agregar afuera de las llaves {}"""
print("{:8}--".format(mult2))
print("{:-<10}".format("-"))
print("{:10}".format(rta))