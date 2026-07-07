class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        DIRECTIONS = [(-1,0),(1,0),(0,1),(0,-1)]
        INF = 2147483647

        q = deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((1,i,j))

        while q:
            step,i,j = q.popleft()
            for x,y in DIRECTIONS:
                nx,ny = x+i,y+j
                if 0<=nx<ROW and 0<=ny<COL and grid[nx][ny] == INF:
                    grid[nx][ny] = step
                    q.append((step+1,nx,ny))
                    