################################################################################
##  ÚLTIMA ACTUALIZACIÓN: 02/08/2022 17:30 #####################################
################################################################################
##  UNIDAD 6A -       L I S T A S    
################################################################################
##  U C A   - I N F O R M Á T I C A   G E N E R A L  ###########################
################################################################################

################################################################################
################################################################################
##     ================
## (1) L  I  S  T  A  S
##     ================
##      
##      + La lista es una secuencia MUTABLE de objetos (cualquier tipo de datos
##            válido en python).
##      + type: <class 'list'>
##      + Utiliza el CORCHETE para definirla.
##      + se puede acceder al contenido de una posición a través de su índice.
##      + Se puede acceder a una posición para leerla y/o escribirla (MUTABLE).
##      + Se puede hacer slicing.
##      + se puede agregar, eliminar elementos.
##
## **** CARACTERÍSTICAS DE LA LISTA !! ****
## -> SECUENCIA  Sucesión de elementos. En 'list' el elemento puede ser
##               cualquier tipo de dato válido de python.
##
## -> MUTABLE    Un tipo de dato es mutable cuando puede ser
##               modificado sus elementos. Es decir puedo acceder a cualquier
##               elemento de la secuencia de una lista y modificarlo.
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
##          +: (Concatena) dos listas. Y se obtiene una nueva lista
## 
##          *: (Concatena)Se utiliza para multiplicar una lista 'li' por un numero
##                 entero 'n'. La operación concatena 'n' veces a 'li'
##                 Y se obtiene una nueva lista.
##          in: Membresía) funciona el operador in (por ser secuencia) 
##              
##            
##
## -> MÉTODOS: 
##            - .append(); .insert(); .pop(); .remove()
##            - IMPORTANTE: Sólo usaremos estos métodos para listas.
################################################################################

################################################################################
## ================================================
## DOS FORMAS DE CREAR UNA LISTA (Inicializar lista)
## ================================================
## lst = []               # Forma-1. Crea lista vacía, sin valores. 
## lst = list()           # Forma-2. crea lista vacía, sin valores.
##                        #-  lst es el nombre de la variable
##                        #-  list() es la función lista
##
## ===================================================
## SE PUEDE CREAR UNA LISTA CON VALORES PREESTABLECIDO
## ===================================================
##
## lst1 = [11,22,3,460]         # crea lista con cuatro elementos.
##
################################################################################

################################################################################
## MODELO VISUAL DE UNA LISTA CARGADA EN MEMORIA
##
##
##  MODELO VISUAL de la lista 'lst1'
##
##  +------+------+------+------+
##  |  11  |  22  |   3  |  460 |    <<== CONTENIDO DE LA LISTA
##  +------+------+------+------+
##     0      1      2       3       <- Índice directo
##    -4     -3     -2      -1       <- Índice inverso
##

lst1 = [11,22,3,460]

##
################################################################################

################################################################################
## =====================
## IMPRIMIR LA LISTA lst
## =====================
##
## print(lst1)      # observar que se imprime la lista en 'formato primitivo'.
##
## =============================================================================
## IMPRIMIR CONTENIDO DE LISTA 'lst1', EL TIPO DE DATO 'type' Y EL LARGO 'Len'
## =============================================================================
##

def imprimirLista1():
    lst1 = [11,22,3,460]              # Cargar lista. O bien Incializar lista
    print(type(lst1),len(lst1), lst1) # con type obtengo el tipo de dato                      
                                      # con len obtengo cantidad elementos
                                      # La lista se impirme en formato primitivo
##                                     
################################################################################

