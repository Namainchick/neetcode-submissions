class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # True is just bought False is just sold
        def dfs(index,bought):
            if index >= n:
                return 0

            if bought:
                return max(dfs(index+2,False)+prices[index],dfs(index+1,True))
            else:
                return max(dfs(index+1,True)-prices[index],dfs(index+1,False))

        return dfs(0,False)


"""
[1,3,4,0,4]
-1 i
   i
"""