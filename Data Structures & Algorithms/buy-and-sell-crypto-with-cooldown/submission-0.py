class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n

        def max_profit(index,coin):
            if index >= n:
                return 0
            
            sell_buy = max_profit(index+2,False) + prices[index] if coin else max_profit(index+1,True) - prices[index]
            skip = max_profit(index+1,coin)

            return max(skip,sell_buy)

        return max_profit(0,False)
