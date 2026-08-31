class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr = [0] * n
        for i in range(m):
            curr[-1] = 1
            prev = curr.copy()
            for j in reversed(range(n)):
                if j + 1 < n:
                    curr[j] = curr[j + 1] + curr[j]
        return curr[0]