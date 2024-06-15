def operaciones(a,b):
    suma=a+b
    resta=a-b
    mul=a*b
    if b==0:
        div=None
    else:
        div=a/b
    tup=(suma,resta,mul,div)
    return tup

def main():
    print(operaciones (54,0))
    
    
main()