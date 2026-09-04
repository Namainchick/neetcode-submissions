class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        time = -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((0,i,j))
        
        while queue:
            time,i,j = queue.popleft()
            for x,y in directions:
                ni,nj = i+x, j+y
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((time+1,ni,nj))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return time