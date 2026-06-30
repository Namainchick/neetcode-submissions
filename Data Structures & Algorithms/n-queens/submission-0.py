class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = set()
        diag1 = set()  
        diag2 = set()
        
        self.result = []

        def backtrack(row,current):
            if len(current) == n:
                board = []
                for col in current:
                    board.append("." * col + "Q" + "." * (n - col - 1))
                self.result.append(board.copy())
                return 

            for col in range(n):
                if col not in column and (row-col) not in diag1 and (row+col) not in diag2:
                    column.add(col)
                    diag1.add(row-col)
                    diag2.add(row+col)

                    current.append(col)
                    backtrack(row+1,current)
                    current.pop()

                    column.remove(col)
                    diag1.remove(row-col)
                    diag2.remove(row+col)

       
        backtrack(0,[])

        return self.result
        
