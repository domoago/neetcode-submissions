class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        prev = ""
        L = 0
        for R in range(1, len(arr)):
            if arr[R - 1] > arr[R] and prev != '>':
                prev = '>'
                res = max(res, R - L + 1)
            elif arr[R - 1] < arr[R] and prev != '<':
                prev = '<'
                res = max(res, R - L + 1)
            else:
                if arr[R - 1] == arr[R]:
                    R += 1
                L = R - 1
        return res