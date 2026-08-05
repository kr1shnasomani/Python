class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0

        for ch in s:
            if ch == "(":
                depth += 1
                max_depth = max(max_depth, depth)
            elif ch == ")":
                depth -= 1

        return max_depth

if __name__ == "__main__":
    s = str(input("Enter the string: "))
    print(Solution().maxDepth(s))