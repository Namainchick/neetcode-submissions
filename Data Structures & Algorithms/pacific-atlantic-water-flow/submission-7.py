class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        out = []
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if j == cols-1 or i == rows-1:
                    atlantic.add((i,j))
                if j == 0 or i == 0:
                    pacific.add((i,j))


        def dfs(ocean,x,y):
            for i,j in directions:
                nx,ny = i+x,j+y
                if 0 <= nx < rows and 0 <= ny < cols and (nx,ny) not in ocean and heights[nx][ny] >= heights[x][y]:
                    ocean.add((nx,ny))
                    dfs(ocean,nx,ny)

        
        a = atlantic.copy()
        p = pacific.copy()

        for i,j in a:
            dfs(atlantic,i,j)
        for i,j in p:
            dfs(pacific,i,j)

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    out.append([i,j])

        return out
            

