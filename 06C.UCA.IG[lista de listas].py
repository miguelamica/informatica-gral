################################################################################
##  ÚLTIMA ACTUALIZACIÓN: 02/08/2022 17:40 #####################################
################################################################################
##  UNIDAD 6A -       L I S T A S  D E  L I S T A S
################################################################################
##  U C A   - I N F O R M Á T I C A   G E N E R A L  ###########################
################################################################################

################################################################################
################################################################################
## =======================================
## L I S T A S  DE  L I S T A S
## =======================================
##
## Es una lista donde cada elemento está compuesto por otra lista (sublista)
## La sublista puede tener 1,2 3, ..etc elementos
##

################################################################################
## lstA=[[]]         # Inicialización en vacío de una lista de lista
##                   # Es una lista que contiene otra lista que está vacía
##
## 

## Imaginemos una lista, donde cada sublista contien
## una cantidad y el nombre de un alimento.
lstA=[[10,"Peras"],[7,"Frutillas"],[2,"Almendras"],[4,"Limones"]]
     

##- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
##  DOS MODELO VISUAL de la lista 'lstA', EN VERTICAL
##
##                C  O  L  U  M  N  A
##       
##
##      |   0   |                  1                        |
##    --+-------+-------------------------------------------+
#       |       | +---+---+---+---+---+                     |
# F  0  |   10  | |'P'|'e'|'r'|'a'|'s'|                     |
#       |       | +---+---+---+---+---+                     |
#       |       |   0   1   2   3   4                       |
# I   --+-------+-------------------------------------------+
#       |       | +---+---+---+---+---+---+---+---+---+     |
#    1  |   7   | |'F'|'r'|'u'|'t'|'i'|'l'|'l'|'a'|'s'|     |
# L     |       | +---+---+---+---+---+---+---+---+---+     |
#       |       |   0   1   2   3   4   5   6   7   8       |
#     --+-------+-------------------------------------------+
# A     |       | +---+---+---+---+---+---+---+---+---+     |
#    3  |   2   | |'A'|'l'|'m'|'e'|'n'|'d'|'r'|'a'|'s'|     |
#       |       | +---+---+---+---+---+---+---+---+---+     |
#       |       |   0   1   2   3   4   5   6   7   8       |
#     --+-------+-------------------------------------------+
#       |       | +---+---+---+---+---+---+---+             |
#    4  |   4   | |'L'|'i'|'m'|'o'|'n'|'e'|'s'|             |
#       |       | +---+---+---+---+---+---+---+             |
#       |       |   0   1   2   3   4   5   6               |
##    --+-------+-------------------------------------------+
## 
## A cada línea se la conoce como fila o registro
## A cada elemento de una línea se lo conoce como celda o campo
##
##

################################################################################
def cargarLstA(ls):    
    alimento = "Peras"
    cantidad = 10
    ls.append([cantidad,alimento])
    alimento = "Frutillas"
    cantidad = 7
    ls.append([cantidad,alimento])
    alimento = "Almendras"
    cantidad = 2
    ls.append([cantidad,alimento])
    alimento = "Limones"
    cantidad = 4
    ls.append([cantidad,alimento])
    
def imprimirLstA(ls):
    for x in ls:
        fila = "|{:4} |{:14} |".format(x[0],x[1])
        print(fila)
    print()
    
def ordenarLstA(ls):
    #ordena de menor a mayor lst[i] > lst[j]
    # Ordena por el columna 1
    col=1
    for i in range(0,len(ls)-1):
        for j in range(i+1,len(ls)):
            if ls[i][col]>ls[j][col]:      #intercambio de elementos
                aux = ls[i]
                ls[i] = ls[j]
                ls[j] = aux
    
    ## Ojo, si ordena caracteres debe tener en cuenta la mayúscula y minúscula
    ## En este caso funciona porque todas las cadenas tiene un mayúscula en 0
                
