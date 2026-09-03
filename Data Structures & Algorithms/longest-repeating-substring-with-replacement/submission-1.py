class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = currMax = res = 0
        count = {}
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            currMax = max(currMax, count[s[R]])
            while R - L + 1 - currMax > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res