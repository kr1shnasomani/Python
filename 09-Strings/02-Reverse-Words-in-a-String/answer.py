class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()

        answer = " ".join(words)

        return answer

# if __name__ == "__main__":
#     s = str(input("Enter the string: "))
#     print(Solution().reverseWords(s))