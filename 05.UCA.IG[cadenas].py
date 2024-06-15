################################################################################
## ÚLTIMA ACTUALIZACIÓN: 02/08/2022 17:00 ######################################
################################################################################
##       S  T  R  I  N  G
################################################################################
## U C A   - I N F O R M Á T I C A   G E N E R A L #############################
################################################################################

################################################################################
################################################################################
## UN STRING (cadena de caracteres) es:
##      Un tipo de dato que está conformado por "CARACTERES"
##      Para python es una secuencia
##      <class 'str'> es el nombre del tipo de dato
## 
## **** CARACTERÍSTICAS DEL STRING !! ****
##
## -> SECUENCIA  Sucesión de elementos. En 'str' el elemento es el caracter.
##
## -> INMUTABLE  Una tipo de dato es inmutable cuando no puede ser
##               modificado sus elementos, sólo se puede reasignar para
##               obtener un nuevo valor.
##
## -> ITERABLE  (Que puede ser recorrido "con un ciclo")
##               Las secuencias en python son iterables
##
## -> LONGITUD: (o largo) Es la cantidad de caracteres que contiene el string
##
## -> Función len(): - SOLO se aplica a una SECUENCIA
##                   - Obtiene la cantidad de elementos de la secuencia
##                   - En un string obtiene la cantidad de caracteres
##                     del string
##
## -> OPERADORES: (Concatenar string)
##          +: Concatena dos cadenas de caracteres
## 
##          *: Se utiliza para multiplicar una cadena 'c' por un numero
##                 entero 'n'. La operación concatena 'n' veces a 'c'
##
## -> MÉTODOS:
##          Hasta el momento sólo utilizaremos el método .format()
##
##
## -> ACCESO CON UN ÍNDICE. Los string están indexados.
##    > si x es string =>
##      x[i] obtiene el elemento de x que se encuentra en la posición i
##           
################################################################################


################################################################################
## MODELO VISUAL DE UN STRING CARGADO EN MEMORIA
##
##
## +---+---+---+---+---+---+
## | P | y | t | h | o | n |    <<== CONTENIDO DEL STRING
## +---+---+---+---+---+---+
##   0   1   2   3   4   5      <- Índice directo
##  -6  -5  -4  -3  -2  -1      <- Índice inverso
##
#
def cadena():
    lenguaje = "Python"       # Asignación de un string a una variable
    print(lenguaje)           # Imprimir el contenido de la variable

##
################################################################################

################################################################################
## MODELO VISUAL DE UN STRING CARGADO EN MEMORIA
##
##
## +---+---+---+---+---+---+---+---+---+---+---+---+---+
## | P | y | t | h | o | N | A | B | C | D | E | F | G |    <<== CONTENIDO 
## +---+---+---+---+---+---+---+---+---+---+---+---+---+  
##   0   1   2   3   4   5   6   7   8   9   10  11  12     <- Índice directo
##  -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1      <- Índice inverso
##
##         ^               ^       ^           ^
##         |  x[-11:-7]    |       |  x[8:11]  |            <- Slicing
##            -> "thoN"              -> "CDE"               
#
def cadena2():
    x = "PythoNABCDEFG"       # Asignación de un string a una variable
    print(x)                  # Imprimir el contenido de la variable

def indCad():
    #acceso a la posición 
    x = "PythoNABCDEFG"
    print(x[0])        #P
    print(x[-len(x)])  #P
    print(x[1])        #y
    print(x[5])        #N
    print(x[-8])       #N
    print(x[len(x)-1]) #G
    print(x[-1])       #G
    
#
##
################################################################################

################################################################################
##
## S L I C I N G    O    S L I C E
##
## variableCadena[start : stop : step]
##
## -> Slicing es el mecanismo de obtener partes "rebanadas" de un cadena
##
## EJEMPLOS:

