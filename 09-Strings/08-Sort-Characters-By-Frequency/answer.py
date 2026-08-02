class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        sorted_keys = sorted(count, key=count.get, reverse=True)

        result = []
        
        for char in sorted_keys:
            result.append(char * count[char])

        return "".join(result)

# if __name__ == "__main__":
#     s = str(input("Enter the string: "))
#     print(Solution().frequencySort(s))