################################################################################                     
## =============================================================                     
## UNA LISTA lst2 PUEDE CONTENER ELEMENTOS DE DISTINTO TIPO DATO
## =============================================================
## lst2 contiene elementos de distinto tipo: 'str','int','bool','float','NoneType' 
## -------------------------------------------------------------------------------
##
# ##############################################################################
# # MODELO VISUAL de la lista 'lst2'
# #
# # +--------+-------+-------+-------+-------+
# # | "abcd" |   2   |  True |  3.14 | None  |    <<== CONTENIDO DE LA LISTA
# # +--------+-------+-------+-------+-------+
# #     0        1       2       3       4        <- Índice directo
# #    -5       -4      -3      -2      -1        <- Índice inverso
#

lst2 = ["abcd",2,True,3.14,None]  # crea lista con cinco elementos
                                  # de distintos tipos
#
# #- - - - - - - - - - - - - - - - - - - -
# # DOS MODELO VISUAL de la MISMA lista 'lst2', EN VERTICAL 
# # - - - 
# #    MODELO 01        # #     MODELO 02 
# #  
# #  --+--------+       # #  --+-------------------+
# #    |        |       # #    | +---+---+---+---+ |
# # 0  | "abcd" |       # # 0  | |'a'|'b'|'c'|'d'| |
# #    |        |       # #    | +---+---+---+---+ |
# #    |        |       # #    |   0   1   2   3   |
# #  --+--------+       # #  --+-------------------+
# # 1  |   2    |       # # 1  |        2          | 
# #  --+--------+       # #  --+-------------------+
# # 2  | True   |       # # 2  |       True        |
# #  --+--------+       # #  --+-------------------+
# # 3  | 3.14   |       # # 3  |       3.14        |
# #  --+--------+       # #  --+-------------------+
# # 4  | None   |       # # 4  |       None        |
# #  --+--------+       # #  --+-------------------+
# #
##                                     
################################################################################

################################################################################
## =================================
## ACCEDER A UN ELEMENTO DE LA LISTA
## LEER UNA LISTA
## ================================= 
##

def leerLista3():
    lst3=[23,3.14,22,"hola",99]
    pos=2
    print(lst3[pos])      #  22
    pos=3
    print(lst3[pos])      #  hola
    print(lst3[pos][0])   #  h   
    
    # pos es el índice (la posición)
    # DEBE SER: pos >=0 and pos < len(lst3) 
    #           caso contrario pos estará fuera de rango
    #           y será un error en ejecución
                       
##                                     
################################################################################

################################################################################
## ==================
## RECORRER UNA LISTA
## ==================
# ##

lst3 =[23,3.14,22,"hola",99]

# ## ------------------------------------------------------
# ## RECORRER lista con while ( Utiliza índice en la lista)
# ## ------------------------------------------------------
# ##

def recorrerListaWhile(lst3):
    print(" - - while - -  -")
    i=0
    while(i<len(lst3)):
        print(lst3[i])
        i+=1
         
# ## ------------------------------------------------------
# ## RECORRER lista con for ( Utiliza índice en la lista)
# ## ------------------------------------------------------
# ##

def recorrerListaFor(lst3):
    print(" - - for - -  -")
    for i in range(0,len(lst3)):  
        print(lst3[i])
 
# ## ------------------------
# ## RECORRER lista con for (Sin utilizar índice en la lista)
# ## ------------------------

def recorrerListaFor2(lst3):
    print(" - - for 2- -  -")
    for x in lst3:  
        print(x)                       
##                                     
################################################################################

################################################################################
## =============================================
## S L I C I N G    O    S L I C E CON UNA LISTA
## =============================================
## Vale para listas todo lo que vimos en string sobre slicing
## -----------------------------------------------------------------------------
## 
## variableLista[start : stop : step]
##
## -> Slicing es el mecanismo de obtener partes "rebanadas" de un secuencia
##
## EJEMPLOS:
        
