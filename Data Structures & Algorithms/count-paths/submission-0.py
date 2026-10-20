class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(0,1),(1,0)]
        self.result = 0

        def dfs(i,j):
            if i == m-1 and j == n-1:
                self.result += 1
            for x,y in directions:
                ni,nj = i+x,j+y
                if 0<=ni<m and 0<=nj<n:
                    dfs(ni,nj)
            
        dfs(0,0)
        return self.result