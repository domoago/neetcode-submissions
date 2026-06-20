class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = arr[i]
            arr[i] = currMax
            currMax = max(currMax, newMax)
        return arr