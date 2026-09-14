class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = prefix.copy()
        prev = 1
        post = 1
        for i in range(len(nums)):
            j = -i - 1
            prefix[i] = prev
            postfix[j] = post
            prev *= nums[i]
            post *= nums[j]
        return [prefix[i] * postfix[i] for i in range(len(nums))]