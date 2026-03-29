#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_distances(cities):
    result = {}
    names = list(cities.keys())
    
    for i, name1 in enumerate(names):
        result[name1] = {}
        for j, name2 in enumerate(names):
            if i != j:
                result[name1][name2] = dist(cities[name1], cities[name2])
    
    return result
