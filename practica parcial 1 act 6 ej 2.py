def caracter(valor):
    res=""
    if valor<10:
        res=str(valor)
    if valor==10:
        res="A"
    if valor==11:
        res="B"
    if valor==12:
        res="C"
    if valor==13:
        res="D"
    if valor==14:
        res="E"
    if valor==15:
        res="F"
    return res
    
def decimalAHexadecimal(numD):
    h1=numD%16
    h2=numD//16
    return caracter(h2)+caracter(h1)

def main():
    num=63
    print("En hexadecimal: {}".format(decimalAHexadecimal(num)))  
    
main()