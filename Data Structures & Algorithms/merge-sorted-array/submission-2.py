class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        leftArr = nums1[0:m]
        leftPtr = m - 1
        rightPtr = n - 1
        mergingPtr = m + n - 1
        while leftPtr >= 0 and rightPtr >= 0:
            if leftArr[leftPtr] > nums2[rightPtr]:
                nums1[mergingPtr] = leftArr[leftPtr]
                leftPtr -= 1
            else:
                nums1[mergingPtr] = nums2[rightPtr]
                rightPtr -= 1
            mergingPtr -= 1

        while leftPtr >= 0:
            nums1[mergingPtr] = leftArr[leftPtr]
            leftPtr -= 1
            mergingPtr -= 1
        while rightPtr >= 0:
            nums1[mergingPtr] = nums2[rightPtr]
            rightPtr -= 1
            mergingPtr -= 1
    
        