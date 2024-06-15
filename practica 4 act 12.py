def trian(b):
    for  f in range(0,b):
        for c in range(0,b):
            if f>=c:
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        
trian(5)