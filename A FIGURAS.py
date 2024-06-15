#figuras con ciclos

def figura(b):        #cuadrado corte lado a lado cada uno en su cuadrado aguanten los rebos carajo
    for f in range(0,b):
        for c in range (0,b):
            print(" *", end="")
        print()


def figura1(b):        #cuadrado corte lado a lado cada uno en su cuadrado aguanten los rebos carajo
    for f in range(0,b):
        for c in range (0,b):
            if True: 
                print(" *", end="")
            else:
                print("  ",end="")
            
        print()
        
        
def figura2(b):        #diagonal principal corte diagonal norte la estacion de subte d 
    for f in range(0,b):
        for c in range (0,b):
            if f==c: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        
        
def figura3(b):        #diagonal secundaria corte el secundario q lugar de mierda por dios
    for f in range(0,b):
        for c in range (0,b):
            if f+c==b-1: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        

def figura4(b):        #techo cuadrado
    for f in range(0,b):
        for c in range (0,b):
            if f==0: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        
def figura5(b):        #base cuadrado
    for f in range(0,b):
        for c in range (0,b):
            if f==b-1: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        
        
def figura6(b):        #lado izquierdo cuadrado
    for f in range(0,b):
        for c in range (0,b):
            if c==0: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        
def figura7(b):        #lado derecho cuadrado
    for f in range(0,b):
        for c in range (0,b):
            if c==b-1: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        
def figura08(b):        #union
    for f in range(0,b):
        for c in range (0,b):
            if c==f or c+f==b-1 or f==0 or f==b-1: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()

def figura8(b):        #union
    for f in range(0,b):
        for c in range (0,b):
            if c==0 or c==b-1 or f==0 or f==b-1: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        
#tambien se puede jugar con el < o > para q imprima figuras rellenas como aaaaaaa mejor no hago el chiste xq me suspenden la cuenta
        
def figura9(b):        #rombo como la figura de las cartas de poker y poker como la cancion poker face de lady gaga
    
    for f in range(0,b):
        for c in range (0,b):
            if f==c+(b//2) or f==c-(b//2) or f +c+(b//2)==b-1 or f+c-(b//2)==b-1: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()        
        
        
def figura10(b):        #rombo como la figura de las cartas de poker y poker como la cancion poker face de lady gaga pero relleno
    
    for f in range(0,b):
        for c in range (0,b):
            if f<=c+(b//2) and f>=c-(b//2) and f +c+(b//2)>=b-1 and f+c-(b//2)<=b-1: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()
        

def figura11(b):        #funcion lineal
    
    for f in range(0,b):
        for c in range (0,b):
            if f==(1/2)*c: 
                print(" *", end="")
            else:
                print("  ", end="")
            
        print()  
        

figura(7)
figura1(7)
figura2(7)
figura3(7)
figura4(7)
figura5(7)
figura6(7)
figura7(7)
figura08(7)
figura8(7)
figura9(7)
figura10(7)
figura11(7)
