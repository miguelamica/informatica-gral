def incrementarDia(dia,mes,año):
    if dia==28 and mes==2 and año>=0 and año%4!=0 and año%400!=0:
        fecha="{:d}/{}/{}".format(1,mes+1,año)
    elif dia<28 and mes==2 and año>=0:
        fecha="{}/{}/{}".format(dia+1,mes,año)
    elif dia==29 and mes==2 and año>=0 and año%4==0 and año%400==0 and año//100!=0:
        fecha="{}/{}/{}".format(1,mes+1,año)
    elif dia<29 and mes==2 and año>=0 and año%4==0 and año%400==0 and año//100!=0:
        fecha="{}/{}/{}".format(dia+1,mes,año)
    elif dia<30:
        if mes==4 or mes==6 or mes==9 or mes==11 and año>=0:
            fecha="{}/{}/{}".format(dia+1,mes,año)
    elif dia==30 and mes==4 or mes==6 or mes==9 or mes==11 and año>=0:
        fecha="{:d}/{}/{}".format(1,mes+1,año)
    elif dia<31:
        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and año>=0:
            fecha="{}/{}/{}".format(dia+1,mes,año)
    elif dia==31 and mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 and año>=0:
        fecha="{:d}/{}/{}".format(1,mes+1,año)
    elif dia==31 and mes==12 and año>=0:
        fecha="{:d}/{:d}/{}".format(1,1,año+1) 
    
    
    return fecha

def main():
    print(incrementarDia(23,4,2022))
    print(incrementarDia(31,5,2022))
    print(incrementarDia(30,9,2022))
    print(incrementarDia(31,12,2022))
    print(incrementarDia(29,2,2000))
    print(incrementarDia(28,2,2000))
    
main()
    
    