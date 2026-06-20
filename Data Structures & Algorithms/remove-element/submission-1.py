class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leftPointer = 0
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
               k -= 1
            else:
                nums[leftPointer] = nums[i]
                leftPointer += 1
        return k