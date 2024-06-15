'''
rtas teorico 23/2/2021
1_  e  si
2_  g  si
3_  f  si
4_  e  si
5_  b  si





'''
def fun(x):
    i=0
    tam=len(x)
    while i< (tam/2):
        a = x[i]
        x[i] = x[tam-1-i]
        x[tam-1-i] = a
        i+=1
def main():
    x=[1,2,3,4,5]
    fun(x)
    print(x)
main()