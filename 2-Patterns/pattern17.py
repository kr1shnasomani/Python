n = 4
for row in range(n):
    print(" " * (n - row - 1), end="")
    for i in range(row + 1):
        print(chr(65 + i), end="")
    for i in range(row - 1, -1, -1):
        print(chr(65 + i), end="")
    print()

# output:
#    A
#   ABA
#  ABCBA
# ABCDCBA
