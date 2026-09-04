class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        R = 0
        st = set()
        while R < len(nums):
            while R < len(nums) and nums[R] in st:
                R += 1
            if R == len(nums):
                return L
            nums[L] = nums[R]
            st.add(nums[L])
            L += 1
            R += 1
        return L