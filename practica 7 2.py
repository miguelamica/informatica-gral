def agregarmedia(entrada):
    archivo=open(entrada)
    lista=archivo.readlines()
    lst1=[]
    for linea in lista:
        linea=linea[:-1]
        linea1=linea.split(",")
        linea1[0]=int(linea1[0])
        linea1[1]=int(linea1[1])
        linea1[2]=int(linea1[2])
        linea1[3]=int(linea1[3])
        lst1.append(linea1)
    salida=open('act2.txt',"w")
    for line in lista:
        nums=line.split(',')
        print (nums)
        suma=0
        for n in nums:
            suma+=int(n)
        prom=suma/len(nums)
        salida.write(line)
        salida.write(str(prom)+'\n')
    salida.close()
    archivo.close()
def main():
    agregarmedia("act2.txt")
main()