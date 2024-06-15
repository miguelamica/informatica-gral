################################################################################
##  ULTIMA ACTUALIZACIÓN: 25/10/2022 10:30 #####################################
################################################################################
##  UNIDAD 6D -        D I C C I O N A R I O S
################################################################################
##  U C A   - I N F O R M Á T I C A   G E N E R A L  ###########################
################################################################################
##  
################################################################################
################################################################################

################################################################################
################################################################################
## =======================
## D I C C I O N A R I O S
## =======================
##      + type: <class 'dict'>
##      + Es una secuencia MUTABLE de elementos que son pares 'clave':'valor'
##        - La 'clave' debe ser un objeto INMUTABLE ( int, float, str, bool, tuple)
##        - El 'valor' puede ser cualquier tipo de datos válido en python.
##
##      + Se utiliza la llAVE {} para definir un diccionario
##      + Formato del diccionario -> {clave0:valor0,...,claveN:valorN}
##      + La 'clave' NUNCA se repite, es decir sólo aparece una vez en el diccionario
##      + El 'valor' puede repetir varias veces.
##
##      + Se puede acceder al contenido de un 'valor' a través de su 'clave'
##      + Se puede acceder a una 'clave' para leer y/o escribir(MUTABLE) su 'valor' 
##
##      + Se puede agregar o eliminar pares 'clave':'valor' (MUTABLE)
##      + La función len() retorna la cantidad de elementos de un diccionario
##
## **** CARACTERÍSTICAS DEL DICCIONARIO !! ****
## -> SECUENCIA  Sucesión de elementos. En 'dict' el elemento es
##               el par clave<->valor
##
## -> MUTABLE    Un tipo de dato es mutable cuando puede ser
##               modificado sus elementos. Es decir puedo acceder a cualquier
##               elemento de la secuencia de una lista y modifircarlo.
##               
## -> ITERABLE  (Que puede ser recorrido "con un ciclo")
##               Las secuencias en python son iterables
##
## -> LONGUITUD: (o largo) Es la cantidad de elementos que contiene el
##                         diccionario.
##
## -> Función len(): - SOLO se aplica a una SECUENCIA
##                   - Obtiene la cantidad de elementos de la secuencia
##
## -> OPERADORES: 
##
##          in: (Membresía) funciona el operador in (por ser secuencia)
##                          in devuelve True si el elemento buscado se
##                             se encuentra en la lista de claves del
##                             diccionario
##                          ejemplo: ->  <elemento> in <diccionario>         
##            
## -> MÉTODOS:
##            - .get(); pop(); .keys(); .values()
##            - IMPORTANTE: Sólo usaremos estos métodos para listas.
################################################################################

################################################################################
## =============================================================
## DOS FORMAS DE CREAR UN DICCIONARIO (Inicializar DICCIONARIO)
## =============================================================
## dic = {}               # crea diccionario vacío, sin valores. 
## dic = dict()           # crea diccionario vacío, sin valores. 
##                        # dic es el nombre de la variable
##                        # dict() es la función diccionario
##
## =============================================================
## SE PUEDE CREAR UN DICCIONARIO CON VALORES PREESTABLECIDO
## =============================================================
##
## # crea DICCIONARIO con tres elementos (pares claves:valor).
##
## di = {10:"Claudia",20:"Lara",3:"Juan",69:"Agustina"}
##
## len(di) # total de elementos del diccionario
################################################################################

di = {10:"Claudia",20:"Lara",3:"Juan",69:"Agustina"}


################################################################################
##- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## MODELO VISUAL  ir a python
## https://pythontutor.com/
##- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 
## # Acceder al siguiente link para ver el modelo visual de un diccionario
## 
## https://pythontutor.com/render.html#code=di%20%3D%20%7B10%3A%22Claudia%22,20%3A%22Lara%22,3%3A%22Juan%22,69%3A%22Agustina%22%7D&cumulative=false&curInstr=1&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
##- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
################################################################################
    

