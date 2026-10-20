from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(0,1),(1,0)]
        self.result = 0

        
        def dfs(i,j):
            cur = 0
            if i == m-1 and j == n-1:
                return 1
            for x,y in directions:
                ni,nj = i+x,j+y
                if 0<=ni<m and 0<=nj<n:
                    cur += dfs(ni,nj)
            return cur

        return dfs(0,0)
