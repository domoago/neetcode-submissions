class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1
        queue = deque()
        visited = set()
        length = 1
        queue.append((0, 0))
        visited.add((0, 0))
        directions = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                if row == col and col == N - 1:
                    return length
                for dr, dc in directions:
                    if min(row + dr, col + dc) < 0 or max(row + dr, col + dc) >= N or grid[row + dr][col + dc] or (row + dr, col + dc) in visited:
                        continue
                    queue.append((row + dr, col + dc))
                    visited.add((row + dr, col + dc))
            length += 1
        return -1