def main_01():
    ls=[]                         #Inicializar lista en vacío
    cargarLstA(ls)                #Carga Lista
    print("lista Original")
    imprimirLstA(ls)
    ls.pop(2)                     # elimina la posición 2
    ls.insert(0,[22,"Aceitunas"]) # inserta en posición 0
    print("lista Modificada")
    imprimirLstA(ls)

    ordenarLstA(ls)               # ordenar lstA por columna 1
    print("lista Ordenada por Alimento")
    imprimirLstA(ls)
    
   
###############################################################
#     Imaginemos ahora una lista donde cada sublista la componen
#     el dni del estudiante, el nombre del estudiante y una 
#     lista de 3 notas de exámenes parciales 
lstAlu=[[11,"Thomas","Pool",['A','A','A']],
        [222,"Juan","Lith",['A','A','D']],
        [33,"Maria","Zul",['D','A','D']],
        [44,"Juana","Charo",['D','D','D']]
       ]

##- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
##  MODELO VISUAL de la lista 'lstAlu', EN VERTICAL
##
##                C  O  L  U  M  N  A
##       
##      |   0   |     1      |    2     |        3         |
##    --+-------+------------+----------+------------------+
#       |       |            |          | +---+---+---+    |
# F  0  |  11   | "Thomas"   |  "Pool"  | |'A'|'A'|'A'|    |
#       |       |            |          | +---+---+---+    |
#       |       |            |          |   0   1   2      |
#     --+-------+------------+----------+------------------+
#       |       |            |          | +---+---+---+    |
# I  1  |  22   | "Juan"     |  "Lith"  | |'A'|'A'|'D'|    |
#       |       |            |          | +---+---+---+    |
#       |       |            |          |  0   1   2       |
##    --+-------+------------+----------+------------------+
#       |       |            |          | +---+---+---+    |
# L  2  |  33   | "Thomas"   |  "Zul"   | |'D'|'A'|'D'|    |
#       |       |            |          | +---+---+---+    |
#       |       |            |          |   0   1   2      |
##    --+-------+------------+-----------------------------+
#       |       |            |          | +---+---+---+    |
# A  3  |  44   | "Juana"    |  "Charo" | |'D'|'D'|'D'|    |
#       |       |            |          | +---+---+---+    |
#       |       |            |          |   0   1   2      |
#     --+-------+------------+----------+------------------+


## RECORRIDO de la lista lstAlu, imprimiendo con formato

def imprimirLstAlu(lstAlu):    
    tabla=" | {:^4} | {:^12} | {:^4} | {:^9} |\n".format("DNI","APELLIDO","NOM","NOTAS")
    for x in lstAlu:
        dni = "{:4}".format(x[0])      # dni
        ape = "{:12}".format(x[2])     # Apellido completo
        nom = "{:4}".format(x[1][0])   # Solo la primer letra del Nombre
        ex=""
        for nota in x[3]:
            ex= ex+"{:3}".format(nota) # las notas del examen
            
        fila = " | "+dni+" | "+ape+" | "+nom+" | "+ex+" | "+"\n"
        tabla=tabla+fila        
    print(tabla)


#############################################################################
##    Cargar en una lista una matriz de 5 filas x 4 columnas que contengan
##    números enteros aleatorios entre 0 y 200.
##    Luego se imprime la matriz con formato.
##
#

import random

def imprimirMatriz(ls):
    res=""
    for f in range(0,len(ls)): 
        for c in range(0,len(ls[0])):
            res = res +  "{:6}".format(ls[f][c])
        res=res+"\n"
    print(res)
    
    
def cargarMatrizAle(nFil,nCol):
    #retorna una lista  de lista 'ls' con la matriz cargada con aleatorios
    ls=[]                        # lista a retornar       
    for f in range(0,nFil):
        auxF=[]                  # lista auxiliar Para cargar la Fila  
        for c in range(0,nCol):
            val= random.randint(0,200)
            auxF.append(val)
        ls.append(auxF)          # cargo la fila en la lista matriz
            
    return ls

def main_02():
    ls = cargarMatrizAle(5,4)
    imprimirMatriz(ls)
    
    
    
    
