class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in t:
            if char not in count:
                return False
            count[char] -= 1

            if count[char] < 0:
                return False

        return True

if __name__ == "__main__":
    s_input = str(input("Enter the first string: "))
    t_input = str(input("Enter the second string: "))
    print(Solution().isAnagram(s_input, t_input))
