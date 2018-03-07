from itertools import count, accumulate, takewhile, product, permutations

print((lambda x: x ** 2 + 5) (4))

num = lambda x: x + 7
print(num(3))

nums = [1, 4, 44, 6, 5]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))

def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)

def num4(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(num4(7)))

def decor(func):
    def wrap():
        print("=======")
        func()
        print("=======")
    return wrap

def text_field():
    print("hello")

text_field = decor(text_field)
text_field()

@decor
def next_text():
    print("some new word")
next_text()

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(5))

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)
def is_odd(x):
    return not is_even(x)
print(is_even(17))
print(is_odd(20))

num_set = {1, 4 ,5 , 6}
word_set = set([3, 5, 0 ,55])
print(3 in num_set)
print(5 not in word_set)

num5 = {1, 4, 1, 5, 5, 4, 8}
print(num5)
num5.add(-1)
num5.remove(1)
print(num5)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

for i in count(3):
    print(i)
    if i > 10:
        break

num6 = list(accumulate(range(8)))
print(num6)
print(list(takewhile(lambda x: x > 10, num6)))
print(list(filter(lambda x: x > 10, num6)))

cuple1 = ("a", "b")

print(list(product(cuple1, range(2))))
print(list(permutations(cuple1)))