def sliceLst():
    lst4=[1,2,3,4,5,6,7,8]
    print(lst4[0:3])             # [inicio: fin]
    print(lst4[1:4])             # [inicio: fin]
    print(lst4[1:])              # [inicio: ] # desde inicio , hasta "el final"
    print(lst4[1:len(lst4)])     # Idem anterior
    print(lst4[:4])              # [ : fin]   # desde "principio", hasta fin
    print(lst4[:])               # [ : ]      # desde "principio", hasta "el final"
    ##print(lst4[])              # error !!! No puede quedar vacío entre los
                                 #           corchetes
    
    print(lst4[1:len(lst4):3])   # [inicio: fin : salto]    
    print(lst4[0:len(lst4):1])   # [inicio: fin : salto]
    print(lst4[::])              # idem anterior
         
    print(lst4[-1])              # Devuelve el último elemento de la lista. 
                                 #     idem a print(lst4[len(lst4)-1])
                                 
    print(lst4[:-1])             # devuelve todos menos el último.                             
    print(lst4[::-1])            # devuelve toda cadena invertida
    
##                                     
################################################################################

################################################################################
## =================================
## OPERADOR 'IN' LISTA
## =================================
## Devuelve True si un elemento se encuentra dentro de una lista
## -----------------------------------------------------------------------------

def inLst():
    lst4=[1,2,3,4,5,6,7,8]  # 
    print(5 in lst4)        # Devuelve True
    print(5 not in lst4)    # Devuelve False
    print(87 not in lst4)   # Devuelve True

################################################################################
## =================================
## M U T A B L E   LISTA
## ESCRIBIR/MODIFICAR UN ELEMENTO DE LA LISTA
## =================================
## La lista admite que se modifique su contenido con una asignación
## Debe existir la posición
## ----------------------------------------------------------------------------
##

def cambiarElementoLst():
    lst1 = ["ES","MU","TA","BLE"]
    print(" - - - - CAMBIAR CONTENIDO - - - -")
    print("antes   ->",lst1)
    lst1[0]="es"                  # PERMITE ASIGNACIÓN, modificación en una
                                  # posición "esto es una forma de MUTABILIDAD"
    print("despues ->",lst1)
    print(" - - - - - - - - - - - - - - - - -")


################################################################################
## =================================
## CONCATENAR  LISTA
## =================================
##
    
def concatenarLst():
    lsA=[1,2,3]
    lsB=["a","b"]
    lsC=lsA+lsB                      # Se crea una nueva lista lsC resultado de
                                     # concatenar lsA con lsB
    print("lista concatenada 1 ->",lsC)
    
    lsD=lsB*2                        # Se crea una nueva lista lsD resultado de
                                     # concatenar 2 veces a lsB
    print("lista concatenada 2 ->",lsD)


################################################################################
## =============================================================================
## REFERENCIA a un LISTA
## Una LISTA está REFERENCIADA a otra cuando ambas  apuntan(id) a la misma LISTA
## Para el caso, lsUno y lsDos comparten el mismo id y por tanto son DEPENDIENTES
## DEPENDIENTES: Cualquier modificación que se realiza desde una variable afectará
##               el contenido de la otra
## =============================================================================
## PROBAR el código en pythontutor
## https://pythontutor.com/visualize.html#mode=edit
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##

def referenciaLst():
    lsUno=["a","b"]               # Inicializar  una lista con datos
    lsDos=lsUno                   # Asignar una lista a otra lista ..
                                  #   se asignan los id, no los contenidos

    print("lsUno","->",id(lsUno),"->",lsUno)
    print("lsDos","->",id(lsDos),"->",lsDos)
                                  # Se puede observar que ambas variables
                                  # tienen el mismo 'id'

################################################################################
## =============================================================================
## COPIA de un LISTA
## Una LISTA es copia de otra cuando apuntan(id) a distintas LISTAS
## pero sus contenidos son los mismos.
## Para el caso,  lsTres y lsCuatro son COPIA por tanto son INDEPENDIENTES
## INDEPENDIENTES: Cualquier modificación que se realiza desde una variable
##                 NO se afectará el contenido de la otra                            
## =============================================================================
## PROBAR el código en pythontutor
## https://pythontutor.com/visualize.html#mode=edit
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##

