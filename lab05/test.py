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