class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols = len(matrix),len(matrix[0])
        self.dp = [[0 for i in range(cols+1)] for j in range(rows+1)]

        for i in range(rows):
            pre_sum = 0
            for j in range(cols):
                above = self.dp[i][j+1]
                pre_sum += matrix[i][j]
                self.dp[i+1][j+1] = pre_sum + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bot_right = self.dp[row2+1][col2+1]
        top = self.dp[row1][col2+1]
        left = self.dp[row2+1][col1]
        top_left = self.dp[row1][col1]

        return bot_right - top - left + top_left
        



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)