class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            if target > numbers[L] + numbers[R]:
                L += 1
            elif target < numbers[L] + numbers[R]:
                R -= 1
            else:
                return [L + 1, R + 1]
        return [L, R]