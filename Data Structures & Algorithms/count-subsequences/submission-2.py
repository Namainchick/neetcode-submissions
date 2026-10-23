class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        ns = len(s)
        nt = len(t)
        
        dp = [[-1] * nt for _ in range(ns)]
        def dfs(i,j):
            if j == nt:
                return 1
            
            if i == ns:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            sol = 0
            for x in range(i,ns):
                if s[x] == t[j]:
                    sol += dfs(x+1,j+1)
                    
            dp[i][j] = sol
            return sol

        return dfs(0,0)