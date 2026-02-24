def dl(n):
    d=[]
    for i in range(2,int(n**0.5)+1):
        if n % i == 0 :
            d.append(i)
            if i != n //i:
                d.append(n//i)
    return(d)
ds=[]
def ps(n):
    for i in dl(n):
        if i % 10 == 8 and i != 8 and i != n:
            return i
    return None
    

res=[]
nc=500_001
while len(res) < 5:
    d=ps(nc)
    if d:
        res.append((nc,d))
        print(f"{nc} {d}")
    nc+=1