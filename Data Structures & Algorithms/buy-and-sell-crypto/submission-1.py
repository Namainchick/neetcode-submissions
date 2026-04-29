class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = float('inf')
        for i in range(len(prices)):
            mini = min(mini,prices[i])
            maxi = max(maxi,prices[i]-mini)
        return maxi
        
