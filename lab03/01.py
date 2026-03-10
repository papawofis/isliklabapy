def per(add1,add2):
    s=[]
    for i in add1:
        if i not in s and i in add2:
            s.append(i)
    return s


def rper(add1, add2):
    if not add1 or not add2:
        return []
    if add1[0] in add2 and add1[0] not in add1[1:]:
        return [add1[0]] + rper(add1[1:], add2)
    else:
        return rper(add1[1:], add2)
    


add1=[1,2,3,4,2]

add2=[2,3,4,6,8]

print(list(per(add1,add2)))
print(rper(add1,add2))