n = 5
for row in range(1, n + 1):
    print("*" * row + " " * (2 * (n - row)) + "*" * row)
for row in range(n - 1, 0, -1):
    print("*" * row + " " * (2 * (n - row)) + "*" * row)

# output:
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