def copiaLst1():
    lsTres=["a","b"]                  # Inicializar una lista con datos
    lsCuatro=[] + lsTres              # Se copia el  contenido: La concatenación
                                      # devuelve una nueva lista 
    print("lsTres","->",id(lsTres),"->",lsTres)
    print("lsCuatro","->",id(lsCuatro),"->",lsCuatro)
                                      # Se puede observar que ambas variables
                                      # tienen distintos 'id'

def copiaLst2():
    # OTRA FORMA DE COPIAR
    lsTres=["a","b"]                  # Inicializar una lista con datos
    lsCuatro=lsTres[:]                # Se copia el  contenido: con slicing
    
    print("lsTres","->",id(lsTres),"->",lsTres)
    print("lsCuatro","->",id(lsCuatro),"->",lsCuatro)
    

################################################################################
################################################################################
################################################################################
## =======================================
## O P E R A C I O N E S  CON L I S T A S
## =======================================
##
## A B M C (CRUD)
## A(C) : Alta     (Create) ->  Agregar / Insertar ( .append(); .insert() )
## B(D) : Baja     (Delete) ->  Borrar / Eliminar  ( .pop() ; .remove() )
## M(U) : Modifica (Update) ->  Actualizar         ( lst[pos]=nuevovalor )
## C(R) : Consulta (Read)   ->  Leer               ( lst[pos] )
## ======================================================================== 
## ****************************************************************
##
##  .append()    - >  Agrega elemento 'ele' al final de la lista.
##                    - NO Retorna nada (None)
##                    - FORMATO =>   .append(ele)
##
##  .insert()    - >  Inserta elemento 'ele' en posición 'pos' indicada.
##                    - NO Retorna nada (None)
##                    - Posición por defecto: NO TIENE
##                    - FORMATO =>   .insert(pos,ele)
##
##  .pop()       - >  Elimina un elemento de un posición 'pos'indicada.
##                     - Retorna valor 'ele' que es el eliminado.
##                     - Prerrequisito: lista no vacía e indices dentro del rango
##                        + Si lista está vacía entonces => ERROR
##                        + Si el indice fuera de rango entonces  => ERROR
##                     - La posición defecto: "la ultima"                   
##                    
##                     - FORMATO =>  .pop('pos') -> 'ele'
##                     - FORMATO =>  .pop()      -> retorna el elemento de la   
##                                                  ÚLTIMA posición, que es la
##                                                  que elimina.
##
##  .remove()    - >  Elimina ELEMENTO 'val' pasado por parámetro. Es
##                    decir, elimina por valor.
##                     - NO Retorna nada (None)
##                     - Prerrequisito:
##                        + El elemento 'val' debe existir dentro de la lista.
##                        + Si elemento no está en la lista entonces => ERROR
##                     - FORMATO =>  .remove(val)
## ****************************************************************
## PROBAR el código en pythontutor
## https://pythontutor.com/visualize.html#mode=edit
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##

## Las siguientes cuatro funciones recibe por parámetro una lista
## más abajo en la función abmcLst() se ponen a estas cuatro funciones juntas
## OBSERVAR el comportamiento de lst dentro de la función abmcLst()

def agregarEnLista(lst):
    #"AGREGAR EN LISTA"
    lst.append(10)
    lst.append(2)
    lst.append(9)
    lst.append(40)
    lst.append(25)
    lst.append(6)

def insertarEnLista(lst):
    #INSERTAR EN LISTA
    ele1= True
    ele2= "chau"
    ele3= "hola"
    pos=3
    lst.insert(pos,ele1)          # inserto en alguna 'pos' (en medio) de la lista"
    lst.insert(len(lst),ele2)     # inserto al final  (atrás) de la lista
    lst.insert(0 ,ele3)           # inserto al inicio (adelante) de la lista

