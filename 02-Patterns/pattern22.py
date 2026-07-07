n = 4
size = 2 * n - 1
for row in range(size):
    for col in range(size):
        distance = min(row, col, size - 1 - row, size - 1 - col)
        print(n - distance, end=" ")
    print()

# output:
# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 
