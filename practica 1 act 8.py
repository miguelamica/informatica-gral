seg=int(input("ingrese tiempo en segundos: "))
dias=seg//60//60//24
horas1=(seg-86000)
horas2=horas1//60//60
minutos=horas1//60%60
segundos=horas1%60
print(" dia(s):",dias," horas:",horas2," minutos:",minutos," segundos:",segundos)