def sliceCad():
    x = "PythoNABCDEFG"
    print(x[0:3])             # [inicio: fin]
    print(x[1:4])             # [inicio: fin]
    print(x[1:])              # [inicio: ] # desde inicio , hasta "el final"
    print(x[1:len(x)])        # Idem anterior
    print(x[:4])              # [ : fin]   # desde "principio", hasta fin
    print(x[:])               # [ : ]      # desde "principio", hasta "el final"
    ##print(x[])              # error !!! No puede quedar vacío entre los
                              #           corchetes
    
    print(x[1:len(x):3])      # [inicio: fin : salto]
    
    print(x[0:len(x):1])      # [inicio: fin : salto]
    print(x[::])              # idem anterior
         
    print(x[:-1])              # devuelve todos los caracteres EXCEPTO el 
                              #     último. idem a print(x[len(x)-1])
    print(x[::-1])            # devuelve invertido el string


###############################################################################
##
## ELEMENTOS DE UNA CADENA
## "" E L  C A R A C T E R ""
##
## -> En python un caracter es un string de largo uno
## -> En python la cadena de caracteres (str) está compuesta por caracteres, 
##    tantos caracteres como largo_de_la_cadena 
## -> Los caracteres están codificados, es decir que un caracter tendrá asociado
##    un valor numérico. A esta codificación se la conoce como código ascii.
##    CÓDIGO ASCII link a tabla ->  https://elcodigoascii.com.ar/
## -> La función ord() obtiene el número de código a partir de un caracter
## -> La función chr() obtiene el caracter a partir de un número de código
##
## EJEMPLOS:

def elCaracter():    
    print("ord ('@')","->",ord("@")) # el ordinal de un CARACTER y va 
                                     # de 0 a 255 (según tabla asciii)
    print("chr(64)","->",chr(64))    # devuelve el caracter segun un entero
                                     # que representa posición en tabla

    print("a -> ",ord("a"))     # Codigo ascii del caracter
    print("A -> ",ord("A"))     # Codigo ascii del caracter
    print("f -> ",ord("f"))     # Codigo ascii del caracter
    print("F -> ",ord("F"))     # Codigo ascii del caracter
    print("@ -> ",ord("@"))     # Codigo ascii del caracter
    
    ## - - - ANALIZAR LAS LETRAS DEL ALFABETO - - -
    ## - - -     Diferencia de 32 entre letra mayúscula y minúscula  - - -
    print(chr(ord("A")+32))     # pasa a minuscula, se le suma 32 al código
    print(chr(ord("a")-32))     # pasa a mayuscula, se le resta 32 al código
    print(chr(ord("T")+32))     # pasa a minuscula, se le suma 32 al código
    print(chr(ord("t")-32))     # pasa a mayuscula, se le resta 32 al código


################################################################################
##
## R E C O R R I D O   de una cadena de caracteres
##
    
## - - - Recorrido con un while y con el índice del string
##
def recorrerStr(cad):    
    i=0
    while i<len(cad):
        print(cad[i])
        i=i+1
      
## - - - Recorrido con un for y con el índice del string
##
def recorrerStrF1(cad):    
    for i in range(0,len(cad)):
        print(cad[i])

## - - - Recorrido con un for, sin utilizar el índice el string
##
def recorrerStrF2(cad):    
    for x in cad:
        print(x)
        

################################################################################
## Identificación de una letra (SIN TENER en cuenta acentos, diéresis y 'enie'(ñ)
## 
def esLetra(car):
    res = False
    if ((car>="a" and car <="z") or (car>="A" and car <="Z")):
        res=True
    return res

################################################################################
## Identificación de una letra (TENIENDO en cuenta acentos, diéresis y 'enie'(ñ)
##
def esLetra2(car):
    res = False
    acentos = car in "áéíóúüñÁÉÍÓÚÜÑ"
    if ((car>='a'and car<='z') or (car>='A' and car<='Z') or acentos  ):
        res = True
    return res

################################################################################
## Pasar a mayúscula un caracter letra
##
def carAMayu(car):
    if car>='a' and car<='z':
        car = chr(ord (car)-32)    
    return car

################################################################################
## Pasar a minúscula un caracter letra
##
def carAMinu(car): 
    if car>='A' and car<='Z':
        car = chr(ord (car)+32)    
    return car

