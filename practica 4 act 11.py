def recHuec():
    b=int(input("Ingrese base: "))
    while b<0:
        b=int(input("Ingrese base: "))
    h=int(input("Ingrese altura: "))
    while h<0:
        h=int(input("Ingrese altura: "))
    for f in range(0,h):
        for c in range(0,b):
            if f==0 or c==0 or f==h-1 or c==b-1:
                print(" *", end="")
            else:
                print("  ",end="")
        print()
        
recHuec()