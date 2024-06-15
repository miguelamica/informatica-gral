def rectangulo():                        #<>
    b=int(input("Ingrese base: "))
    while b<0:
        b=int(input("Ingrese base: "))
    h=int(input("Ingrese altura: "))
    while h<0:
        h=int(input("Ingrese altura: "))
    for f in range(0,h):
        for c in range(0,b):
            if True:
                print(" *", end="")
            else:
                print("  ",end="")
        print()
    
    
rectangulo()