base=float(input("Ingrese base: "))
altura=float(input("Ingrese altura: "))
round(base, 2)
round(altura, 2) 
print("Calculos que se pueden hacer con la base {} y la altura {}:".format(base,altura))
area=(base*altura)/2
print("area: {:6.2f}".format(area))
hipotenusa=(base**2+altura**2)**0.50
perimetro=base+altura+hipotenusa
print("perimetro: {:6.2f}".format(perimetro))