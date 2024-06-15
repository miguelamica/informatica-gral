################################################################################
##  ÚLTIMA ACTUALIZACIÓN: 24/10/2022 21:30 #####################################
################################################################################
##  UNIDAD 6B -       T U P L A S
################################################################################
##  U C A   - I N F O R M Á T I C A   G E N E R A L  ###########################
################################################################################

################################################################################
################################################################################

################################################################################
################################################################################
##     ================
##        T U P L A S
##     ================
##      
##      + La tupla es una secuencia INMUTABLE de objetos (cualquier tipo de datos
##            válido en python).
##      + type: <class 'tuple'>
##      + Utiliza el PARÉNTESIS para definirla.
##      + se puede acceder al contenido de una posición a través de su índice.
##      + Se puede acceder a una posición SÓLO para leerla(INMUTABLE).
##      + Se puede hacer slicing.
##
##
## **** CARACTERÍSTICAS DE LA LISTA !! ****
## -> SECUENCIA  Sucesión de elementos. En 'tuple' el elemento puede ser
##               cualquier tipo de dato válido de python.
##
## -> INMUTABLE  Un tipo de dato es inmutable cuando NO puede ser
##               modificado sus elementos. 
##               
## -> ITERABLE  (Que puede ser recorrido "con un ciclo")
##               Las secuencias en python son iterables
##
## -> LONGITUD: (o largo) Es la cantidad de elementos que contiene la lista
##
## -> Función len(): - SOLO se aplica a una SECUENCIA
##                   - Obtiene la cantidad de elementos de la secuencia
##
## -> OPERADORES: 
##          +: (Concatena) dos tuplas. Y se obtiene una nueva tupla
## 
##          *: (Concatena)Se utiliza para multiplicar una tupla 'tu' por un numero
##                 entero 'n'. La operación concatena 'n' veces a 'tu'
##                 Y se obtiene una nueva tupla.
##         in: Membresía) funciona el operador in (por ser secuencia) 
##    
##
## -> MÉTODOS: 
##            - .NO USAREMOS NINGÚN MÉTODO
##            
################################################################################

#################################################################################
##
## T U P L A

def laTupla():
    tu1 = ()               # crea tupla vacía, sin valores
    tu2 = tuple()          # crea tupla vacía, sin valores. Idem anterior
                           # con len obtengo cantidad elementos
    tu3 = (1,)             # crea tupla con un elemento
    tu4 = (1,2,3)          # crea tupla con tres elementos
                           # crea tupla con CINCO elementos
    tu5 = ("abc",2,True,3.14,[99,88,77])   

    print(" - - - tu5 -  -")
    print("contenido ->",tu5)              # imprimir toda la tupla
    print("largo ->",len(tu5))             # imprimir largo de la tupla
    print("elemento tu5[1] ->",tu5[1])     # imprimir un elemento de la tupla
    print("slicing tu5[1:4] ->",tu5[1:4])  # imprimir slicing
    print(" - - - X -  -")

    ### INMUTABLE
    ### tu[0]="xxx"         # error, NO se puede asignar inmutable

################################################################################
## ==================
## RECORRER UNA TUPLA
## ==================
###
#
## RECORRER tupla

tu6 =(23,3.14,22,"hola",99)

# ## ------------------------------------------------------
# ## RECORRER lista con while ( Utiliza índice en la lista)
# ## ------------------------------------------------------
# ##

def recorrerTuplaWhile(tu6):
    print(" - - while - -  -")
    i=0
    while(i<len(tu6)):
        print(tu6[i])
        i+=1

# ## ------------------------------------------------------
# ## RECORRER lista con for ( Utiliza índice en la lista)
# ## ------------------------------------------------------
# ##

def recorrerTuplaFor(tu6):
    print(" - - for - -  -")
    for i in range(0,len(tu6)):  
        print(tu6[i])
 
# ## ------------------------
# ## RECORRER lista con for (Sin utilizar índice en la lista)
# ## ------------------------

def recorrerTuplaFor2(tu6):
    print(" - - for 2- -  -")
    for x in tu6:  
        print(x)                       

def concatenarTupla():
    tu7=(1,3)    
    num=99
    tu8=("aa",num,"bb")
    #concatenar
    tuA = tu7 + (num,)
    tuB = tu8 + tu7
    print("tu7 + (num,) ->",tuA)
    print("tu8 + tu7 ->",tuB)
    

################################################################################
################################################################################
## CONVERSIÓN DE TIPOS
## - - - - - -  - - - -
## de <??> a <tuple>
##     Para convertir un tipo de dato a tupla, el tipo de dato a convertir 
##     debe ser iterable. Se pueden convertir a tupla el <str>, <list> y <range>

##
## de <tuple> a <??>
##     Una tuple se puede convertir a <str>, <list>
##
################################################################################



