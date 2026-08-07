class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return goal in (s+s)

if __name__ == "__main__":
    s_input = str(input("Enter the first string: "))
    goal_input = str(input("Enter the second string: "))
    print(Solution().rotateString(s_input, goal_input))
