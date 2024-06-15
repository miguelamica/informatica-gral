def costoPorConsumo(con):              #<>
    if con<=100 and con>0 and int(con)==con:
        costo= con*35
    elif con>100<=500 and int(con)==con:
        costo=100*35+(con-100)*50
    elif con>500<=1000 and int(con)==con:
        costo=100*35+400*50+(con-500)*85
    elif con>1000 and int(con)==con:
        costo=100*35+400*50+500*85+(con-1000)*170
    elif con<0 or int(con)!=con:
        costo=-1
    return costo

def main():
    print(costoPorConsumo(38))
    print(costoPorConsumo(102))
    print(costoPorConsumo(250))
    print(costoPorConsumo(785))
    print(costoPorConsumo(3500))
    
    print(costoPorConsumo(-45))
    print(costoPorConsumo(3.14))
main()