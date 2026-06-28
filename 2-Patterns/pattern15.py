for row in range(5, 0, -1):
    for col in range(row):
        print(chr(65 + col), end="")
    print()

# output:
# ABCDE
# ABCD
# ABC
# AB
# A
