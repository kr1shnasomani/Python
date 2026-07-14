x = int(input())
y = int(input())

while y != 0:
    remainder = x % y
    x = y
    y = remainder

print(x)