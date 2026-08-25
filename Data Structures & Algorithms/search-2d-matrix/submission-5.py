class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid]) - 1]:
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    midArr = (left + right) // 2
                    if matrix[mid][midArr] == target:
                        return True
                    elif target < matrix[mid][midArr]:
                        right = midArr - 1
                    else:
                        left = midArr + 1
                return False
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        return False