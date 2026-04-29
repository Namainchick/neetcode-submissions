class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        mini = 1000
        for i in range(len(prices)):
            mini = min(mini,prices[i])
            dp[i] = prices[i] - mini
        maxi = 0
        for i in dp:
            maxi = max(maxi,i)
        return maxi
        
