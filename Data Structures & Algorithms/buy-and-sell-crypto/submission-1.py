class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_idx = sell_idx = 0
        best_profit = 0

        while sell_idx < len(prices):
            curr_profit = prices[sell_idx] - prices[buy_idx]
            best_profit = max(best_profit, curr_profit)
            sell_idx += 1
            if sell_idx < len(prices) and prices[sell_idx] < prices[buy_idx]:
                buy_idx = sell_idx
        
        return best_profit