import random
from math import pi, sqrt as square_root

def func1():
    print("lalala")
func1()
# this is comment
def func2(x, y):
    print(x + y)
func2(3, 4)
"""
multipule lines comments
"""
def func3(x, y):
    if x > y:
        return x
    else:
        return y
num = func3(4, 5)
print(num)

func4 = func3

num = func4(6, 7)
print(num)

def func5(x, y):
    return x + y
def func6(func, x, y):
    return func(func(x, y), func(x, y))

print(func6(func5, 4, 5))

for i in range(5):
    print(random.randint(1, 6))
    
print(pi)

print(square_root(16))
