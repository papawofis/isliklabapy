#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PI = 3.1415926

def area(r):
    """Площадь круга"""
    return PI * r * r

def in_circle(point, r):
    """Проверка, лежит ли точка внутри круга"""
    x, y = point
    dist = (x**2 + y**2) ** 0.5
    return dist < r
