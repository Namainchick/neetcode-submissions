class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}

        def dfs(i,cur):
            if i >= n:
                return 0
            if (i,cur) in dp:
                return dp[(i,cur)]
            if cur == amount: return 1
            if cur > amount:
                return 0
            ways = 0
            ways += dfs(i,cur+coins[i]) + dfs(i+1,cur)
            dp[(i,cur)] = ways
            return ways

        return dfs(0,0)
            

