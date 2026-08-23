class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        currMax = 0
        for num in nums:
            if num == 1:
                currMax += 1
            else:
                currMax = 0
            max = currMax if currMax > max else max
        return max