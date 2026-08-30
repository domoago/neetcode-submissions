class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        def dfs(row, col):
            if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            count = 1
            count += dfs(row - 1, col)
            count += dfs(row + 1, col)
            count += dfs(row, col + 1)
            count += dfs(row, col - 1)
            return count
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j))
        return res