################################################################################
## Pasar a mayúscula todas las letras de una cadena palabra
##
def palAMayu (pal):
    i=0
    palMay = ""
    while i<len(pal):
        palMay = palMay + carAMayu(pal[i])
        i=i+1    
    return palMay

################################################################################
## Identificar una palabra, es decir que todos sus caracteres sean letra
##
def esPalabra(pal):
    res = True
    i=0
    while i<len(pal):
        if not esLetra2(pal[i]):
            res=False
        i=i+1
    return res

################################################################################
################################################################################
################################################################################
################################################################################

################################################################################
## Buscar una cadena 'cad' dentro de otra cadena 'frase'
## Si la ecuentra retorna True. Si no la encuentra retorna False
##
def buscaCad(cad, frase ):                          # funcion booleana
    esta = False                                    # asumo que no esta    
    i = 0
    while i< (len(frase)-len(cad)+1) and not esta:  #(len(frase)-len(cad)+1)
        if frase[i:i+len(cad)]==cad:
            esta = True                             # la encontre           
        i = i + 1

    return esta                                     # 


################################################################################
## Contar la cantidad apariciones de cadena 'cad ' dentro de otra cadena 'frase'
## OJO ## FALLA con cad="" , Entra en un ciclo infinito
##
def contarCad2(cad, frase): ## FALLA con cad=""
    cont = 0
    i = 0
    while i<(len(frase)-len(cad)+1):  #i<(len(frase)): 
        if frase[i:i+len(cad)]==cad:
            cont = cont + 1
            i = i + len(cad)
        else:
            i = i + 1 
    return cont

################################################################################
## Contar la cantidad apariciones cadena 'cad ' dentro de otra cadena 'frase'
## version supercompleta resuelve cadena vacia
## 
def contarCad(cad, frase):       
    cont = 0
    i = 0
    if (cad!=""):
        while i<(len(frase)-len(cad)+1):
            if frase[i:i+len(cad)]==cad:
                cont = cont + 1
                i = i + len(cad)
            else:
                i = i + 1               
    elif(cad=="" and frase==""):         
        cont = 1                          # mismo comportamiento que el método
    else:                                 #      .count() de str
        cont = len(frase)+1               # mismo comportamiento que el método
                                          #      .count() de str
    return cont

################################################################################
## Retorna una cadena separada por comas con los números de indices iniciales
## en donde se encuentra cad dentro de frase
## 
def indiceCad(cad, frase ):
    res = None                                  # inicializa var de respuesta
    i = 0                                       # inicializa var indice
    if cad!="":
        while i<(len(frase)-len(cad)+1):
            if frase[i:i+len(cad)]==cad:
                #SI encontre cad en frase               
                if (res==None):                 # Armado cadena de respuesta
                    res = str(i)                # primera vez
                else:
                    res = res + "," + str(i)    # el resto de las veces                   
                i = i + len(cad)                # incremento saltando la 
                                                #    cadena encontrada
            else:
                #NO encontre cad en frase
                i = i + 1                       # incremento de a uno              
    return res

################################################################################
## Retorna una cadena de caracteres con las palabra encontradas
##     Retorna las palabras separadas por un salto de linea (\n')
##
## Recordar que:
##       Una palabra es una cadena de caracteres LETRA.
##       Un separador de palabra (para este ejemplo) es cualquier
##           caracter NO LETRA.
## 

def verPal(frase):
    res = ""
    i=0                                               # inicializar 
    largoFrase = len(frase)                           # largo de la frase
    while i<largoFrase :                              # mientras no se termine 
                                                      #     la frase       
        while i<largoFrase and not esLetra(frase[i]): # recorre lo "no" letra
            i+=1                                      # salto de a uno
           
        pal=""       
        while i<largoFrase and esLetra(frase[i]):     #recorre "lo que es" letra
            pal = pal + frase[i]                      #carga la palabra
            i+=1
           
        if pal!="": 
            #print(pal)
            res = res + pal + "\n"         
           
    return res

#cad="aron"
#frase = "# $Baron!, urgente ya ha nacido! Es un varon$$$"
