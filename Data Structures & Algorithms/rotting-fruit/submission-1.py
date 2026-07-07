class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
        ROW = len(grid)
        COL = len(grid[0])

        q = deque()
        time = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((0,i,j))

        while q:
            time,i,j = q.popleft()
            for x,y in DIRECTIONS:
                nx,ny = i+x,j+y
                if 0<=nx<ROW and 0<=ny<COL and grid[nx][ny] == 1:
                    q.append((time+1,nx,ny))
                    grid[nx][ny] = 2

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1

        return time