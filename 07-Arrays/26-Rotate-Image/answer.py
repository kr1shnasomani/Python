from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(n):
            left = 0
            right = n - 1

            while left < right:
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp

                left += 1
                right -= 1

        return matrix

# if __name__ == "__main__":
#     import ast
#     matrix = ast.literal_eval(input("Enter the matrix: "))
#     print(Solution().rotate(matrix))
