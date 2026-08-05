class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in s_to_t:
                if s_to_t[ch1] != ch2:
                    return False

            if ch2 in t_to_s:
                if t_to_s[ch2] != ch1:
                    return False

            s_to_t[ch1] = ch2
            t_to_s[ch2] = ch1

        return True

if __name__ == "__main__":
    s = str(input("Enter first string: "))
    t = str(input("Enter second string: "))
    print(Solution().isIsomorphic(s, t))