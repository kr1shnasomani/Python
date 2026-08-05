class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = len(s)
        total = 0

        for i in range(n):
            if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
                total = total - roman[s[i]]
            else:
                total = total + roman[s[i]]

        return total

if __name__ == "__main__":
    s = str(input("Enter the roman numeral: "))
    print(Solution().romanToInt(s))
