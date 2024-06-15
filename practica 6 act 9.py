def cargarAlu():                    #<>
    alu=[]
    dni=int(input("ingrese dni: "))
    alu.append(dni)
    nom=input("ingrese nombre completo: ")
    alu.append(nom)
    ed=int(input("ingrese edad:"))
    alu.append(ed)
    
    return alu
        
def cargarLstAlu():
    num=int(input("ingrese num de alumnos: "))
    lst=[]
    i=0
    while i<num:
        lst.append(cargarAlu())
        i+=1
    return lst

    
def ordenarLst(lst):
    for x in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i][0]>lst[i+1][0]:
                aux=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=aux
    return lst[::-1]
                
def main():
    lst=cargarLstAlu()
    print(lst)
    ordenarLst(lst)
    print(lst)
    
main()


"""[2698705, 'James Howlett', 18], [38698705, 'Jakie chan', 22],
[35698705, 'Jean Grey', 22]"""