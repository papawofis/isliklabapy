# ЗАДАНИЕ 00_distance.py
--------
#### Задание: Рассчитать расстояние между городами, составить словарь и вывести на экран

С помощью формулы ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 рассчитаем дистанцию от одного города до другого

###### Добавленная часть кода
>``` python
>for site1, coords1 in sites.items():
>    city_distances = {}
>    for site2, coords2 in sites.items():
>        if site1 != site2:
>            x1, y1 = coords1
>            x2, y2 = coords2
>            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
>            city_distances[site2] = round(distance,2)
>    
>    distances[site1] = city_distances
>
>print(distances)
>```

###### Результат
>```
>{'Moscow': {'London': 145.6, 'Paris': 130.38}, 'London': {'Moscow': 145.6, 'Paris': 42.43}, 'Paris': {'Moscow': 130.38, 'London': 42.43}}
>```



# ЗАДАНИЕ 01_circle.py
----
#### Задание:
1. Вывести на консоль значение прощади данного круга с точностю до 4-х знаков после запятой;
2. Вывести на консоль True, если точка point лежит внутри круга, False - не лежит;
3. Аналогично для другой точки (point_2)

Воспользуемся формулой площади круга: S=π*R^2
