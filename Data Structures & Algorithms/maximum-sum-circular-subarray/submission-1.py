class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = currMin = currMax = 0
        globalMin = globalMax = nums[0]
        for num in nums:
            currMin = num + min(currMin, 0)
            currMax = num + max(currMax, 0)
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
            total += num
        return max(total - globalMin, globalMax) if globalMax > 0 else globalMax
