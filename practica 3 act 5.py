def fecha(dia,mes,año):
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia<=31 and año>=0:
        rta="la fecha es correcta"
    else:
        rta="la fecha es incorrecta"
    if mes==4 or mes==6 or mes==9 or mes==11 and dia<=30 and año>=0:
        rta="la fecha es correcta"
    else:
        rta="la fecha es incorrecta"
    if mes==2 and dia<=28 and año>=0:
        rta="la fecha es correcta"
    else:
        rta="la fecha es incorrecta"
    if mes==2 and dia<=29 and año%4==0 and año%400==0:
        rta="la fecha es correcta"
    else:
        rta="la fecha es incorrecta"
    return rta

def main():
    dia=int(input("Ingrese un dia: "))
    mes= int(input("Ingrese un mes: "))
    año= int(input("Ingrese un año: "))
    print(fecha(dia,mes,año))
    
main()