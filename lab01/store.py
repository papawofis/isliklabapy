goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

def calculate_lamp():
    """Расчет для лампы"""
    code = goods['Лампа']
    batch = store[code][0]
    quantity = batch['quantity']
    cost = quantity * batch['price']
    return quantity, cost

def calculate_table():
    """Расчет для стола"""
    code = goods['Стол']
    batch1 = store[code][0]
    batch2 = store[code][1]
    quantity = batch1['quantity'] + batch2['quantity']
    cost = (batch1['quantity'] * batch1['price'] + 
            batch2['quantity'] * batch2['price'])
    return quantity, cost

def calculate_sofa():
    """Расчет для дивана"""
    code = goods['Диван']
    batch1 = store[code][0]
    batch2 = store[code][1]
    quantity = batch1['quantity'] + batch2['quantity']
    cost = (batch1['quantity'] * batch1['price'] + 
            batch2['quantity'] * batch2['price'])
    return quantity, cost

def calculate_chair():
    """Расчет для стула"""
    code = goods['Стул']
    batch1 = store[code][0]
    batch2 = store[code][1]
    batch3 = store[code][2]
    quantity = batch1['quantity'] + batch2['quantity'] + batch3['quantity']
    cost = (batch1['quantity'] * batch1['price'] + 
            batch2['quantity'] * batch2['price'] + 
            batch3['quantity'] * batch3['price'])
    return quantity, cost

def print_result(product_name, quantity, cost):
    """Выводит результат"""
    print(f'{product_name} - {quantity} шт, стоимость {cost} руб')
def res():  
    lamps_qty, lamps_cost = calculate_lamp()
    print_result('Лампа', lamps_qty, lamps_cost)
    table_qty, table_cost = calculate_table()
    print_result('Стол', table_qty, table_cost)
    sofa_qty, sofa_cost = calculate_sofa()
    print_result('Диван', sofa_qty, sofa_cost)
    chair_qty, chair_cost = calculate_chair()
    print_result('Стул', chair_qty, chair_cost)