################################################################################
## LEER DICCIONARIO
##
def leerDic():
    print("Acceso con indice usando 'corchete'")
    print("OJO debe existir la clave, sino hay error")
    print("Para clave {}, el valor es {}".format(k,di[k]))
    print()
    print("Acceso con indice usando '.get'")
    print("Si la clave no existe, entocens retorna None")    
    print("\t\tPara clave {}, el valor es {}".format(k,di.get(k)))

    #print(di[11])  # ojo que rompe cuando no se encuentra la clave en 
                    # el diccionario cuando se usa acceso con corchete
                    # Hay que usar .get para que no genero un error


################################################################################
################################################################################
## ==================================================
## O P E R A C I O N E S  CON D I C C I O N A R I O S
## ==================================================
##
## A B M C (CRUD)
## A(C) : Alta     (Create) ->  Agregar / Insertar ( di[<clave>] = <valor> )
## B(D) : Baja     (Delete) ->  Borrar / Eliminar  ( di.pop(<clave>)       )
## M(U) : Modifica (Update) ->  Actualizar         ( di[<clave>] = <valor> )
## C(R) : Consulta (Read)   ->  Leer               ( di[<clave>] ; di.get(<clave>)
## ======================================================================== 
## ****************************************************************
##
################################################################################
## ALTA BAJA MODIFICACION CONSULTA EN UN DICCIONARIO
##
##  ALTA          - >  Agrega elemento 'par clave-valor' al diccionario 'di'
##                     Se utiliza la asignación.
##                     Si la clave NO EXISTE entonces la crea y le asigna valor.
##                     Si la clave EXISTE entonces modifica el valor (VER MODIF.).
##                     - FORMATO =>   di[<clave>] = <valor>
##
##  MODIFICACION  - >  Modifica valor  de un clave asociada al diccionario 'di'
##                     Se utiliza la asignación.
##                     Si la clave EXISTE entonces modifica el valor.
##                     Si la clave NO EXISTE entonces la crea 
##                         y le asigna valor (VER ALTA).
##                     - FORMATO =>   di[<clave>] = <valor> 
##
##  ELIMINAR      - >  Elimina elemento 'par clave-valor' del diccionario 'di'.
##                     Se Utiliza el método '.pop()'
##                     Método '.pop()'
##                          + Se le pasa la clave y elimina el 'par clave valor',
##                               y retorna el valor asociado a la clave eliminada
##                          + La clave debe EXISTIR en el diccionario, sino
##                                da ERROR
##                     - FORMATO =>   di.pop(<clave>)
##
##  CONSULTA      - >  Leer elemento 'par clave-valor' del diccionario 'di'.
##                     HAY dos formas
##                    (1) Utilizando la asignación:
##                        + Devuelve el valor de la clave asociada
##                        + OJO!!, si la clave NO EXISTE entonces da ERROR.
##                        + FORMATO =>   di[<clave>]
##
##                    (2) Utilizando el método '.get()':
##                        + Devuelve el valor de la clave asociada
##                        + Si la clave NO EXISTE entonces devuleve None.
##                        + FORMATO =>   di.get(<clave>)
################################################################################                       
                    
def abmcDic(di):
    print("ORIGINAL:",di)
    #ALTA - Agregar un elemento par clave-valor
    di[102]='Lucia'
    print("DESPUES DEL ALTA:",di)
    #MODIFICACION - Cambia el valor asociado a una clave
    di[3]='Juan Carlos'
    print("DESPUES DE LA MODIFICACION:",di)
    #ELIMINACION - Elimina par clave-valor apartir de la clave
    di.pop(20)
    print("DESPUES DE LA ELIMINACION:",di)
    #CONSULTA - Leer un par clave-valor apartir de la clave
    print("En la clave {} se encuentra el valor {}".format(10,di[10]))
 
    
################################################################################
## OBTENER LAS CLAVES DE UN DICCIONARIO
##
def clavesDic(di):
    di.keys()              # es un iterable que contiene solo las claves del dict
    res = list(di.keys())  # es una lista que contiene solo las claves del dict
    print("Lista de Claves:",res)
    
################################################################################
## OBTENER LOS VALORES DE UN DICCIONARIO
##
def valoresDic(di):
    di.values()            # es un iterable que contiene solo los valores del dict
    res=list(di.values())  # es una lista que contiene solo los valores del dict
    print("Lista de Valores:",res)
 

