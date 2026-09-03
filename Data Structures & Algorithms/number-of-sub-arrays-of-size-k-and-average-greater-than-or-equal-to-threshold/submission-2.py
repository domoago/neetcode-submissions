class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        res = 0
        currSum = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                currSum -= arr[L]
                L += 1
            currSum += arr[R]
            if currSum / k >= threshold and R - L + 1 == k:
                res += 1
        return res
