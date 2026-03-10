from sys import *


def rx(n):
    if n == 1:
        return 3**0.5
    return (3 + rx(n-1))**0.5
    
def x(n):
    sum=0
    tek=0
    for i in range(n):
        tek=(3+tek)**0.5
        sum+=tek
    return tek

    

n=3
print(rx(n))
print(x(n))

