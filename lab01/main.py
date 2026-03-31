#calc
from calc import get_distances
print(get_distances())

#01.cir
from circle import ps,fp,sp
print(ps())
print(fp())
print(sp())

#02.oper
from expr import solve_25, calculate, check

res = calculate()
print(res)
print(f"Решение: {solve_25()} = 25")

#3.mov
from movies import first, last, second, second_last, get_movies

print(first())
print(last())
print(second())
print(second_last())

print("---")
#4.fam
from family import ors , ro

print(ro())
print(ors())

print("---")
#5.zoo

from zoo import bear, birds, elep, find
print(bear())
print(birds())
print(elep())
print(find())

print("---")

#6.song
from song import zp, pes;
print(zp())
print(pes())

print("---")
#7 secr
from sec import mess

print(mess())

print("---")

#8 gard
from gard import res
print(res())

print("---")
#9 shop

from shop import zd
    
print(zd())

print("---")
#10 store

from store import res
print(res())