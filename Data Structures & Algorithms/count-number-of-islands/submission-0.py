class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.locations = [(1,0),(-1,0),(0,1),(0,-1)]
        self.result = 0

        def dfs(i,j):  
            #mark all connecting 1's
            grid[i][j] = "x"
            for x,y in self.locations:
                nx,ny = i+x,j+y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                    dfs(nx,ny)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.result += 1
                    dfs(i,j)

        return self.result

        

