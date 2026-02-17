from itertools import *
def p(z):
    res=""
    while z >0:
        res=str(z%5)+res
        z//=5
    return(res)
def zd(z):
    s=5**36+5**24-25
    x=p(s)
    res= x.count("4")
    return res
z=0
print(zd(z))