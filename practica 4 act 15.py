def rombo(b):
    for f in range(0,b):
        for c in range (0,b):
            if f<=c+(b//2) and f>=c-(b//2) and f +c+(b//2)>=b-1 and f+c-(b//2)<=b-1: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        
rombo(7)