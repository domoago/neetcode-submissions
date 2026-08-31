class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS= len(obstacleGrid[0])
        curr = [0] * COLS
        curr[-1] = 1
        for i in reversed(range(ROWS)):
            for j in reversed(range(COLS)):
                if obstacleGrid[i][j]:
                    curr[j] = 0
                elif j + 1 < COLS:
                    curr[j] += curr[j + 1]
        return curr[0]
