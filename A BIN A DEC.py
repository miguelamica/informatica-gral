#de binario a decimal
def dec_a_bin(num):
    d1=num//2
    dec1=num%2
    d2=d1//2
    dec2=d1%2
    d3=d2//2
    dec3=d2%2
    d4=d3//2
    dec4=d3%2
    d5=d4//2
    dec5=d4%2
    d6=d5//2
    dec6=d5%2
    d7=d6//2
    dec7=d6%2
    print("{}{}{}{}{}{}{}".format(dec7,dec6,dec5,dec4,dec3,dec2,dec1))
    
dec_a_bin(77)

def decabin(num):
    d1=num%2
    d2=num//2%2
    d3=num//4%2
    d4=num//8%2
    d5=num//16%2
    d6=num//32%2
    d7=num//64%2
    print("{}{}{}{}{}{}{}".format(d7,d6,d5,d4,d3,d2,d1))

decabin(77)

#de decimal a octal
def dec_a_oct(num):
    d1=num//8
    dec1=num%8
    d2=d1//8
    dec2=d1%8
    d3=d2//8
    dec3=d2%8
    print("{}{}{}".format(dec3,dec2,dec1))

dec_a_oct(122)

def deaoct(num):
    d1=num%8
    d2=num//8%8
    d3=num//64%8
    print("{}{}{}".format(d3,d2,d1))
    
deaoct(122)
 
    