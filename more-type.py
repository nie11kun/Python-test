nums = {1: "one", 2: "two", 3: "three"}

print(1 in nums)
print(5 in nums)

print(nums.get(1))
print(nums.get(123))
print(nums.get(45, "not in the dictronary"))

# tuple is immutable
tuple1 = ("one", "two", "three")
print(tuple1[0])

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(nums[2:6])
print(nums[5:])
print(nums[1:5:2])
print(nums[1:-1])

cubes = [i**3 for i in range(5)]
print(cubes)

cubes2 = [i**2 for i in range(10) if i**2 % 2 == 0]
print(cubes2)


num9 = "{x}, {y}".format(x = 4, y = 5)
print(num9)

print(", ".join(["one", "two", "three"]))
print("hello me".replace("me", "world"))
print("this is test".startswith("this"))
print("will be upper".upper())
print("WILL BE LOWWER".lower())
print("spam, last, your".split(", "))

print(max(1, 2, 4, 6, 9))
print(abs(-45))
print(sum([1, 5, 8]))

num = [1, 4, 6, 7, 9]

if all(i > 0 for i in num):
    print("all bigger than 0")
if any(i % 2 == 0 for i in num):
    print("at least one is")
for v in enumerate(num):
    print(v)

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = input("enter the file name: ")
with open(filename) as f:
    text = f.read()
print(text)


