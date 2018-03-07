class Animal:
    def __init__(self, color, legs):
        legs = 5
        self.color = color
        self.legs = legs
    def sound(self):
        print("wow")

class Cat(Animal):
    def sound(self):
        print("miaomiao")
        super().sound()

cat1 = Cat("red", 4)
print(cat1.color)
cat1.sound()

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
num1 = Vector2D(1, 2)
num2 = Vector2D(3, 4)
result = num1 + num2# same as num1.__add__(num2)
print(result.x)
'''
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
'''
class SpecialStr:
    def __init__(self, cont):
        self.cont = cont
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
str1 = SpecialStr("spam")
str2 = SpecialStr("other words")

print(str1 / str2)

'''
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=
'''

class ComStr:
    def __init__(self, cont):
        self.cont = cont
    def __gt__(self, other):
        for i in range(len(other.cont) + 1):
            r = other.cont[:i] + ">" + self.cont + ">" + other.cont[i:]
            print(r)
str1 = ComStr("abc")
str2 = ComStr("def")
str1 > str2

'''
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in
'''

class Test1:
    def __init__(self, cont):
        self.cont = cont
    def __getitem__(self, index):
        return self.cont[index + 1]
    def __len__(self):
        return len(self.cont) + 2
test1 = Test1([1, 2, 5, 6])
print(test1[0])
print(len(test1))

class Test2:
    __doNotUseOutside = 1
    def __init__(self, cont):
        self._hiddenedCont = cont
test2 = Test2([1, 2, 3])
print(test2._hiddenedCont)
# print(test2.__doNotUseOutside)

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calculate_area(self):
        return self.x * self.y
    @classmethod
    def new_square(cls, length):
        return cls(length, length)

test3 = Rectangle.new_square(5)
print(test3.calculate_area())

class Test4:
    def __init__(self, cont):
        self.cont = cont
    @staticmethod
    def func1(x):
        if x == 1:
            raise ValueError("there has 1 in list")
        else:
            return True
list1 = [2, 5, 7, 9]
if all(Test4.func1(i) for i in list1):
    print("there is not have 1")

class Test5:
    def __init__(self, cont):
        self.cont = cont
        self._num1 = False
    @property
    def num1(self):
        return self._num1
    @num1.setter
    def num1(self, x):
        if x:
            password = input("enter the password: ")
            if password == "123456":
                self._num1 = x
            else:
                ValueError("incorrect password")

test5 = Test5(123)
print(test5.num1)
test5.num1 = True
print(test5.num1)

