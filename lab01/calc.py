#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_distances(sites=sites):
    result = {}
    names = list(sites.keys())
    
    for i, name1 in enumerate(names):
        result[name1] = {}
        for j, name2 in enumerate(names):
            if i != j:
                result[name1][name2] = dist(sites[name1], sites[name2])
    
    return result
