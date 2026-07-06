class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.best = 0
        self.directions = [(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(i,j,best):
            grid[i][j] = 0
            best += 1
            for x,y in self.directions:
                nx,ny = i+x,j+y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    best = dfs(nx,ny,best)
            return best

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.best = max(self.best, dfs(i,j,0))

        return self.best