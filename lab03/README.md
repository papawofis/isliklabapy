 ЗАДАНИЕ 01.py
--------
#### Задание: написать функцию для нахождения пересечения двух списков.
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


ЗАДАНИЕ 02.py
--------
#### Задание: написать функцию для расчета \[x_n = \sqrt{3 + \sqrt{3 + \sqrt{3 + \sqrt{3 + \ldots + \sqrt{3}}}}} \quad \text{(n корней)}\]
```python
from sys import *


def rx(n):
    if n == 1:
        return 3**0.5
    return (3 + rx(n-1))**0.5
    
def x(n):
    sum=0
    tek=0
    for i in range(n):
        tek=(3+tek)**0.5
        sum+=tek
    return tek

n=3
print(rx(n))
print(x(n))
```
###### Результат
<img width="222" height="50" alt="image" src="https://github.com/user-attachments/assets/e1c5ccef-a273-458c-86e6-6a7cf282a559" />

##### Используемые материалы:
[Рекурсия с нуля Python](https://www.google.com/url?esrc=s&q=&rct=j&sa=U&url=https://www.youtube.com/watch%3Fv%3Dw3FlW2THtUk&ved=2ahUKEwi8g4XQ3pSTAxX6gv0HHTFMAscQuAJ6BAgJEAI&usg=AOvVaw2XY2AK2rms1m6S0adgg_-i)


