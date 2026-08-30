class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = {}
        def dfs(i):
            if i >= n:
                return i == n
            if i in self.cache:
                return self.cache[i]
            self.cache[i] = dfs(i + 1) + dfs(i + 2)
            return self.cache[i]
        return dfs(0)
            
        
