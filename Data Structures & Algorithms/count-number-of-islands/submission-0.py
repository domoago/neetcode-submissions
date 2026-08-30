class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(row, col):
            if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res