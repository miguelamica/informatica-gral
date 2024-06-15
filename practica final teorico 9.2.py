'''
rtas teorico 9.2.2021
1_  e  si
2_  f  si
3_  g  no, rta es E
4_  d? no, rta es B
5_  g? no, rta es D





'''
def fun(a,b,c):
    p = a and(b or c)
    q = (a and b) or (a and c)
    if p == q:
        res = 10
    else:
        res = -10
    return res
def main():
    res = fun(True,True,True) + fun(True,True,False)
    print(res)
main()