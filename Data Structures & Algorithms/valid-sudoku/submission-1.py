class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] in row[i] and board[i][j] != ".":
                    return False
                else:
                    row[i].add(board[i][j])
                if board[j][i] in col[j] and board[j][i] != ".":
                    return False
                else:
                    col[j].add(board[j][i])

                if board[i][j] in box[(i//3)*3+(j//3)] and board[i][j] != ".":
                    return False
                else:
                    box[(i//3)*3+(j//3)].add(board[i][j])
        return True