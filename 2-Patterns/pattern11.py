for row in range(5):
    for col in range(row + 1):
        print((row + col + 1) % 2, end=" ")
    print()

# output:
# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 
