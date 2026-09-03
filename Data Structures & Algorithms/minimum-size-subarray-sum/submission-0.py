class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        total = L = 0
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                res = min(res, R - L + 1)
                total -= nums[L]
                L += 1
        return res if res != len(nums) + 1 else 0
            