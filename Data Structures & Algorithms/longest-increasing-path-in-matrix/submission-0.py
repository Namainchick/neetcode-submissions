class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        brute force:
        for each index do dfs and store longest for all. 
        n^4

        better:
        we cant be better than n^2 because we have to check each one atleast once. 
        could storing best way and then relaxation work.
        """
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        n  = len(matrix)
        memo = [[-1] * n for _ in range(n)]

        def dfs(i,j):
            if memo[i][j] != -1:
                return memo[i][j]
            best = 0
            for x,y in directions:
                ni,nj = i+x,j+y
                if 0<=ni<n and 0 <=nj<n and matrix[i][j] < matrix[ni][nj]:
                    best = max(best,dfs(ni,nj))
            
            memo[i][j] = best + 1
            return memo[i][j]
        
        res = 0
        for i in range(n):
            for j in range(n):
                if memo[i][j] == -1:
                    res = max(res,dfs(i,j))
            
        return res
    