def eliminarEnListaPorPosicion(lst,pos):
    ## ELIMINAR POR POSICIÓN
                                  # 'pos' posición a eliminar
    res=None                      # inicializar variable respuesta en None
    if pos >=0 and pos<len(lst):  # si lista no está vacía y 'pos' dentro de rango
        res = lst.pop(pos)        # ELIMINA posición pos y captura valor eliminado
    return res                    # en 'res' se encuentra el valor eliminado
                                  #   o bien None si 'pos' fuera de rango

def eliminarEnListaPorValor(lst,val):
    ## ELIMINAR POR VALOR
    if val in lst:                # Se valida que 'val' se encuentre en 'lst'
        lst.remove(val)           # se elimina 'val' en 'lst'

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - -  - - - -
## PROBAR el código en pythontutor
## https://pythontutor.com/visualize.html#mode=edit
        
def abmcLst():
    # Todas las funcionalidades abmc juntas 
    lst=[]
    print("Partimos de una lista vacía")
    print("\t1 -> ",lst)
    agregarEnLista(lst)                     # la función agrega elementos a lst
    print("Agrego elemento a lst")
    print("\t2 -> ",lst)
    insertarEnLista(lst)                    # la función inserta elementos en lst
    print("Inserto tres elemento a lst")
    print("\t3 -> ",lst)
    pos=3
    x1 = eliminarEnListaPorPosicion(lst,pos)# la func. elimina de la posic. 'pos'
    print("Elimino de posición",pos,"el elemento",x1, "de lst")
    print("\t4 -> ",lst)
    val=40
    eliminarEnListaPorValor(lst,val)        # la función elimina el valor 'val'
    print("Elimino por valor el elemento",val, "de lst")
    print("\t5 -> ",lst)
    
##-       - -       - -       - -       - -       - -       - -       - -       - 
## IMPORTANTE: Observar que las funciones no tienen retorno y sin embargo podemos
##             visualizar en abmcLst() el contenido de la lista lst con los 
##             cambios ocurridos dentro de cada función.
##             Esto de debe a que el tipo de dato lista <list> cuando se pasan por 
##             parámetro lo hace "por referencia" y no "por valor" (como los tipos  
##             que conocíamos hasta ahora).
##             Por ejemplo: cuando desde abmcLst() se invoca a agregarEnLista(lst), 
##                          la función recibe el mismo id del lst que se encuentra  
##                          en la función abmcLst(). En definitiva dentro de la 
##                          función agregarEnLista() hay un REFERENCIA A lst que se  
##                          encuentra dentro la función abmcLst()
################################################################################

################################################################################
################################################################################    
## F U N C I O N E S
## + PASAJE DE PARÁMETRO "POR VALOR"
## + PASAJE DE PARÁMETRO "POR REFERENCIA"
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##
##         POR VALOR: Significa que se hace una transferencia del valor de los 
##                    datos, es decir del contenido de la variable.
##                    En python es equivalente a decir que se genera 
##                    dentro de la función que es llamada, una variable con una  
##                    COPIA del contenido de la variable que se encuentra en 
##                    el contexto donde se llamó a la función y se le paso el 
##                    parámetro. Los pasajes por valor tienen comportamiento 'in'
##                    
##                    Los tipos de datos que funcionan de esta manera y que se
##                    utilizan en la materia son :
##                     <int>, <float>, <str>, <bool>, <NoneType>, <tuple>, <range>
##
##         POR REFERENCIA: Significa que se hace una transferenCia de una 
##                         dirección de donde se encuentra los datos, es decir 
##                         la dirección del contenido de la variable.
##                         En python se transfiere el id de la variable.
##                         
##                         Por tanto, en python es equivalente a decir que se 
##                         genera dentro de la función que es llamada, una  
##                         variable que tiene la REFERENCIA al contenido de la variable 
##                         que se encuentra en el contexto donde se llamó a la 
##                         función y se le pasó el parámetro.
##                    
##                         Los pasajes por referencia pueden tener
##                         comportamiento 'in' o 'out' o 'inout' 
##                         Los tipos de datos que funcionan de esta manera y 
##                         se utilizan en la materia son :                         
##                         <list>, <dict>                     
################################################################################
    
