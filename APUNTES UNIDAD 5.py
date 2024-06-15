#cad=""
#cad="aron"

def esLetra(car):
    res = False
    if ((car>="a" and car <="z") or (car>="A" and car <="Z")):
        res=True
    return res

frase = "# $Baron!, aaa urgente ya ha aaaaaa nacido! Es un varon$$$"
def verPal(frase):
    res=""
    pri=""
    ult=""
    i=0                                               
    largoFrase = len(frase)
    while i<largoFrase:        
        while i<largoFrase and not esLetra(frase[i]):
            i+=1        
        pal=""
        while i<largoFrase and esLetra(frase[i]):
            pal=pal+frase[i]
            i+=1
        if pal!="":
            #print(pal,end=",")
            if pri=="":
                pri=pal
            ult=pal
    res="**\n"+pri+" , "+ult+"\n**"
    return res
    
print(verPal(frase))


# def contarCad(cad, frase):
#     cont = 0
#     i=0
#     while i<len(frase):
#         if cad == frase[i:i+len(cad)]:
#             cont+=1
#             i+=len(cad)
#         else:
#             i+=1
#         
#     return cont
# 
# print(contarCad(cad, frase))