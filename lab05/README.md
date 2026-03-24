ЗАДАНИЕЛабы.py
--------
#### Задание: Генератор, создающий пароли по определённым правилам. Инвертируйте регистр букв в выводе генератора.
```python
import random
import string

def gen_pass(len=8, digits=True, symbols=False):
    # Генератор паролей
    chars = string.ascii_letters  # Буквы из аскиай
    
    if digits:
        chars += string.digits     # Добавляем цифры 0-9
    
    if symbols:
        chars += string.punctuation # Добавляем спецсимволы
    
    while True:
        password = ''.join(random.choice(chars) for _ in range(len))
        yield password     # Возвращаем пароль и ждём следующий вызов


def swap_case(ch):
    # Меняет регистр букв (A->a, b->B)
    if ch.isalpha():
        return ch.swapcase()
    return ch  # Не буквы возращаем просто


def min_len(pwd, lim=6):
    # Проверяет минимальную длину пароля
    return len(pwd) >= lim


def main():
    print("Генератор паролей\n")
    
    # Создаём генератор паролей (длина 8, есть цифры, нет символов)
    passwords = gen_pass(len=8, digits=True, symbols=False)
    # Оставляем только пароли длиной ≥ 6
    filtered = filter(lambda p: min_len(p, 6), passwords)
    # Инвертируем регистр каждого символа в пароле
    inverted = map(lambda p: ''.join(map(swap_case, p)), filtered)
    
    # Выводим первые 10 паролей с инвертированным регистром
    for i, pwd in enumerate(inverted, 1):
        if i > 10:
            break
        print(f"{i:2d}. {pwd}")

    # Ещё один генератор (длина 4, нет цифр, есть символы)
    pr = gen_pass(len=4, digits=False, symbols=True)
    
    print(next(pr))  # Выводим первый пароль
    print(next(pr))  # Выводим второй пароль


if __name__ == "__main__":
    main()
```
##### Результат:
<img width="227" height="234" alt="image" src="https://github.com/user-attachments/assets/d18bc0fa-4482-4ef6-8cea-45b1107c1f0d" />


ЗАДАНИЕмедиум.py
--------
#### Задание: Напишите для генератора тесты с помощью pytest
```python
import pytest
from generator import gen_pass, swap_case, min_len

def test_swap_case():
    """Тест инверсии регистра"""
    assert swap_case('a') == 'A'
    assert swap_case('Z') == 'z'
    assert swap_case('1') == '1'
    assert ''.join(map(swap_case, "Hello123")) == "hELLO123"

def test_min_len():
    """Тест проверки длины пароля"""
    assert min_len("123456", 6) == True
    assert min_len("abc", 6) == False
    assert min_len("password123", 3) == True

def test_gen_pass():
    """Тест генератора паролей"""
    gen = gen_pass(len=8, digits=True, symbols=False)
    password = next(gen)
    
    # Проверяем длину
    assert len(password) == 8
    # Проверяем, что есть буквы
    assert any(c.isalpha() for c in password)
    # Проверяем, что есть цифры
    assert any(c.isdigit() for c in password)
```
##### Результат:
<img width="744" height="180" alt="image" src="https://github.com/user-attachments/assets/0b87fcfd-07c2-4d24-b949-36858c9b0d99" />

##### Используемые материалы:

[Модуль random в Python](https://www.google.com/url?esrc=s&q=&rct=j&sa=U&url=https://www.youtube.com/watch%3Fv%3DF5SYEE6eT28&ved=2ahUKEwiyxobx9LeTAxXHT1UIHXeBDHsQtwJ6BAgBEAE&usg=AOvVaw0yhKoWPsagm3PsOuyzg938)

[Модуль string в Python](https://www.google.com/url?esrc=s&q=&rct=j&sa=U&url=https://www.youtube.com/watch%3Fv%3DKMsuQ61iUTo&ved=2ahUKEwjA27aj9beTAxURUFUIHXieAZAQtwJ6BAgGEAE&usg=AOvVaw1PGgX8g9CIAvlbXPJhjPpu)
