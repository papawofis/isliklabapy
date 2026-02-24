 ЗАДАНИЕ 01 question.py
--------
#### Задание: Ученица составляет 5-буквенные слова из букв ГЕПАРД. При этом в каждом слове ровно одна буква Г, слово не может начинаться на букву А и заканчиваться буквой Е. Какое количество слов может составить ученица?
```python
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
```
###### Результат
<img width="479" height="38" alt="image" src="https://github.com/user-attachments/assets/b9ad2d15-0897-4a8a-acdd-07a90a30fbef" />


ЗАДАНИЕ 02 question.py
--------
#### Задание: Значение выражения 536+524−25 5^{36} + 5^{24} − 25 536+524−25 записали в системе счисления с основанием 5. Сколько цифр 4 содержится в этой записи?
```python
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
```
###### Результат
<img width="439" height="31" alt="image" src="https://github.com/user-attachments/assets/25810f91-1846-412b-ad95-0a9f4db04294" />


ЗАДАНИЕ 03 question.py
--------
#### Задание: Найдите 5 чисел больших 500000, таких, что среди их делителей есть число, оканчивающееся на 8, при этом этот делитель не равен 8 и самому числу. В качестве ответа приведите 5 наименьших чисел, соответствующих условию.

### Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке сначала выводится само число, затем минимальный делитель, оканчивающийся на 8, не равный 8 и самому числу.
```python
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
        if i % 10 == 0 and i != 8 and i != n:
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
```
###### Результат
<img width="291" height="112" alt="image" src="https://github.com/user-attachments/assets/55afa104-e077-43e3-810d-1e0fe479caa6" />

###Ссылки на используемые материалы:
    1. [Itertools в Python - Хабр](https://habr.com/ru/companies/otus/articles/529356/)
    
    2. [itertools — Functions creating iterators for efficient looping](https://docs.python.org/3/library/itertools.html)
    
    3. [Итерируем правильно: 20 приемов использования в Python модуля itertools](https://proglib.io/p/iteriruemsya-pravilno-20-priemov-ispolzovaniya-v-python-modulya-itertools-2020-01-03)

