def medTrian(b):
    for f in range(0,b):
        for c in range(0,b):
            if f+c<=b-1 and f>=c:
                print(" *",end="")
            else:
                print("  ",end="")
        print()
        
medTrian(7)




