class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        i,j = 0,cols-1

        while i < rows and j >= 0:
            number = matrix[i][j]
            if number == target:
                return True
            else:
                if number > target:
                    j -= 1
                else:
                    i += 1

        return False

        """
        [[1, 3, 5, 7]
        [10,11,16,20]
        [23,30,34,60]]
        """