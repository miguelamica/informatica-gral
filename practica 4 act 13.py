def triIso(b):
    for f in range(0,(b//2)+1):
        for c in range(0,b):
            if f+c>=(b//2) and c-f<=(b//2):
                print(" *",end="")
            else:
                print("  ",end="")
        
        print()
        
triIso(9)