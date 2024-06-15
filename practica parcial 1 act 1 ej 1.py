def fun1T1(num1,num2):
    cifNum1=len(str(num1))
    cifNum2=len(str(num2))
    if cifNum1==cifNum2 and cifNum1%2==0 or cifNum2%2==0:
        d=num1%10
        u=num2//10**(cifNum2-1)
        rta="{}{}".format(d,u)
    elif cifNum1==cifNum2 and cifNum1%2==1 or cifNum2%2==1:
        d=(num1//10**(cifNum1//2))%10
        u=(num2//10**(cifNum2//2))%10
        rta="{}{}".format(d,u)
    if cifNum1!=cifNum2:
        rta=-1
    return rta

def main():
    num1=1
    num2=436
    print(fun1T1(num1,num2))

    
main()
        