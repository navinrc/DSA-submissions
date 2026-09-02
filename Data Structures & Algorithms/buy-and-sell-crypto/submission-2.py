class Solution:
    # sliding window approach - solving after looking at solution
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                cur_price = prices[right] - prices[left]
                max_profit = max(max_profit,cur_price)
            else:
                left = right # we move the left pointer to the lowest price to maximize profits
            right += 1
        return max_profit