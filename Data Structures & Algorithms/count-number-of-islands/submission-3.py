class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def discover_island(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if grid[row][col] != "1":
                return

            grid[row][col] = "0"

            discover_island(row + 1, col)
            discover_island(row - 1, col)
            discover_island(row, col + 1)
            discover_island(row, col - 1)


        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    discover_island(row, col)
                    islands += 1
        return islands
