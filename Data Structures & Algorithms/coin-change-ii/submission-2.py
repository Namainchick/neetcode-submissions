class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}

        def dfs(i,cur):
            if (i,cur) in dp:
                return dp[(i,cur)]
            if cur == amount: return 1
            if cur > amount:
                return 0
            ways = 0
            for j in range(i,n):
                ways += dfs(j,cur+coins[j])
            dp[(j,cur)] = ways
            return ways

        return dfs(0,0)
            

