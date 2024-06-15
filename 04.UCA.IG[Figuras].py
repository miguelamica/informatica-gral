
################################################################################
## ÚLTIMA ACTUALIZACIÓN: 19/06/2022 04:00 ######################################
################################################################################
##       UNIDAD 4 - FIGURAS con ciclos
################################################################################
## U C A   - I N F O R M Á T I C A   G E N E R A L #############################
################################################################################

################################################################################
################################################################################

################################################################################
## COMENTARIOS
##
## La idea de esta práctica de desarrollar figuras con ciclos de repetición es 
## la de poner en la lograr manejar ciclos múltiples con una condición 
## lógica compleja en su interior, y con ello visualizar así el comportamiento  
## de dichas condiciones lógicas.
## 
## Dibujaremos puntos dentro de un cuadrilátero, dicho cuadrilátero puede 
## interpretarse como una matriz.
## 
## Representamos con " *" (asteriscos) la instancia dentro del ciclo cuando
## la condición lógica es True.
## Representamos con "  " (espacio) la instancia dentro del ciclo cuando
## la condición lógica es False.
## 
## Utilizaremos una plantillas (una función prehecha) donde cambiando la 
## condición lógica obtendremos distintas figuras en el espacio de dos
## dimensiones (x,y)
##
################################################################################

################################################################################
##
## PLANTILLA PROPUESTA A UTILIZAR
##
## Definiciones:
##    b: base     -> representa la base (o bien el lado) de un cuadrado
##                   es un número entero
##    f: fila     -> representa la fila de una hipotética matriz
##                   es un número entero
##    c: columna  -> representa la fila de una hipotética matriz
##                   es un número entero
##    <<CONDICIÓN LÓGICA>> -> Aquí colocaremos la condición lógica que dará
##                            origen a la figura.       

##
##
## La plantilla a continuación ....
##
'''
def figura(b):    
    for f in range(0,b):
        for c in range(0,b):
            if <<CONDICIÓN LÓGICA>> :
                print(" *",end="")
            else:
                print("  ",end="")                
        print()

'''
################################################################################

################################################################################
## ALGUNAS CONDICIONES Y LA DESCRIPCIÓN DE LA FIGURA QUE IMPRIME UTILIZANDO
## LA PLANTILLA PROPUESTA, reemplazando la <<CONDICIÓN LÓGICA>>
##
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Cuadrado (de ​asteriscos)
'''
True
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Diagonal principal de un cuadrado
'''
f==c
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Diagonal secundaria de un cuadrado
'''
f+c==b-1
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Lado superior del cuadrado
'''
f==0
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Lado inferior del cuadrado
'''
f==b-1
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Lado izquierdo del cuadrado
'''
c==0
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Lado derecho del cuadrado
'''
c==b-1
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Recta media vertical del cuadrado
'''
c==b//2 
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Recta media horizontal del cuadrado
'''
f==b//2 
'''
##
## Hasta aquí las figuras básicas lineales. Ahora veremos como pasar figuras
## en dos dimensiones utilizando el simbolo mayor > o el simbolo menor <
##
## ALGUNAS PUEDEN SER
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Triangulo Inferior SudOeste
'''
f>=c 
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Triangulo superior NorEste
'''
f<=c 
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Triangulo Inferior SudEste
'''
f+c>=b-1
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Triangulo Inferior NorOeste
'''
f+c<=b-1
'''

##
## Ahora veremos como pasar figuras como combinar distintas figuras
## 
## El operador 'or' se utiliza para hacer unión de figuras
## El operador 'and' se utiliza para hacer intersección de figuras
##

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Se suma (union) el Triangulo Inferior SudEste con la Diagonal principal
'''
f+c>=b-1  or f==c
'''

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Se realiza (intersección) del Triangulo Inferior SudEste y la Diagonal principal
'''
f+c>=b-1 and f==c
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Se realiza intersecciones y uniones diversas para obtener un figura
'''
(f+c>=b-1 and f>=c) or c==b//2 or (f==0 and c>=b//2)
'''

##
## Ahora veremos como desplazar las línes o las figuras
##
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##  Siendo x un numero entero
##  (+) Sumando x a la fila se desplaza x veces hacia arriba (Norte)
##
'''
b//2==f+2
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##  Siendo x un numero entero
##  (+) Sumando x a la columna se desplaza x veces hacia izquierda (Oeste)
##
'''
b//2==c+2
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##
##  Siendo x un numero entero 
##  (-) Restando x a la fila se desplaza x veces hacia Abajo (Sur)
##
'''
b//2==f-2
'''
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##  Siendo x un numero entero
##  (-) Restando x a la columna se desplaza x veces hacia derecha (Este)
'''
b//2==c-2
'''


## ANEXO
##
## Aplicando el concepto de la ecu​a​cación de la recta de m (su pendiente)
## Su multiplicación a ​'​f​'o a ​'​c​'​ por un valor de ​'​m​'​ vamos a obtener una
## inclinación de la recta
## Para ​'​m​'​=1/2
'''
f==(1/2)*c
'''
##



################################################################################
## EJEMPLOS - ROMBO VACIO,  ROMBO LLENO Y
## RELOJ DE ARENA (Arriba vacio, abajo medio lleno)
################################################################################

def figura_01(b):    
    for f in range(0,b):
        for c in range(0,b):
            if f+c==b-1-(b//2) or f+c==b-1+(b//2) or f==c+(b//2) or f==c-(b//2):
                print(" *",end="")
            else:
                print("  ",end="")                
        print()
def figura_02(b):    
    for f in range(0,b):
        for c in range(0,b):
            if f+c>=b-1-(b//2) and f+c<=b-1+(b//2) and f<=c+(b//2) and f>=c-(b//2):
                print(" *",end="")
            else:
                print("  ",end="")                
        print()

def figura_03(b):    
    for f in range(0,b):
        for c in range(0,b):
            if f==c or f+c==b-1 or f==0 or f==b-1 or (f>=c and f+c>=b-1)and f>=b*(2/3) :
                print(" *",end="")
            else:
                print("  ",end="")                
        print()
        
def figura_04(b):    
    for f in range(0,b):
        for c in range(0,b):
            if f==(1/2)*c :
                print(" *",end="")
            else:
                print("  ",end="")                
        print()
        
def main():
    b=11 # Base debe ser IMPAR
    print("\nFigura ROMBO vacio de base={}".format(b))
    figura_01(b)
    
    print("\nFigura ROMBO lleno de base={}".format(b))
    figura_02(b)
    
    print("\nFigura RECTA base={}".format(b))
    print("inclinada con un m=1/2")
    figura_03(b)
    
    print("\n")
    figura_04(b)
main()

################################################################################
##########################    F  I  N    #######################################
################################################################################
