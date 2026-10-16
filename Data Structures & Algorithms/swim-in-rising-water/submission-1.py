class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[-1] * n for _ in range(n)]
        heap = [(grid[0][0],0,0)]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        while heap:
            h,i,j = heapq.heappop(heap)
            if dp[i][j] != -1: continue

            #check neigbours
            smallest = (float('inf'))
            for x,y in directions:
                ni,nj = i+x,j+y
                if 0<=ni<n and 0<=nj<n:
                    if dp[ni][nj] != -1:
                        smallest = min(smallest,dp[ni][nj])
                    else:
                        heapq.heappush(heap,(grid[ni][nj],ni,nj))

            dp[i][j] = max(h,smallest) if smallest != float('inf') else h 
        print(dp)

        return dp[n-1][n-1]

                

