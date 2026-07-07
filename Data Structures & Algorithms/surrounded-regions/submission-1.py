class Solution:
    def solve(self, board: List[List[str]]) -> None:
        islands = []
        safe = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        ROW = len(board)
        COL = len(board[0])

        def dfs(i,j):
            if (i,j) in safe:
                return 
            safe.add((i,j))
            for x,y in directions:
                ni,nj = i+x,j+y
                if 0<=ni<ROW and 0<=nj<COL and (i,j) not in safe and board[ni][nj] == "O":
                    dfs(ni,nj)

        for i in range(ROW):
            for j in range(COL):
                if (i == 0 or j == 0 or i == ROW-1 or j == COL-1) and board[i][j] == "0":
                    dfs(i,j)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "0" and (i,j) not in safe:
                    board[i][j] = "X"

        
