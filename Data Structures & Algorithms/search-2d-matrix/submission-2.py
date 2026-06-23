class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topRow = 0
        bottomRow = len(matrix) - 1
        while bottomRow >= topRow:
            row = (topRow + bottomRow) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            elif matrix[row][0] > target:
                bottomRow = row - 1
            elif matrix[row][-1] < target:
                topRow = row + 1
        if bottomRow < topRow:
            return False
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
        return False
