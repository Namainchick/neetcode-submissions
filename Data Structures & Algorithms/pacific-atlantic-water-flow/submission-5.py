class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        cols = len(heights[0])
        rows = len(heights)
        pacific, atlantic = [[0 for j in range(cols)] for i in range(rows)],[[0 for j in range(cols)] for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    pacific[i][j] = 1
                if i-1 >= 0 and pacific[i-1][j] == 1 and heights[i-1][j] <= heights[i][j]:
                    pacific[i][j] = 1
                if j-1 >= 0 and pacific[i][j-1] == 1 and heights[i][j-1] <= heights[i][j]:
                    pacific[i][j] = 1

        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if i == rows-1 or j == cols-1:
                    atlantic[i][j] = 1
                if i+1 < rows:
                    if atlantic[i+1][j] == 1 and heights[i+1][j] <= heights[i][j]:
                        atlantic[i][j] = 1
                if j+1 < cols:
                    if atlantic[i][j-1] == 1 and heights[i][j+1] <= heights[i][j]:
                        atlantic[i][j] = 1

        out = []

        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    out.append([i,j])

        print(atlantic,pacific)

        return out