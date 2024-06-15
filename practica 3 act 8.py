def promedioParRec(not1,not2,not3,rec):
    pro=(not1+not2+not3+rec)/4
    if rec>4:
       rta="Promedio: {:3.2f}. \nEl alumno deberá rendir el final".format(pro)
    else:
        rta="Promedio: {:3.2f}. \nEl alumno fue aplazado".format(pro)
    return rta

def promedioParciales(not1,not2,not3):
    if (not1+not2+not3)/3>=7:
        res="El alumno promocionó la materia"
    elif (not1+not2+not3)/3<7:
        res="El alumno deberá rendir final"
    return res 

def main():
    not1=int(input("Ingrese la nota del primer parcial: "))
    not2=int(input("Ingrese la nota del segundo parcial: "))    #><
    not3=int(input("Ingrese la nota del tercer parcial: "))
    if not1>=4 and not2>=4 and not3>=4:
        print(promedioParciales(not1,not2,not3))
    else:
        rec=int(input("Ingrese la nota del recuperatorio: "))
        print(promedioParRec(not1,not2,not3,rec))
        
main()