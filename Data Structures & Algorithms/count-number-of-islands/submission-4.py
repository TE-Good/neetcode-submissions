class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def discover(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != "1":
                return

            grid[r][c] = "0"
            discover(r + 1, c)
            discover(r - 1, c)
            discover(r, c + 1)
            discover(r, c - 1)

        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    discover(row, col)
                    islands += 1
        return islands