################################################################################
## RECORRER UN DICCIONARIO
       
## ----------------------------------------------------------------------
## RECORRER diccionario con while ( Utiliza índice en la lista de claves)
## ----------------------------------------------------------------------
def recorreDictW(di):
    i=0
    lsClaves = list(di.keys()) 
    while i<len(lsClaves):
        print("{:4}:{:12}".format(lsClaves[i],di[lsClaves[i]]))
        i+=1
        
## ----------------------------------------------------------------------
## RECORRER diccionario con for ( Utiliza índice en la lista de claves)
## ----------------------------------------------------------------------
def recorreDictF(di):
    lsClaves = list(di.keys()) 
    for i in range(0,len(lsClaves)):
        print("{:4}:{:12}".format(lsClaves[i],di[lsClaves[i]]))
        

## ----------------------------------------------------------------------
## RECORRER diccionario con for ( NO Utiliza índice )
## ----------------------------------------------------------------------
def recorreDictF2(di):
    for  clave in di :   # idem -> for  clave in di.keys():
        print("{:4}:{:12}".format(clave,di[clave]))
 
################################################################################


################################################################################
## RETORNA COPIA DE UN DICCIONARIO
def copiarDic(di):
    diCopia={}
    for  clave in di : 
        diCopia[clave] = di[clave]
    return diCopia

################################################################################
## REFERENCIA y COPIA de un DICCIONARIO
################################################################################
## =============================================================================
## REFERENCIA a un DICCIONARIO
## Un DICCIONARIO esta REFERENCIADO a otra cuando ambas apuntan al mismo 'id'
##
## COPIA de un DICCIONARIO
## Un DICCIONARIO es copia de otro cuando tienen el mmismo contenido 
## pero apuntan a distintos 'id'
##
## PROBAR el código en pythontutor
## https://pythontutor.com/visualize.html#mode=edit
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##
def copiarDic(di):
    diCopia={}
    for  clave in di : 
        diCopia[clave] = di[clave]
    return diCopia

def main_copiarDic():
    di = {10:"Claudia",20:"Lara",3:"Juan",69:"Agustina"}
    refDi = di              # REFERENCIA
    copiaDi = copiarDic(di) # COPIA
    print(id(di))
    print(id(cloneDi))
    print(id(copiaDi))
#main_copiarDic()

################################################################################
## C O N C L U S I O N
## *********************************************************************
## *********************************************************************
## I M P O R T A N T E:
## OBSERVAR QUE UN DICCIONARIO SE PASA POR REFERENCIA A UNA FUNCIÓN
## *********************************************************************
## *********************************************************************
       
################################################################################
## ELIMINAR ELEMENTO DE UN DICCIONARIO
def eliminaEleDicXClave(di,clave):
    valor=None
    if di.get(clave)!=None:
        valor = di.pop(clave)
    return valor

################################################################################
## VACIAR  UN DICCIONARIO
def vaciarDic(di):
    lstClaves = list(di.keys())
    for clave in lstClaves : 
        di.pop(clave)
       
################################################################################
## EJEMPLOS DE USO
################################################################################

def cargarDicPersonas(di):
    #{dni:[apellidos,nombres], ..., dni2:[apellidos2,nombres2] }    
    di[123]=["Altusia","Mauro"]
    di[364]=["Lopez","Andrea"]
    di[796]=["Martinez","Luis"]
    di[633]=["Trigo","Marina"]
    
def mostrarPersonas(di):
    i=0
    lstClaves = list(di.keys())
    titulo="{:<5s}{:12s}{:12s}".format("DNI","APELLIDO","NOMBRE")
    print(titulo)
    print(".........................")
    while(i<len(lstClaves)):
        clave = lstClaves[i]  # dni
        lstValor = di[clave]  # valor asociado a la clave
        nom = lstValor[1]
        ape = lstValor[0]              
        fila = "{:<5d}{:12s}{:12s}".format(clave,ape,nom)
        print(fila)
        i+=1
# def main():
#     di={}
#     cargarDicPersonas(di)
#     mostrarPersonas(di)
# 
# main()
        
################################################################################
################################################################################
     
        