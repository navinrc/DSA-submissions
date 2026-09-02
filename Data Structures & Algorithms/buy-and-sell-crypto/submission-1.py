class Solution:
    '''
    max profit = prices.getIndex(max) - prices.getIndex(min) 
    traverse - 2p 
    ------
    max prof = 0
    left,right = 0, len(prices)
    iterate prices check left < right always :
        find curr_iter_prof -> prices[right] - prices[left]
        check prices[left] < prices[right]  and curr_iter_prof > max prof
            max prof = curr_iter_prof
        else 
            right - 1
        return max prof
    '''
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            left = i
            right = len(prices) - 1
            while left < right:
                curr_iter_prof = prices[right] - prices[left]
                if curr_iter_prof > 0 and curr_iter_prof > max_profit:
                    max_profit = curr_iter_prof
                else: 
                    right -= 1
        return max_profit


            
            