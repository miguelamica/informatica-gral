def figura(b):
    for f in range(0,(b//2)+1):
        for c in range(0,b):
#             if (c==0 or c==b-1 or f==0 or f==b-1) : borde
            if ((c-f)>=1 and c+f<=(b-2)) or f==0 or f==(b//2) or c==0 or c==(b-1):
                print(" *",end="")
            else:
                print("  ",end="")
                
        print()
        
figura(13)