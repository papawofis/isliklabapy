from itertools import *
def zd(z):
    k=0
    alf= 'ГЕПАРД'
    for x in product (alf, repeat = 5):
        s="".join(x)
        if s[0] != 'А' and s[-1] != 'Е' and s.count('Г') == 1:
            k+=1
    return(k)
z=0
print(zd(z))
