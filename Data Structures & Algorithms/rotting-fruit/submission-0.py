class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = 2
                for dr, dc in directions:
                    if min(row + dr, col + dc) < 0 or row + dr >= ROWS or col + dc >= COLS or grid[row + dr][col + dc] != 1:
                        continue
                    queue.append([row + dr, col + dc])
                    grid[row + dr][col + dc] = 2
                    fresh -= 1
            time += 1
        return time if not fresh else -1