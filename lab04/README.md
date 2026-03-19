АДАНИЕ 01.py
--------
#### Задание: замыкание реализующее последовательность Фибоначчи.
```python
def per(add1,add2):
    pers= set(add1) & set(add2)
    return pers


def rper(add1, add2, res = None):
    if add1 is None:
        res=[]
    if len(add1) == 0: 
        return res
    id = add1[0]
    if (id in add2) and id not in res:
        res.append(id)
    return rper(add1[1:],add2,res)


add1=[1,2,3,4]

add2=[2,3,4,6,8]

print(list(per(add1,add2)))
print(rper(add1,add2,res=[]))
```
###### Результат
<img width="122" height="55" alt="image" src="https://github.com/user-attachments/assets/f2b2c1fb-963e-4feb-b655-4598e617a59c" />
