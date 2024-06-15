def orden(num1,num2,num3):
    if num1<num2<num3:
        res=num1,num2,num3
    elif num1<num3<num2:
        res=num1,num3,num2
    elif num2<num3<num1:
        res=num2,num3,num1
    elif num2<num1<num3:
        res=num2,num1,num3
    elif num3<num1<num2:
        res=num3,num1,num2
    elif num3<num2<num1:
        res=num3,num2,num1
    return res
        
        

def main():
    num1=int(input("Ingrese el 1er numero: "))
    num2=int(input("Ingrese el 2do numero: "))
    num3=int(input("Ingrese el 3er numero: "))
    print("Los numeros ordenados ascendentemente son: ",orden(num1,num2,num3))
    
    
main()