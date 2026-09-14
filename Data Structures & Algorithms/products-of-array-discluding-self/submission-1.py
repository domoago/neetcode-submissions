class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 2)
        postfix = [1] * (len(nums) + 2)
        prev = 1
        for i in range(len(nums)):
            prefix[i + 1] = nums[i] * prev
            prev = prefix[i + 1]
        prev = 1
        for i in reversed(range(len(nums))):
            postfix[i + 1] = nums[i] * prev
            prev = postfix[i + 1]
        return [prefix[i] * postfix[i + 2] for i in range(len(nums))]
