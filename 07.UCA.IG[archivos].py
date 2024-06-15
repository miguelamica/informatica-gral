################################################################################
##  ÚLTIMA ACTUALIZACIÓN: 02/08/2022 17:55 #####################################
################################################################################
##  UNIDAD 7 -       A R C H I V O S   D E   T E X T O 
################################################################################
##  U C A   - I N F O R M Á T I C A   G E N E R A L  ###########################
################################################################################

################################################################################
################################################################################


"""
 E L  A R C H I V O
 Un ARCHIVO es un conjunto de bytes (secuencias de ceros y unos) que son
 almacenados en un dispositivo.  Un archivo es identificado por un NOMBRE
 y la descripción de la carpeta que lo contiene.
 
 En los ARCHIVO DE TEXTO los bytes representan CARACTERES (letras, números
 y signos de puntuación incluyendo espacios en blanco y caracteres especiales
 "tabulaciones ('\t'), salto de línea y retorno de carro. ('\n')").
 
 Los CARACTERES de los ARCHIVO DE TEXTO  que trabajaremos están codificados
 en ASCII
"""

"""
  E L  A R C H I V O  Y  P Y T H O N
  
   
    A) APERTURA DE UN ARCHIVO 
  
    open  -> Función para Abrir un archivo. Genera "una conexión lógica"
             entre el archivo físico y la variable que en python
             representará a dicho archivo. Tiene dos Parámetros
                1) El NOMBRE_DEL_ARCHIVO_EN_DISPOSITIVO (es un string).
                   Se suele colocar un nombre amigable que permita
                   identificar fácilmente al archivo dentro del código
                2) El MODO_DE_APERTURA (es un string). Es un cadena
                   prefijada que tendrá un significado para la función:
                    "r"  -> Lectura              "w"  -> Escritura
                    "r+" -> Lectura/Escritura    "w+" -> Escritura/Lectura
                    "a"  -> Agregado             "a+" -> Agregado
                                                         Escritura/Lectura
                    
    E j e m p l o
    
        arch = open(NOMBRE_DEL_ARCHIVO_EN_DISPOSITIVO , MODO_DE_APERTURA)
        
               'open' devuelve un tipo de dato <class '_io.TextIOWrapper'>
               que representa un archivo de texto en memoria (Para Python).
               Este tipo de dato es un iterable, por tanto puede usarse
               directamente en un ciclo for.
               
               arch es nombre de la variable que representa al archivo de
               texto en el contexto de nuestro programa python
            
    
       - MÉTODOS QUE USAREMOS PARA ADMINISTRAR EL ARCHIVO EN PYTHON -
    
     B) LECTURA DEL ARCHIVO
           .readlines() ->  retorna una lista con TODO el contenido del archivo
                            Cada elemento de la lista 
           .readline()  ->  retorna un string con el contenido de UNA línea del
                            archivo
           
     C) ESCRITURA DEL ARCHIVO
           .write(CADENA)     ->  escribe la CADENA de caracteres pasada por
                                  parámetro en el archivo que la variable
                                  del método tenga asociado.
           
     D) CIERRE "DE LA CONEXIÓN" CON EL ARCHIVO

           .close()     ->  Cierra el archivo (ES OBLIGATORIO CERRAR SIEMPRE)

"""


