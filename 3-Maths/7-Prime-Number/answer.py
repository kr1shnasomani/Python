n = int(input())

result = []

i = 1
if n <= 1:
    print("false")
else:
    while i <= n:
        if n % i == 0:
            result = result + [i]
        i += 1
    if len(result) == 2:
        print("true")
    else:
        print("false")