class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        currMax = 0
        for num in nums:
            if num == 1:
                currMax += 1
            else:
                currMax = 0
            ans = max(ans, currMax)
        return ans
