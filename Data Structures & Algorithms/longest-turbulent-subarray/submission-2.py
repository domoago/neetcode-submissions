class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0
        res = R = 1
        prev = ""
        while R < len(arr):
            if arr[R - 1] < arr[R] and prev != "<":
                prev = "<"
                res = max(res, R - L + 1)
                R += 1
            elif arr[R - 1] > arr[R] and prev != ">":
                prev = ">"
                res = max(res, R - L + 1)
                R += 1
            else:
                R = R + 1 if arr[R - 1] == arr[R] else R
                L = R - 1
                prev = ""
        return res