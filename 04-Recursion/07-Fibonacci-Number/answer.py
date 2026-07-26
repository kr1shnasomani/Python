class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        result = self.fib(n - 1) + self.fib(n - 2)
        return result

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(Solution().fib(n))