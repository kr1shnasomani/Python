from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            left = 0
            right = n - 1

            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]

                left += 1
                right -= 1

        return matrix

if __name__ == "__main__":
    n_input = int(input("Enter number of rows: "))
    matrix_input = [list(map(int, input().split())) for _ in range(n_input)]
    print(Solution().rotate(matrix_input))
