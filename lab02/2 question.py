def p(z):
    res=""
    while z >0:
        res=res+str(z%5)
        z//=5
    return(res)

def zd():
    s=5**36+5**24-25
    x=p(s)
    res= x.count("4")
    return res

print(zd())