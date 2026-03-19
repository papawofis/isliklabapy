ЗАДАНИЕ 01.py
--------
#### Задание: замыкание реализующее последовательность Фибоначчи.
```python
def dec(func):
    cache = {}  # словарь
    
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))  # ключик для кэширки
        
        if key in cache:
            print(f"берем из кэша{args}")
            return cache[key]
        
        print(f"считаем для аргументов{args}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper

@dec
def fib():
    a,b=0,1
    def next():
        nonlocal a,b
        res = a
        a,b=b, a+b
        return res
    return next


fi = fib()
print(fi()) 
print(fi())  
print(fi())  
print(fi())  
print(fi())  
print(fi())  
print(fi())  
```
###### Результат
<img width="442" height="176" alt="image" src="https://github.com/user-attachments/assets/cace691d-75ef-47c5-b3b4-0f69b2c6ffd9" />

ЗАДАНИЕ 02.py
--------
#### Задание: создать декоратор для кэширования результатов выполнения функций.
```python
def opc(u=True):
    def dec(func):
        cache = {}  # словарь

        def wrapper(*args, **kwargs):
            if not u:
                return func(*args,**kwargs)
            
            key = (args, tuple(kwargs.items()))  # ключик для кэширки
            
            if key in cache:
                print(f"берем из кэша{args}")
                return cache[key]
            
            print(f"считаем для аргументов{args}")
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        return wrapper
    return dec

@opc(True)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

@opc(False)
def fib2(n):
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

@opc
def fib3(n):
    if n < 2:
        return n
    return fib3(n-1) + fib3(n-2)


print(fib(3))
print(fib2(3))  
print(fib3(3))  
```
###### Результат
<img width="679" height="172" alt="image" src="https://github.com/user-attachments/assets/6c82a0f8-1850-4dad-93c1-a9a9174cdd19" />
