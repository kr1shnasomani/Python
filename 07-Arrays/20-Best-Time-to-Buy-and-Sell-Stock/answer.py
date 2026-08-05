from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        max_profit = 0

        n = len(prices)

        for i in range(1, n):
            if prices[i] > best_buy:
                today_profit = prices[i] - best_buy
                max_profit = max(max_profit, today_profit)
            
            best_buy = min(best_buy, prices[i])

        return max_profit

if __name__ == "__main__":
    prices = list(map(int, input("Enter the stock prices: ").split()))
    print(Solution().maxProfit(prices))