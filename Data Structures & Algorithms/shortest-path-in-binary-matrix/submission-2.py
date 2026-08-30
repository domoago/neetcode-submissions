class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return -1
        neighbors = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        length = 1
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                for dr, dc in neighbors:
                    if min(row + dr, col + dc) < 0 or row + dr >= ROWS or col + dc >= COLS or (row + dr, col + dc) in visited or grid[row + dr][col + dc] == 1:
                        continue
                    queue.append((row + dr, col + dc))
                    visited.add((row + dr, col + dc))
            length += 1
        return -1