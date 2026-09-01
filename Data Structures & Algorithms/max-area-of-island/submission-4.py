class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.best = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        self.current = 1
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):
            grid[i][j] = 0
            self.best = max(self.best,self.current)
            for x,y in directions:
                new_i,new_j = x+i, y+j
                if 0 <= new_i < rows and 0 <= new_j < cols: 
                    if grid[new_i][new_j] == 1:
                        self.current += 1
                        dfs(new_i,new_j)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.current = 1
                    dfs(i,j)

        return self.best

                    
