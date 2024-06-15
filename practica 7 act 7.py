def agregarRegistro():                      #<>
    arc=open("act7.csv","a")
    nuevo=input("Ingrese nuevos datos a registrar (separados c/u por un (punto y coma): ")
    arc.write(nuevo)
    arc.close()
    
def eliminarRegistro():
    arc=open("act7.csv","r")
    lst=arc.readlines()
    lst1=[]
    for linea in lst:
        linea=linea[:-1]
        linea1=linea.split(";")
        lst1.append(linea1)
    arc.close()
    eli=input("Ingrese numero de registro a eliminar: ")
    i=0
    num=i
    while eli!=lst1[i][0]:
        if eli!=lst1[i][0]:
            i+=1
            num=i
        else: num=i
    lst1.remove(lst1[num])
    arc1=open("act7.csv","w")
    for x in range(len(lst1)):
        arc1.write(str(lst1[x][0]))
        arc1.write(";")
        arc1.write(lst1[x][1])
        arc1.write(";")
        arc1.write(str(lst1[x][2]))
        arc1.write("\n")
    arc1.close()
    return lst1
    
def buscarRegistro():
    arc=open("act7.csv","r")
    lst=arc.readlines()
    lst1=[]
    for linea in lst:
        linea=linea[:-1]
        linea1=linea.split(";")
        lst1.append(linea1)
    arc.close()
    bus=input("Ingrese dni o apellido a buscar: ")
    print("\n")
    i=0
    lst2=[]
    while i<len(lst1):
        if bus in lst1[i][0]:
            print(lst1[i])
            lst2.append(lst1[i])
            i+=1
        elif bus in lst1[i][1]:
            print(lst1[i])
            lst2.append(lst1[i])
            i+=1
        else:
            i+=1
    if len(lst2)==0:
        print("El dni o apellido no se encuentra en el registro. Por favor, intentar nuevamente.")
    print("\n")
            
def ordenarArchivo():
    arc=open("act7.csv","r")
    lst=arc.readlines()
    lst1=[]
    for linea in lst:
        linea=linea[:-1]
        linea1=linea.split(";")
        linea1[0]=int(linea1[0])
        linea1[2]=int(linea1[2])
        lst1.append(linea1)
    arc.close()
    num=int(input("Ingrese el numero de campo para ser ordenado(1, dni; 2, nombre; 3, edad): "))
    arc1=open("act7.csv","w")
    if num==1:
        for x in range(len(lst1)-1):
            for i in range(len(lst1)-1):
                if lst1[i][0]>lst1[i+1][0]:
                    aux=lst1[i]
                    lst1[i]=lst1[i+1]
                    lst1[i+1]=aux  
            
        for linea2 in lst1:
            arc1.write(str(linea2[0]))
            arc1.write(";")
            arc1.write(linea2[1])
            arc1.write(";")
            arc1.write(str(linea2[2]))
            arc1.write("\n")
            
    elif num==2:
        for x in range(len(lst1)-1):
            for i in range(len(lst1)-1):
                if lst1[i][1][0]>lst1[i+1][1][0]:
                    aux=lst1[i]
                    lst1[i]=lst1[i+1]
                    lst1[i+1]=aux  
            
        for linea2 in lst1:
            arc1.write(str(linea2[0]))
            arc1.write(";")
            arc1.write(linea2[1])
            arc1.write(";")
            arc1.write(str(linea2[2]))
            arc1.write("\n")
            
    elif num==3:
        for x in range(len(lst1)-1):
            for i in range(len(lst1)-1):
                if lst1[i][2]>lst1[i+1][2]:
                    aux=lst1[i]
                    lst1[i]=lst1[i+1]
                    lst1[i+1]=aux  
            
        for linea2 in lst1:
            arc1.write(str(linea2[0]))
            arc1.write(";")
            arc1.write(linea2[1])
            arc1.write(";")
            arc1.write(str(linea2[2]))
            arc1.write("\n")
            
    print(lst1)
    arc1.close()
    
def mostrarArchivo():
    arc=open("act7.csv","r")
    lst=arc.readlines()
    lst1=[]
    for linea in lst:
        linea=linea[:-1]
        linea1=linea.split(";")
        linea1[0]=int(linea1[0])
        linea1[2]=int(linea1[2])
        lst1.append(linea1)
    
    arc.close()
    print(lst1)
    
    
def menu():
    print("1. AGREGAR REGISTRO\n 2. ELIMINAR REGISTRO\n 3. BUSCAR REGISTRO\n 4. ORDENAR ARCHIVO POR\n 5. MOSTRAR ARCHIVO\n 6. SALIR\n")
    rta=int(input("Ingrese el valor de la opción: "))
    while rta<6:
        if rta==1:
            agregarRegistro()
            print("1. AGREGAR REGISTRO\n 2. ELIMINAR REGISTRO\n 3. BUSCAR REGISTRO\n 4. ORDENAR ARCHIVO POR\n 5. MOSTRAR ARCHIVO\n 6. SALIR\n")
            rta=int(input("Ingrese el valor de la opción:"))
            
        elif rta==2:
            eliminarRegistro()
            print("1. AGREGAR REGISTRO\n 2. ELIMINAR REGISTRO\n 3. BUSCAR REGISTRO\n 4. ORDENAR ARCHIVO POR\n 5. MOSTRAR ARCHIVO\n 6. SALIR\n")
            rta=int(input("Ingrese el valor de la opción:"))
            
        elif rta==3:
            buscarRegistro()
            print("1. AGREGAR REGISTRO\n 2. ELIMINAR REGISTRO\n 3. BUSCAR REGISTRO\n 4. ORDENAR ARCHIVO POR\n 5. MOSTRAR ARCHIVO\n 6. SALIR\n")
            rta=int(input("Ingrese el valor de la opción:"))
            
        elif rta==4:
            ordenarArchivo()
            print("1. AGREGAR REGISTRO\n 2. ELIMINAR REGISTRO\n 3. BUSCAR REGISTRO\n 4. ORDENAR ARCHIVO POR\n 5. MOSTRAR ARCHIVO\n 6. SALIR\n")
            rta=int(input("Ingrese el valor de la opción:"))
            
        elif rta==5:
            mostrarArchivo()
            print("1. AGREGAR REGISTRO\n 2. ELIMINAR REGISTRO\n 3. BUSCAR REGISTRO\n 4. ORDENAR ARCHIVO POR\n 5. MOSTRAR ARCHIVO\n 6. SALIR\n")
            rta=int(input("Ingrese el valor de la opción:"))
        
#         elif rta==6:
#             print("Fin de las operaciones. Muchas gracias por operar con nosotros. Que tenga un buen dia :) <3!")
            
def main():
    print(menu())
    
menu()