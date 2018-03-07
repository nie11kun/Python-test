# import this

def func1(x, *y):# *y as an tuple
    print(x)
    print(y[1])

func1(1, 2, 4)

def func2(x, y=2):
    print(y)
func2(1)
func2(1, 5)

def func3(x, **y):
    print(y)
func3(3, a=1, b=3)

num1 = (1, 2 ,3)
a, b, c = num1
print(a)
print(b)
print(c)
a, b = b, a
print(a)
print(b)

a, *b, c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)

a = 4 if 2 > 3 else 2
print(a)

for i in range(5):
    if i == 7:
        break
else:# is break had not been processed then run else part
    print("have not break")

try:
    print(1)
except ZeroDivisionError:
    print("0 found")
else:# if no exception then process else part
    print("working fine")

def func4():
    print("test to import this py file to others")
    
if __name__ == "__main__":
    print("this line will only been processed when directly run this python file, not beed imported to others")

