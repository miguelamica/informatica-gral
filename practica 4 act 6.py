def aBinario(numD):
    numB=""
    if 0<numD<1000:
        while 0<numD:
            res=numD%2
            numB=str(res)+numB
            numD//=2
    print(numB)

def main():
    aBinario(180)

main()
