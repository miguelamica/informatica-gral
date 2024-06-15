bin=int(input("ingrese un numero binario (hasta 5 dígitos): "))
u=(bin%10)*1
d=(bin//10%10)*2
c=(bin//100%10)*4
um=(bin//1000%10)*8
dm=(bin//10000%10)*16
dec=dm+um+c+d+u
print("el numero decimal es",dec)

