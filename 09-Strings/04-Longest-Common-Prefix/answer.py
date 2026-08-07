from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            i = 0

            while i < len(prefix) and i < len(word):
                if prefix[i] == word[i]:
                    i += 1
                else:
                    break

            prefix = prefix[:i]

            if prefix == "":
                return ""

        return prefix

if __name__ == "__main__":
    strs_input = list(map(str, input("Enter the strings: ").split()))
    print(Solution().longestCommonPrefix(strs_input))
