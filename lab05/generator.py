import random
import string

def gen_pass(len=8, digits=True, symbols=False):
    # Генератор паролей
    chars = string.ascii_letters
    
    if digits:
        chars += string.digits
    
    if symbols:
        chars += string.punctuation
    
    while True:
        password = ''.join(random.choice(chars) for _ in range(len))
        yield password


def swap_case(ch):
    # Меняет регистр букв
    if ch.isalpha():
        return ch.swapcase()
    return ch


def min_len(pwd, lim=6):
    # Проверяет минимальную длину пароля
    return len(pwd) >= lim


def main():
    print("Генератор паролей\n")
    
    passwords = gen_pass(len=8, digits=True, symbols=False)
    filtered = filter(lambda p: min_len(p, 6), passwords)
    inverted = map(lambda p: ''.join(map(swap_case, p)), filtered)
    
    for i, pwd in enumerate(inverted, 1):
        if i > 10:
            break
        print(f"{i:2d}. {pwd}")

    pr = gen_pass(len=4, digits = False, symbols = True)

    print(next(pr))
    print(next(pr))


if __name__ == "__main__":
    main()