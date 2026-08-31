class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 2
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr
        return prev
