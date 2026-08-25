class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        leftArr = nums1[0:m]
        rightArr = nums2[0:n]
        leftPtr = rightPtr = mergingPtr = 0
        while leftPtr < m and rightPtr < n:
            if leftArr[leftPtr] < rightArr[rightPtr]:
                nums1[mergingPtr] = leftArr[leftPtr]
                leftPtr += 1
            else:
                nums1[mergingPtr] = rightArr[rightPtr]
                rightPtr += 1
            mergingPtr += 1

        while leftPtr < m:
            nums1[mergingPtr] = leftArr[leftPtr]
            leftPtr += 1
            mergingPtr += 1
        while rightPtr < n:
            nums1[mergingPtr] = rightArr[rightPtr]
            rightPtr += 1
            mergingPtr += 1
    
        