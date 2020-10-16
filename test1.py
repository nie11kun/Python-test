print('hello')
print(2 + 2)
print(2**5) # n次方
print(int("2") + int("3"))
x = 7
print(x)
print(2 == 2)

if 2 < 3:
    print("2 less than 3")
else:
    if 3 > 2:
        print("3 big than 2")
    else:
        print("funny")

if 2 < 3:
    print()
elif 3 > 2:
    print()
else:
    print()

if (1 == 1) and (2==2):
    print(True)

if not 1 == 1:
    print(False)

i = 1
while i < 5:
    print(i)
    i += 1

i = 0
while 1 == 1:
    i += 1
    if i > 5:
        print("break")
        break
    if i % 2 ==0:
        continue
    print(i)

things = ["hea", [1, 2, 3], 0]
print(things[1])
print(things[2])
things[2] = 5
print(things[2])

num = [1, 2, 3]
print(num + [4, 5, 6])
print(num * 3)

print(0 in num)

print(1 not in num)

num.append(4)

print(len(num))

index = 1

num.insert(index, 10)
print(num[1])

num.remove(3)
print(num.index(2))

nums = list(range(10))
print(nums)

num2 = list(range(3, 8, 2))
print(num2)

colors = ["red", "blue", "white"]
for color in colors:
    print(color)

while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")

    user_input = input(": ")
    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("enter a number: "))
        num2 = float(input("enter another number: "))
        res = str(num1 + num2)
        print("the result is: " + res)
    elif user_input == "subtract":
        print()
    elif user_input == "multiply":
        print()
    elif user_input == "divide":
        print()
    else:
        print("unknown input")

str123 = '   lalala   lalala'
str123 = str123.strip()

print(str123)
