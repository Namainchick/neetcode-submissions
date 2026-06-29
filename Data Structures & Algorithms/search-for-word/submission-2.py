class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows = len(board)
        cols = len(board[0])

        def backtrack(row, col, index):
            if index == len(word):
                return True
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and board[new_row][new_col] == word[index]):
                    visited.add((new_row, new_col))
                    if backtrack(new_row, new_col, index+1):  
                        return True
                    visited.remove((new_row, new_col))    
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if backtrack(i,j,1):
                        return True
                    visited.remove((i,j))

        return False

"""
that must be a hard. damn.
"""
