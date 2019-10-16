try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("can not use zero as division")

try:
    print(10 + "num")
    print("num" / 2)
except ZeroDivisionError:
    print("zero accur")
except (ValueError, TypeError):
    print("error")
    # raise
finally:
    print("this will be showed anyway")

def func7(x):
    assert x > 0
    num = x * 5
    assert (num < 20), "bigger than 20"
    return num

num = func7(3)
print(num)

file1 = open("file.txt", "r")
print(file1.read(2))#read first 2
print(file1.read(2))#read 3 4
print(file1.readlines(1))
for line in file1:
    print(line)
file1.close()

try:
    file2 = open("file.txt", "w")
    for i in range(5):
        num = file2.write("the new word been writed\n")
    print(num)
finally:
    file2.close()
"""
def func9():
    print("hi")
num9 = func9()
print(num9)
"""
age = {"a": 24, "b": 25}
print(age["a"])

