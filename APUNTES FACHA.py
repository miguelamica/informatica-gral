num=257
print("el contenido del num es:", num)
print("el id del num es:", id(num))

'''una cadena de caracteres ("10") no es lo mismo que un numero comun (10). la cadena de caracteres no se puede ni sumar ni restar ni multiplicar.
ejemplo'''
num1="10"
num2="20"
suma=num1+num2
print(suma)
'''es distint0 a esto'''
num1=10
num2=20
suma=num1+num2
print(suma)


'''
10 - entero - int
3.14 - real - float
"100" "hola" - texto - str
True - logico -bool
nada - ?????? - NoneType
'''


'''convertir de dato a variable'''
print(str(10))
print(float(10))
print(bool(10==10.0))

'''puede convertir de str a float entre comillas pero no de str a int con comillas porque considera como si tuviera una letra
ACLARACIÓN: PARA CONVERTIR DE STR A FLOAT EL NUMERO TIENE QUE ESTA SEPARADO POR UN PUNTO (3.14) PORQUE SINO TIRA ERROR'''
print(int(3.14))
print(round(3.14))

num1=int(input("che tecleate el numero1 porfis: "))
num2=int(input("perdoname que te joda de vuelta pero me podes escribir otro numero??: "))
print("Tecleaste: ",num1, "y",num2)
print("ahora vamos a hacer cuentas con esos numeros que te pedi que escribas: ")
suma=num1+num2
print(num1,"+",num2,"=",suma)
print(num1,"-",num2,"=",num1-num2)
print(num1,"*",num2,"=",num1*num2)
print(num1,"/",num2,"=",num1/num2)
print(num1,"//",num2,"=",num1//num2)
print(num1,"%",num2,"=",num1%num2)
print(num1,"**",num2,"=",num1**num2)


