class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])

        i,j = 0,COL-1

        while i < ROW and j >= 0:
            num = matrix[i][j]
            if num == target:
                return True
            elif num > target:
                j -= 1
            else:
                i += 1

        return False