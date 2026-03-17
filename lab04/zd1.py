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