num=int(input("Ingresa un número de 5 digitos: "))
u=num%10
d=num//10%10
c=num//100%10
um=num//1000%10
dm=num//10000
print("Mira, te separe tu numero por digitos y lo eleve al cuadrado: ", dm**2,um**2,c**2,d**2,u**2)