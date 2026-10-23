class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        ns = len(s)
        nt = len(t)

        def dfs(i,j):
            if j == nt:
                return 1
            
            if i == ns:
                return 0
            sol = 0
            for x in range(i,ns):
                if s[x] == t[j]:
                    sol += dfs(x+1,j+1)
            
            return sol

        return dfs(0,0)