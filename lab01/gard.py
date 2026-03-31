# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

def af(garden_flowers, meadow_flowers):
    # Создаем множества
    garden_set = set(garden_flowers)
    meadow_set = set(meadow_flowers)
    
    # Вычисляем результаты
    all_flowers = garden_set | meadow_set
    common = garden_set & meadow_set
    garden_only = garden_set - meadow_set
    meadow_only = meadow_set - garden_set
    
    # Выводим
    print("Все виды цветов:", all_flowers)
    print("Растут и там, и там:", common)
    print("Только в саду:", garden_only)
    print("Только на лугу:", meadow_only)
    
    # Возвращаем результаты на случай, если понадобятся дальше
    return all_flowers, common, garden_only, meadow_only
def res(garden=garden, meadow=meadow):
    return af(garden, meadow)