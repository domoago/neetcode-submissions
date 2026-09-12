class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]
        for row in range(1, ROWS + 1):
            prefixSum = 0
            for col in range(1, COLS + 1):
                prefixSum += matrix[row - 1][col - 1]
                self.prefixMatrix[row][col] = prefixSum + self.prefixMatrix[row - 1][col]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        return self.prefixMatrix[row2][col2] - self.prefixMatrix[row1 - 1][col2] - self.prefixMatrix[row2][col1 - 1] + self.prefixMatrix[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)