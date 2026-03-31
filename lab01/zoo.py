#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo_list = ['lion', 'kangaroo', 'elephant', 'monkey', ]
birds_list = ['rooster', 'ostrich', 'lark', ]
# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
def bear(zoo_list=zoo_list):
    zoo_list.insert(1, 'bear')
    print( zoo_list)
    return zoo_list

def birds(zoo_list=zoo_list, birds_list=birds_list):
    for bird in birds_list:
        zoo_list.append(bird)
    print(zoo_list)
    return zoo_list

def elep(zoo_list=zoo_list):
    zoo_list.remove('elephant')
    print(zoo_list)
    return zoo_list

def find(zoo_list=zoo_list):
   for i in range(len(zoo_list)):
    if (zoo_list[i]=='lion' ) or (zoo_list[i]=='lark'):
        print(i+1)