"""
   F O R M A T O  D E  U N  A R C H I V O   D E   T E X T O 

   Define la forma en que la información se organiza y cómo está codificada
   en el archivo.
   
   ARCHIVO de texto ("simples"):
   
      PROPIEDADES
      + Contiene caracteres codificados (generalmente) en ASCII
      + Línea: es una secuencia de caracteres. Su fin es determinado por la 
               aparición del caracter salto de línea ('\n')
      
      - Por ejemplo: Un archivo que contenga un párrafo, o varios párrafos.
                     Por lo general una secuencia de caracteres que le
                     damos un significado.                     
    
   ARCHIVO CSV (Comma Separated Value):
      Es un formato de archivo de texto que se utiliza para representar datos
      en forma de tabla, en donde las columnas (los campos) se separan con coma. 
   
      + Es un archivo de texto
      + Contiene las mismas propiedades que el ARCHIVO de texto ("simples")
      
      P E R O !!!
      + La información se encuentra separada por algún caracter denominado
        delimintador. El separador típico es la 'coma' (","). Pero también
        suele usarse como separador otros caracteres como ser: 'punto y coma'(";"),
        tabulador("\t"), punto (".") ... u otros caracteres.
        El caracter delimitador no debe pertenecer al dominio de la información
        que se desea representar en el archivo.
        El ("\n") se debe encontrar al final indicando el fin de la línea.
      + Cada elemento que se encuentra separado por el "separador" se lo
        denomina campo
      + Cada línea compuesta por uno o más campos se la denomina registro.
        
        - Por ejemplo: 
            El siguiente es un archivo que se indica varias personas
            con su dni, nombre y apellido:
            
            2345,juan,Arrategui
            1234,Alicia,Castro
            4321,Claudia,Lopez
            9876,Gabriela,Mistral
            

"""

################################################################################
## CASO 1:
#'''
#  Función que lee un archivo con readlines.
#  Imprime la lista resultante de la lectura con readlines
#'''
def leerArch1():  
    print("----------leerArch1()---------------")    
    print("-Con readlines, imprime lista ------")
    print()
    arch = open("archLec.txt","r")      # Abrir archivo de lectura
    lstLineas = arch.readlines()        # leer todas las líneas del archivo y
                                        #   guardar en una lista lstLinea.
    print(lstLineas)                    # imprimir la lista con el contenido de
                                        #   las líneas del archivo. Se puede ver
                                        #   (en la salida) los caracteres 
                                        #   newline '\n' en el string que
                                        #   contiene cada elemento de la lista.
    arch.close()                        # cerrar el archivo
                                    
################################################################################  
## CASO 2
#    '''
#    Función que lee un archivo con readlines 
#    Imprime iterando con un ciclo la lista resultante de la lectura
#    con readlines
#    '''
def leerArch2():
    print("----------leerArch2()---------------")
    print("-Con readlines, recorre lista ------")
    print()
    arch = open("archLec.txt","r")      # Abrir archivo de lectura
    lstLinea = arch.readlines()         # leer todas las lineas del archivo y
                                        #   guardar en una lista
    for linea in lstLinea:              # recorrer lstLinea (list) y obtener cada
                                        #   línea (string)
       linea=linea[:-1]                 # Eliminar el caracter '\n'(newline), que
                                        #   es el último caracter del string línea
       print(linea)                     # imprimir la línea
    arch.close()                        # cerrar el archivo
                                    
################################################################################ 
## CASO 3
#   '''
#   Función lee un archivo con readline
#   imprime el string de la línea que retorna readline, 
#   Itera haciendo lectura de cada línea hasta el fin del archivo
#   '''
def leerArch3():
    print("----------leerArch3()---------------")
    print("-Con readline, imprime string - -----")
    print()
    arch = open("archLec.txt","r")      # Abrir archivo de lectura
    linea=arch.readline()               # leer una línea del archivo
                                        #   (antes de entrar al ciclo).
                                        #   Escribe el contenido en linea (str)
    while linea!="":                    # Mientras haya una línea en el archivo
                                        #  (linea=="", entonces es el fin del
                                        #  archivo)      
        linea = linea[:-1]              # Eliminar el caracter '\n'(newline),
                                        #   que es el último del string línea
        print(linea)                    # imprimir la línea la cual contiene la
                                        #   información de la línea leída del
                                        #   archivo.
        linea=arch.readline()           # leer una línea del archivo (dentro del
                                        #   ciclo)
    arch.close()                        # cerrar el archivo
    
