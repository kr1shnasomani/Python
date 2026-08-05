class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(left, right):
            if left >= right:
                return True

            if not s[left].isalnum():
                return check(left + 1, right)

            if not s[right].isalnum():
                return check(left, right - 1)

            if s[left].lower() != s[right].lower():
                return False

            return check(left + 1, right - 1)

        return check(0, len(s) - 1)

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(Solution().isPalindrome(s))
