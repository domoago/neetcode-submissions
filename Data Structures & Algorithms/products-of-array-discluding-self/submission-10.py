class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prev = 1
        for i in range(len(nums)):
            res[i] = prev
            prev *= nums[i]
        prev = 1
        for i in reversed(range(len(nums))):
            res[i] *= prev
            prev *= nums[i]
        return res