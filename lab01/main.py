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
