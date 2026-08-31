class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        memo = {}
        def dfs(i, j):
            if i == ROWS or j == COLS:
                return 0
            elif obstacleGrid[i][j]:
                return 0
            elif (i, j) in memo:
                return memo[(i, j)]
            elif i == ROWS - 1 and j == COLS - 1:
                return 1
            else:
                memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
                return memo[(i, j)]
        return dfs(0, 0)