#00.dist
from calc import get_distances

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = get_distances(sites)
print(distances)

#01.cir
from circle import area, in_circle

radius = 42

# Площадь круга с точностью 4 знака
s = area(radius)
print(f"{s:.4f}")

# Первая точка
point = (23, 34)
print(in_circle(point, radius))

# Вторая точка
point2 = (30, 30)
print(in_circle(point2, radius))

#02.oper

#3.mov
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from movies import first, last, second, second_last, get_movies

mf = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Способ 1 - по отдельности
print(first(mf))
print(last(mf))
print(second(mf))
print(second_last(mf))

print("---")

