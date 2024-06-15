num=str(input("Ingrese un numero de cifras inpar (al menos 3 cifras): "))
num1=int(len(num))
print("El numero tiene",len(num),"cifras")
primer=int(num)//10**(num1-1)
ultimo=int(num)%10
central=int(num)//10**(num1//2)
central1=central%10
print("la primer cifra es",primer," la ultima es",ultimo,"y la central es",central1)