for row in range(1, 6):
    for col in range(row):
        print(chr(65 + col), end="")
    print()

# output:
# A
# AB
# ABC
# ABCD
# ABCDE
