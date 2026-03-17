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
   