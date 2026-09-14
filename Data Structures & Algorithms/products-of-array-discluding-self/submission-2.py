class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        prev = 1
        for i in range(len(prefix)):
            prefix[i] = prev
            prev *= nums[i]
        prev = 1
        for i in reversed(range(len(prefix))):
            postfix[i] = prev
            prev *= nums[i]
        return [prefix[i] * postfix[i] for i in range(len(nums))]