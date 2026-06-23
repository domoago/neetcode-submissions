class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchRow(nums: List[int], target: int) -> bool:
            L = 0
            R = len(nums) - 1
            while L <= R:
                mid = (L + R) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    R = mid - 1
                elif nums[mid] < target:
                    L = mid + 1
            return False
        L = 0
        R = len(matrix) - 1
        while L <= R:
            mid = (L + R) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return searchRow(matrix[mid], target)
            elif matrix[mid][0] > target:
                R = mid - 1
            elif matrix[mid][-1] < target:
                L = mid + 1
        return False