################################################################################ 
## CASO 4
#  Función que lee un archivo e itera directamente sobre es el tipo de
#  dato _io.TextIOWrapper con un ciclo for
#
def leerArch4():
    print("----------leerArch4()---------------")
    print("-iterando io.TextIOWrapper (objeto archivo de texto)------")
    print()
    arch = open("archLec.txt","r")      # Abrir archivo de lectura "r"
    for linea in arch:                  # iterar arch. Se obtiene un 'str' en 
                                        #   cada iteración que es una línea del  
                                        #   archivo, que está determinada por
                                        #   el '\n' al final   
        print(linea[:-1])               # imprimir linea. El [:-1] esta para no
                                        #   imprimir el último caracter de la línea
                                        #   (que es donde está el '\n'
    arch.close()                        # cerrar el archivo
    
################################################################################ 
## CASO 5
## Función lee un archivo csv. Luego, por cada línea se separa en sus campos
## con un split (se divide el string por su <<separador>>) creando una sublista
## con los elementos de la línea del archivo.
## Se convierte el contenido del archivo en una lista de lista. Luego
## se imprime dicha lista
def leerArch5():
    print("----------leerArch5()---------------")
    print("-iterando el archivo ....+ split ------")
    print()
    arch = open("archLec.txt","r")      # Abrir archivo de lectura
    lstDatos=[]                         # Lista donde vamos a guardar los datos
                                        #   del archivo    
    for linea in arch:                  # recorrer arch  y obtener  cada línea (str)
        linea= linea[:-1]               # Eliminar el caracter '\n'(newline), que
                                        #   se encuentra al final del string
        lstLinea=linea.split(",")       # partir el string en listas determinadas
                                        #   por la <<coma>> dentro del string
                                        # << convertir los datos a su formato original
        lstLinea[0]=int(lstLinea[0])    # << de str a int
        lstLinea[1]=int(lstLinea[1])    # << de str a int 
        lstLinea[2]=float(lstLinea[2])  # << de str a float
        lstLinea[4]=int(lstLinea[4])    # << de str a int
        
        lstDatos.append(lstLinea)       # agregar la línea (en formato de lista)
                                        #   a la lista lstDatos 
              
    imprimirLista(lstDatos)             # imprimir la lista de lista lstDatos
    arch.close()                        # cerrar el archivo                                    

def imprimirLista(lst):
     for linea in lst:
        print("{:3d}{:4d} {:>8.3f}  {:20}{:4}".format(linea[0],linea[1],linea[2],linea[3],linea[4]))

################################################################################ 
## CASO 6
## Escritura de un archivo de texto
def escribirArch():
    print("----------escribirArch()---------------")
    print()
    import random
    arch = open("archEsc.txt","w")      # Abrir archivo de escritura    
    a=random.randint(0,99)              # cargo números aleatorios
    b=random.randint(0,99)
    c=random.randint(0,99)
    
    contenido = "23,5,9\n34,78,9\n"     # escribir un string con el contenido 
    contenido += str(a)+","+str(b)+","+str(c)+"\n" #"3.14,67,89\n"
    
    arch.write(contenido)               # escribir archivo
    arch.write("0,0,0\n")               # escribir archivo
    
    arch.close()                        # cerrar el archivo     
    print("----se escribió el archivo archEsc.txt--")

################################################################################ 
## CASO 7
## Agregado en un archivo de texto
def escribirAppendArch():
    print("----------escribirAppendArch()---------------")
    print()
    import random
    arch = open("archApp.txt","a")      # Abrir archivo "archApp.txt" de
                                        #   append (agregar o  anexar)    
    a=random.randint(0,99)              # cargo números aleatorios
    b=random.randint(0,99)
    c=random.randint(0,99)    
                                        # escribir un string con el contenido 
    contenido  = str(a)+","+str(b)+","+str(c)+"\n"
    
    arch.write(contenido)               # escribir archivo
    arch.close()                        # cerrar el archivo     
    print("----agregó en el archivo archApp.txt--")
  

  
def main():

#    leerArch1()
#    leerArch2()
#    leerArch3()
#    leerArch4()
#    leerArch5()
#    escribirArch()
#    escribirAppendArch()

main()

