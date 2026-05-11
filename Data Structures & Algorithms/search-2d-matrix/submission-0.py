class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)
        left = 0
        right = n*m - 1
        while left <= right:
            mid = (right + left) // 2
            x = int(mid / n) 
            y = mid - (x * n)

            num = matrix[x][y]

            if num == target:
                return True
            
            if num < target:
                left = mid + 1
            else:
                right = mid - 1
            print(mid)
        return False