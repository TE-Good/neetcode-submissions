class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def discoverIsland(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if grid[row][col] != "1":
                return

            grid[row][col] = "0"

            discoverIsland(row + 1, col)
            discoverIsland(row - 1, col)
            discoverIsland(row, col + 1)
            discoverIsland(row, col - 1)

        num_of_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    discoverIsland(row, col)
                    num_of_islands += 1
        return num_of_islands
