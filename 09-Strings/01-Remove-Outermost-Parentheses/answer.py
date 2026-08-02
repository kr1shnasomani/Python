class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_count = 0
        ans = []

        for ch in s:
            if ch == "(":
                if open_count > 0:
                    ans.append(ch)
                open_count += 1
            else:
                open_count -= 1
                if open_count > 0:
                    ans.append(ch)

        return "".join(ans)

# if __name__ == "__main__":
#     s = str(input("Enter the string: "))
#     print(Solution().removeOuterParentheses(s))