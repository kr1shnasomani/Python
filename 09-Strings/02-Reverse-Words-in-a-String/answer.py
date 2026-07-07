class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()

        answer = " ".join(words)
        
        return answer