################################################################################
##    CARGA UNA LISTA CON VALORES ALEATORIOS
## ---------------------------------------
## PROBAR el código en pythontutor
## https://pythontutor.com/visualize.html#mode=edit
##
 
import random
## ls: lista donde se cargan los números
## cant: cantidad de números que se cargaran en la lista
## ini: valor inicial del intervalo para generar números aleatorios
## fin: valor final del intervalo para generar números aleatorios
def cargarListaAle_01(ls,cant,ini,fin):    
    for i in range(0,cant):
        valAle = random.randint(ini,fin)
        ls.append(valAle)   
def pruebaLstAle():
    # Prueba la carga de una lista con valores aleatorios
    lst=[]
    print("Antes->:",lst)
    cargarListaAle_01(lst,5,10,100)
    print("Después->:",lst)

################################################################################
##    O R D E N A R
##    UNA LISTA
    
## Para lograr ordenar una lista debemos poder comparar todos los elementos
## contra todos. En la comparación, que se hace uno a uno, hay
## que determinar quién está primero y quien último en el orden que se ente
## procesando.
## La idea que se propone en la cátedra es la de realizar algoritmos que ordene
## una lista sin generar una lista copia auxiliar para hacerlo.
## Si bien hay muchos algoritmos para hacer ordenamiento, aquí proponemos uno
## totalmente genérico, similar al algoritmo denominado
## 'ordenamiento por selección'.
## ---------------------------------------
## PROBAR el código en pythontutor
## https://pythontutor.com/visualize.html#mode=edit
##

def ordenarLst(ls):
    #ordena de menor a mayor lst[i] > lst[j]
    for i in range(0,len(ls)-1):
        for j in range(i+1,len(ls)):
            if ls[i]>ls[j]:        #intercambio de elementos
                aux = ls[i]
                ls[i] = ls[j]
                ls[j] = aux
     
################################################################################
################################################################################


################################################################################
################################################################################
  
def cargarListaAle_02(lst):
    # carga lista con valores aleatorios hasta que
    # sale el aleatorio 0(cero)    
    ele = random.randint(0,10)      
    while(ele!=0):                   
        lst.append(ele)              
        ele = random.randint(0,10)   

def eliminarEnLista_02(lst, val):
    # elimina todas las ocurrencias , es decir
    # todas las veces que aparece 'val' en 'lst'
    i = 0 
    while (i<len(lst)):
        if lst[i] == val:
            lst.pop(i)                # elimina por posición
            # i+=1 #"NOOOOOOOOO"   <- porque al eliminar ya tiene un elemento
                   #                  menos (el indice se corrió al eliminar)
        else:
            i+=1
            
    ## IMPORTANTE: No utilizar el for para eliminar elemento en una lista 
    ##             por posición; dado que lo que entrega el range es un inmutable
    ##             por tanto no modifica su tamaño al eliminar elementos
            
def eliminarEnLista_03(lst, val):
    # recorre toda la lista y borra cuando encuentra el valor 'val'
    for x in lst:
        if val in lst:
            lst.remove(val)
            
def eliminarTodoEnLista(lst):
    # Elimina todos los elementos de una lista
    while(len(lst)>0):
        lst.pop()
            
################################################################################
################################################################################
## CONVERSIÓN DE TIPOS
## - - - - - -  - - - -
## de <??> a <list>
##     Para convertir un tipo de dato a lista, el tipo de dato a convertir 
##     debe ser iterable. Se pueden convertir a lista el <str>, <tuple> y <range>
##                       <dict> también, pero parcialmente ya que solo convierte
##                              las claves; se verá más adelante.
##
## de <list> a <??>
##     Una lista se puede convertir a <str>, <tuple>
##
################################################################################




