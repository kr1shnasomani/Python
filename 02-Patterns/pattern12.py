n = 4
for row in range(1, n + 1):
    for i in range(1, row + 1):
        print(i, end="")
    print(" " * (2 * (n - row)), end="")
    for i in range(row, 0, -1):
        print(i, end="")
    print()

# output:
# 1      1
# 12    21
# 123  321
# 12344321
