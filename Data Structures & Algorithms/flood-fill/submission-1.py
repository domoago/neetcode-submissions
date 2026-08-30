class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]
        if og == color:
            return image
        def dfs(row, col):
            rows = len(image)
            cols = len(image[0])
            if min(row, col) < 0 or row >= rows or col >= cols or image[row][col] != og:
                return
            if image[row][col] != color:
                image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            return
        dfs(sr, sc)
        return image