class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leftPointer = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[leftPointer] = nums[i]
                leftPointer += 1
                k += 1
        return k