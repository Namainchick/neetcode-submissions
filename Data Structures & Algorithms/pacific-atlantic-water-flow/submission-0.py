class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        pacific = set()
        atlantic = set()
        result = []

        ROW = len(heights)
        COL = len(heights[0])

        for i in range(ROW):
            for j in range(COL):
                if i == 0 or j == 0:
                    pacific.add((i,j))
                if i == ROW-1 or j == COL-1:
                    atlantic.add((i,j))

        def dfs(ocean,i,j):
            for x,y in directions:
                nx,ny = i+x,j+y
                if 0<=nx<ROW and 0<=ny<COL and (nx,ny) not in pacific and heights[i][j] <= heights[nx][ny]:
                    ocean.add((nx,ny))
                    dfs(ocean,nx,ny)

        p = pacific.copy()
        a = atlantic.copy()
        for i,j in p:
            dfs(pacific,i,j)
        for i,j in a:
            dfs(atlantic,i,j)

        for i in range(ROW):
            for j in range(COL):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i,j])
        return result

